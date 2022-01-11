import os
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.contacts import ResolveUsernameRequest
import csv
from IPython.core.debugger import Tracer
debughere = Tracer()



def get_channel_info(chat_o):
    chat_d = {}

    chat_d["access_hash"] = chat_o.access_hash
    chat_d["id"] = chat_o.id
    chat_d["title"] = chat_o.title
    chat_d["username"] = chat_o.username
    
    return chat_d


async def get_message_info(channel_id, channel_username ,message_o):
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



csv_channel_f = open('data/telegram_channels.csv', 'a', encoding='UTF8')
channel_writer = csv.writer(csv_channel_f)

csv_message_f = open('data/telegram_message.csv', 'a', encoding='UTF8')
message_writer = csv.writer(csv_message_f)

csv_user_f = open('data/telegram_user.csv', 'a', encoding='UTF8')
user_writer = csv.writer(csv_user_f)



creds_dict = {
    "api_id":"",
    "api_hash":"",
    "phone":"",
    "username":"",
}

for key in creds_dict.keys():
    creds_dict[key] = os.environ.get(key)
    try:
        del os.environ[key]
    except:
        pass

client = TelegramClient(creds_dict["username"], 
                        creds_dict["api_id"], 
                        creds_dict["api_hash"])

async def main():
    await client.start()
    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    search = 'Freie Sachsen'
    result = await client(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))

    for chat in result.chats:
        
        chat_dict = get_channel_info(chat)
        print(f"Crawl Users and Messages in channel {chat_dict['username']}")
        #channel_writer.writerow(chat_dict.values())

        # crawl channel users
        try:
            channel = await client(ResolveUsernameRequest(chat_dict["username"]))
            user_list = await client.get_participants(entity=channel)
            print(f"User Crawl in {chat_dict['username']} is allowed. NOM NOM NOM")
            for _user in user_list:
                user_dict = get_user_info(chat_dict["id"], chat_dict["username"], _user)
                #user_writer.writerow(user_dict.values())
        except:
            print(f"User Crawl in {chat_dict['username']} not allowed :(")
            #user_writer.writerow([chat_dict["id"], chat_dict["username"], "No User Crawl allowed"])

        # crawl channel messages
        try:
            print(f"Crawl Messages in {chat_dict['username']} is allowed. NOM NOM NOM")
            async for message in client.iter_messages(chat):
                message_dict = await get_message_info(chat_dict["id"], chat_dict["username"], message)
                debughere()
                #message_writer.writerow(message_dict.values())
        except:
            print(f"Crawl Messages in {chat_dict['username']} not allowed :(")
            message_writer.writerow([chat_dict["id"], chat_dict["username"], "No Message Crawl allowed"])


    


 
   

with client:
    client.loop.run_until_complete(main())


csv_channel_f.close()
csv_message_f.close()
csv_user_f.close()
