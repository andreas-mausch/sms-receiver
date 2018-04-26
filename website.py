from flask import Flask, render_template
from pymongo import MongoClient, DESCENDING

app = Flask(__name__)

mongo = MongoClient('mongodb+srv://sms:9La3WJ0UICiIY2pQ@cluster0-0hvw0.mongodb.net/sms')
database = mongo.get_default_database()
messages = database.messages

@app.route("/")
def showMessages():
    lastMessages = messages.find().limit(50).sort('timestamp', DESCENDING)

    return render_template('messages.html', lastMessages=lastMessages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
