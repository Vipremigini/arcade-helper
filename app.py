from flask import Flask, request
import threading
import requests


app = Flask(__name__)

@app.post("/api/try")
def trial():
    murl = "https://arcade-helper.onrender.com/api/send"
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


@app.post("/api/send")
def reply():
    rurl = request.form.get("rurl")
    response = requests.post(url, headers=headers, json=data)
    rdata = response.json()
    rtext = rdata['choices'][0]['message']['content']
    send = {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": rtext
      }
    }]}
    requests.post(rurl, json=send)
