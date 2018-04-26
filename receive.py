#!/usr/bin/env python

import os
from pymongo import MongoClient
from datetime import datetime

def main():
    mongo = MongoClient('mongodb+srv://sms:9La3WJ0UICiIY2pQ@cluster0-0hvw0.mongodb.net/sms')
    database = client.get_default_database()
    messages = db.messages

    number = os.environ['SMS_1_NUMBER']
    text = os.environ['SMS_1_TEXT']

    with open('/home/pi/sms/sms', 'w') as outfile:
        outfile.write('Number: %s\n' % number)
        outfile.write('Text: %s\n' % text)
    
    messages.insert_one({
        number: number,
        text: text,
        timestamp: datetime.now()
    })

if __name__ == "__main__":
    main()
