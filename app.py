from flask import Flask, request
import threading
import requests


app = Flask(__name__)

@app.post("/api/try")
def trial():
    murl = "https://ah-helper.onrender.com/api/send"
    sendurl = request.form.get("response_url")
    send = { "rurl" : sendurl }
    thread = threading.Thread(target= requests.post(murl, json=send))
    thread.start()
    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": sendurl
      }
    }]}

