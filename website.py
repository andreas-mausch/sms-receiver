from bson import json_util
from flask import Flask, render_template, Response
from pymongo import MongoClient, DESCENDING

app = Flask(__name__)

mongo = MongoClient('mongodb+srv://sms:9La3WJ0UICiIY2pQ@cluster0-0hvw0.mongodb.net/sms')
database = mongo.get_default_database()
messages = database.messages

def findLastMessages():
    return list(messages.find().limit(50).sort('timestamp', DESCENDING))

@app.route("/")
def showMessages():
    return render_template('messages.html', lastMessages=findLastMessages())

@app.route("/json")
def showMessagesJson():
    lastMessages = findLastMessages()
    for message in lastMessages:
        del message['_id']

    return Response(
        json_util.dumps(lastMessages,
            json_options=json_util.JSONOptions(
                datetime_representation=json_util.DatetimeRepresentation.ISO8601
            )
        ),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
