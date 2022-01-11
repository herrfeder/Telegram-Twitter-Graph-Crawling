import tweepy as tweepy
import csv
import time
import os
from IPython.core.debugger import Tracer
debughere = Tracer()


def extract_tweet(tweet):
    tweet_dict = {}
    tweet_dict["created_at"] = tweet.created_at
    tweet_dict["id"] = str(tweet.id)
    tweet_dict["text"] = tweet.full_text.replace("\n", " ")
    tweet_dict["tweeter_url_handle"] = tweet.user.screen_name
    tweet_dict["tweeter_id"] = str(tweet.user.id)
    tweet_dict["tweeter_name"] = tweet.user.name
    tweet_dict["profile_image"] = tweet.user.profile_image_url
    tweet_dict["favorites_count"] = tweet.favorite_count
    tweet_dict["retweet_count"] = tweet.retweet_count
    tweet_dict["replied_user_handle"] = tweet.in_reply_to_screen_name
    tweet_dict["replied_user_id"] = str(tweet.in_reply_to_user_id)
    tweet_dict["hashtags"] = tweet.entities["hashtags"]
    tweet_dict["user_mention"] = tweet.entities["user_mentions"]
    tweet_dict["url"] = tweet.entities["urls"]

    t = tweet_dict
        
    tweet_row = [ t["created_at"], t["id"], t["text"],
                t["tweeter_url_handle"], t["tweeter_id"], t["tweeter_name"], t["profile_image"],
                t["favorites_count"], t["retweet_count"], t["replied_user_handle"],
                t["replied_user_id"], t["hashtags"], t["user_mention"], t["url"]]

    return tweet_row

def extract_retweets(tweet_id, retweet_ids):
    retweet_date = retweet_ids.created_at # when retweet happend
    retweeter_user = retweet_ids.user.screen_name # twitter user handle of retweeter
    retweeter_id = retweet_ids.user.id_str # user id of retweeter
    retweeter_pic =  retweet_ids.user.profile_image_url # profile pic of retweeter
    retweeter_follower = retweet_ids.user.followers_count # followers that follow this account
    retweeter_subscr = retweet_ids.user.friends_count # accounts that follows this user
    retweeter_tweeted_num = retweet_ids.user.statuses_count # created tweets
    retweeter_account_created = retweet_ids.user.created_at # when was user account created
    tweet_account_pic = retweet_ids.retweeted_status.author.profile_image_url # image url of original account
    tweet_account_user_handle = main_user
    tweet_text = retweet_ids.retweeted_status.text.replace("\n", " ") # Text of original tweet

    retweet_row = [ retweet_date, retweeter_user, retweeter_id, 
            retweeter_pic, retweeter_follower, retweeter_subscr, 
            retweeter_tweeted_num, retweeter_account_created, main_user, 
            tweet_id, tweet_account_pic, tweet_account_user_handle, tweet_text]

    return retweet_row





creds_dict = {
    "api_key":"",
    "api_secret":"",
    "bearer_token":"",
}

for key in creds_dict.keys():
    creds_dict[key] = os.environ.get(key)
    try:
        del os.environ[key]
    except:
        pass

auth = tweepy.AppAuthHandler(creds_dict["api_key"], creds_dict["api_secret"])
api = tweepy.API(auth)


news_dict = []
# between 15.Nov - 08.Nov
#news_dict.append("https://twitter.com/nikitheblogger/status/1459922154829631491") # corona impufng
#news_dict.append("https://twitter.com/reitschuster/status/1460208086250135553") # corona impfung
#news_dict.append("https://twitter.com/BjoernHoecke/status/1458124712324878343") # belarus
#news_dict.append("https://twitter.com/Georg_Pazderski/status/1459122771414368264") # belarus flüchtlinge
#news_dict.append("https://twitter.com/HGMaassen/status/1459485773107974146") # corona impfung
#news_dict.append("https://twitter.com/USMortality/status/1460327221508329480") # corona impfung
#news_dict.append("https://twitter.com/Kukicat7/status/1460268217276977164") # corona impufng
#news_dict.append("https://twitter.com/M_Ziesmann/status/1459544004425564166") # corona impfung
#news_dict.append("https://twitter.com/shlomosapiens/status/1460273103926292485") # corona impfung
#news_dict.append("https://twitter.com/WinDieselPower/status/1459183795278647308") # corona impufng
#news_dict.append("https://twitter.com/Burpeelover/status/1459963868114006021") # belarus
news_dict.append("https://twitter.com/DerLuegenbaron/status/1460331680246517775") #belarus
news_dict.append("https://twitter.com/Hartes_Geld/status/1459618439362981899") # belarus flüchtlinge
news_dict.append("https://twitter.com/Alice_Weidel/status/1460596090026307595") # corona impfung
news_dict.append("https://twitter.com/wolff_ernst/status/1460209063703334914") # corona impfung
news_dict.append("https://twitter.com/RalfH49079853/status/1458422660040384520") # flüchtline
news_dict.append("https://twitter.com/Dieter_Stein/status/1458365157684432897") # belarus politik
news_dict.append("https://twitter.com/ainyrockstar/status/1458459240704643087") # belarus flüchtlinge
news_dict.append("https://twitter.com/JackPosobiec/status/1460012265038651399") # belarus
news_dict.append("https://twitter.com/Zorro22222221/status/1458071418256699403") # belarus
news_dict.append("https://twitter.com/Iwonka05826541/status/1460105433880924161") # corona impfung
news_dict.append("https://twitter.com/schmettee/status/1459961490530832391") # corona impfung
news_dict.append("https://twitter.com/argonerd/status/1462777818576785418") # corona impfung
news_dict.append("https://twitter.com/SHomburg/status/1462848385183068161") # corona impfung
news_dict.append("https://twitter.com/VonDorset/status/1460967090031108101") # belarus
news_dict.append("https://twitter.com/TheRepublicDe/status/1461025568892276741") # belarus flüchtlinge
news_dict.append("https://twitter.com/realTomBohn/status/1462752797582049283") # corona

