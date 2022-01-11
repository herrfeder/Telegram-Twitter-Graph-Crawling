import tweepy as tweepy
import csv
import time
import os
from IPython.core.debugger import Tracer

debughere = Tracer()


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
news_dict.append("https://twitter.com/nikitheblogger/status/1459922154829631491") # corona impufng
news_dict.append("https://twitter.com/reitschuster/status/1460208086250135553") # corona impfung
news_dict.append("https://twitter.com/BjoernHoecke/status/1458124712324878343") # belarus
news_dict.append("https://twitter.com/Georg_Pazderski/status/1459122771414368264") # belarus flüchtlinge
news_dict.append("https://twitter.com/HGMaassen/status/1459485773107974146") # corona impfung
news_dict.append("https://twitter.com/USMortality/status/1460327221508329480") # corona impfung
news_dict.append("https://twitter.com/Kukicat7/status/1460268217276977164") # corona impufng
news_dict.append("https://twitter.com/M_Ziesmann/status/1459544004425564166") # corona impfung
news_dict.append("https://twitter.com/shlomosapiens/status/1460273103926292485") # corona impfung
news_dict.append("https://twitter.com/WinDieselPower/status/1459183795278647308") # corona impufng
news_dict.append("https://twitter.com/Burpeelover/status/1459963868114006021") # belarus
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


csv_f = open('data/fake_news_tweet_id_retweets_01.csv', 'w', encoding='UTF8')
writer = csv.writer(csv_f)


# Twitter API allows only to get 100 latest retweets
for main_tweet in news_dict:
    main_user = main_tweet.split("/")[3]
    tweet_id =  main_tweet.split("/")[5]
    print(f"Collect Retweets for {main_user} with tweet {tweet_id}")
    for retweet_ids in api.get_retweets(tweet_id, count=100):
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

        row = [ retweet_date, retweeter_user, retweeter_id, 
                retweeter_pic, retweeter_follower, retweeter_subscr, 
                retweeter_tweeted_num, retweeter_account_created, main_user, 
                tweet_id, tweet_account_pic, tweet_account_user_handle, tweet_text]

        writer.writerow(row)
    
    time.sleep(600)

csv_f.close()



# spannende quellen
# https://www.tagesspiegel.de/gesellschaft/medien/twitter-datenanalyse-groesster-afd-twitter-account-ist-ein-scheinriese/19691492.html
# --> https://twitter.com/balleryna
# https://netzpolitik.org/2019/faelschen-zuechten-und-verstaerken-fragwuerdige-twitter-tricks-bei-der-afd/


# fake news accounts
# https://twitter.com/Kukicat7
# https://twitter.com/USMortality