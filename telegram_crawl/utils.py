import pandas as pd

def get_forward_channels_df(filepath):

    messages_df = pd.read_csv( 
                                filepath,
                                names=[ 'sender_id', 'text', 'date', 
                                        'id', 'webpage_url', 'webpage_id', 
                                        'reply_to', 'number_views', 'number_forwards', 
                                        'post_author', 'message', '_sender_id', 
                                        'sender_username', 'sender_title', 'channel_id', 
                                        'forwarded_from_channel_id', 'for_channel_id', 'for_channel_title', 
                                        'for_channel_username', 'for_channel_access_hash', 'origin_channel_id', 
                                        'origin_channel_username']
                            )

    forward_channel_df = messages_df[["for_channel_id", "for_channel_title", "for_channel_username", "for_channel_title"]]
    forward_channel_df.drop_duplicates(inplace=True)
    forward_channel_df.dropna(inplace=True)
    forward_channel_df["for_channel_id"] = forward_channel_df["for_channel_id"].apply(lambda x: str(int(x)))

    return forward_channel_df["for_channel_username"].tolist()


def get_crawled_channels(filepath):

    cr_channels_df = pd.read_csv(  
                                    filepath,
                                    names=["access_hash", "id", "title", "username"]
                                )

    return cr_channels_df["username"].tolist() 


def get_channel_info(chat_o):
    chat_d = {}

    chat_d["access_hash"] = chat_o.access_hash
    chat_d["id"] = chat_o.id
    chat_d["title"] = chat_o.title
    chat_d["username"] = chat_o.username
    
    return chat_d


async def get_message_info(channel_id, channel_username , message_o):
    mess_d = {}

    mess_d["sender_id"] = message_o.sender_id
    try:
        mess_d["text"] = message_o.text.replace("\n", " ")
    except:
        mess_d["test"] = message_o.text
    mess_d["date"] = message_o.date
    mess_d["id"] = message_o.id
    try:
        mess_d["webpage_url"] = message_o.media.webpage.url
        mess_d["webpage_id"] = message_o.media.webpage.id
    except:
        mess_d["webpage_url"] = ""
        mess_d["webpage_id"] = ""

    mess_d["reply_to"] = message_o.reply_to
    mess_d["number_views"] = message_o.views
    mess_d["number_forwards"] = message_o.forwards
    mess_d["post_author"] = message_o.post_author
    try:
        mess_d["message"] = message_o.message.replace("\n", " ")
    except:
        mess_d["message"] = message_o.message
    mess_d["_sender_id"] = str(message_o._sender.id)
    mess_d["sender_username"] = message_o._sender.username
    mess_d["sender_title"] = message_o._sender.title
    mess_d["channel_id"] = message_o.to_id.channel_id
    try:
        mess_d["forwarded_from_channel_id"] = message_o.fwd_from.from_id.channel_id
        forwarded_channel = await client.get_entity(mess_d["forwarded_from_channel_id"])
        mess_d["for_channel_id"] = forwarded_channel.id
        mess_d["for_channel_title"] = forwarded_channel.title
        mess_d["for_channel_username"] = forwarded_channel.username
        mess_d["for_channel_access_hash"] = forwarded_channel.access_hash
    except:
        mess_d["forwarded_from_channel_id"] = ""
        mess_d["for_channel_id"] = ""
        mess_d["for_channel_title"] = ""
        mess_d["for_channel_username"] = ""
        mess_d["for_channel_access_hash"] = ""

    mess_d["origin_channel_id"] = channel_id
    mess_d["origin_channel_username"] = channel_username

    return mess_d


def get_user_info(channel_id, channel_username, user_o):
    user_d = {}

    user_d["id"] = str(user_o["id"])
    user_d["access_hash"] = user_o["access_hash"]
    user_d["first_name"] = user_o["first_name"]
    user_d["last_name"] = user_o["last_name"]
    user_d["username"] = user_o["username"]
    user_d["status"] = user_o.status.__dict__
    user_d["phone"] = user_o["phone"]
    user_d["photo"] = user_o["photo"]

    user_d["origin_channel_id"] = channel_id
    user_d["origin_channel_username"] = channel_username

    return user_d