news_dict.append("https://twitter.com/isabelschayani/status/1459998020238520329") # belarus
news_dict.append("https://twitter.com/georgrestle/status/1460269640496652289") # belarus
news_dict.append("https://twitter.com/ABaerbock/status/1459868827211210755") # belarus
news_dict.append("https://twitter.com/J_Pahlke/status/1458779441732235266") # belarus
news_dict.append("https://twitter.com/ennopark/status/1459515657335283729") # belarus
news_dict.append("https://twitter.com/OliviaKortas/status/1460246064536207361") # belarus
news_dict.append("https://twitter.com/c_lindner/status/1461630862848573443") # corona pandemie
news_dict.append("https://twitter.com/janboehm/status/1461664900955181069") # afd
news_dict.append("https://twitter.com/Karl_Lauterbach/status/1462199291619987461") # corona impfung
news_dict.append("https://twitter.com/GoeringEckardt/status/1461612976738390021") # corona
news_dict.append("https://twitter.com/c_drosten/status/1461096295800709125") # corona
news_dict.append("https://twitter.com/Markus_Soeder/status/1462765776356712453") # corona impfung
news_dict.append("https://twitter.com/Luisamneubauer/status/1462849793508749313") # corona
news_dict.append("https://twitter.com/KuehniKev/status/1462397370877071361") # extrem
news_dict.append("https://twitter.com/Kachelmann/status/1462758962537930762") # extrem
news_dict.append("https://twitter.com/polenz_r/status/1462930591607926793") # corona
news_dict.append("https://twitter.com/polinaivanovva/status/1460893659440766982") # belarus
news_dict.append("https://twitter.com/_Seebruecke_/status/1461432828722393093") # belarus
news_dict.append("https://twitter.com/Unteilbar_/status/1460605557249908737") # belarus flüchtlinge
news_dict.append("https://twitter.com/BMISprecher/status/1461352489207304196") # belarus
news_dict.append("https://twitter.com/kattascha/status/1462545289911275534") # corona
news_dict.append("https://twitter.com/kattascha/status/1462545289911275534") # corona
news_dict.append("https://twitter.com/EberhardSchlie/status/1462704022943674370") # corona
news_dict.append("https://twitter.com/FlorianPost/status/1462692770347470850") # corona
news_dict.append("https://twitter.com/KathaSchulze/status/1462680077871763462") # corona



csv_tweet_f = open('data/fake_news_tweet_id_tweets_01.csv', 'a', encoding='UTF8')
tweet_writer = csv.writer(csv_tweet_f)

csv_retweet_f = open('data/fake_news_tweet_id_retweets_01.csv', 'a', encoding='UTF8')
retweet_writer = csv.writer(csv_retweet_f)

for main_tweet in news_dict:
    main_user = main_tweet.split("/")[3]

    print(f"Crawl tweets for {main_user}")

    try:
        tweets = api.user_timeline(screen_name=main_user, 
                            # 200 is the maximum allowed count
                            count=10,
                            include_rts = True,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
    except:
        print("We need to sleep, we stressed Twitter API to much")
        time.sleep(905)
        tweets = api.user_timeline(screen_name=main_user, 
                            # 200 is the maximum allowed count
                            count=10,
                            include_rts = True,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )

    if len(tweets) == 0:
        break

    for tweet in tweets:
        tweet_row = extract_tweet(tweet)
        tweet_writer.writerow(tweet_row)

        tweet_id = tweet_row[1]
        print(f"Collect Retweets for {main_user} with tweet {tweet_id}")
        for retweet_ids in api.get_retweets(tweet_id, count=20):

            retweet_row = extract_retweets(tweet_id, retweet_ids)
            retweet_writer.writerow(retweet_row)

            retweet_user = retweet_row[1]

            print(f"Crawl tweets for Retweeter {retweet_user}")
            try:
                retweet_tweets = api.user_timeline(screen_name=retweet_user, 
                                    # 200 is the maximum allowed count
                                    count=10,
                                    include_rts = True,
                                    # Necessary to keep full_text 
                                    # otherwise only the first 140 words are extracted
                                    tweet_mode = 'extended'
                                    )
            except:
                print("We need to sleep, we stressed Twitter API to much")
                time.sleep(905)
                retweet_tweets = api.user_timeline(screen_name=retweeter_user, 
                                    # 200 is the maximum allowed count
                                    count=10,
                                    include_rts = True,
                                    # Necessary to keep full_text 
                                    # otherwise only the first 140 words are extracted
                                    tweet_mode = 'extended'
                                    )

            if len(retweet_tweets) == 0:
                break

            for tweet in retweet_tweets:
                tweet_row = extract_tweet(tweet)

                tweet_writer.writerow(tweet_row)



        time.sleep(30)

csv_tweet_f.close()
csv_retweet_f.close()