


from telethon.sync import TelegramClient
from telethon import functions, types

import configparser
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.contacts import ResolveUsernameRequest
import csv
from IPython.core.debugger import Tracer
import time
debughere = Tracer()
import pandas as pd


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

with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.messages.GetRepliesRequest(
        peer='username',
        msg_id=2385,
        offset_id=42,
        offset_date=datetime.datetime(2018, 6, 25),
        add_offset=0,
        limit=100,
        max_id=0,
        min_id=0,
        hash=0
    ))
    print(result.stringify())