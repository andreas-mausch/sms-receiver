#!/usr/bin/env python

import os
from pymongo import MongoClient
from datetime import datetime

def main():
    mongo = MongoClient('mongodb+srv://sms:9La3WJ0UICiIY2pQ@cluster0-0hvw0.mongodb.net/sms')
    database = mongo.get_default_database()
    messages = database.messages

    number = os.environ['SMS_1_NUMBER']
    text = os.environ['SMS_1_TEXT']
    
    messages.insert_one({
        'number': number,
        'text': text,
        'timestamp': datetime.now()
    })

if __name__ == "__main__":
    main()
