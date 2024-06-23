from flask import Flask, request
import threading
import requests


url = 'https://jamsapi.hackclub.dev/openai/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer A0SO2U3QRRBRAQWO0CBUFSJK00VHCQGBP30BL18U834PZ4FACE00W60VFJVD8EDW'
}
data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {
            'role': 'user',
            'content': 'You are a software engineer that wants to bring joy through chaos. Come up with something different every time. Please propose a funky simple project that will take under 6 hours to complete in 1 quick sentence. Keep it at less than 15 words. The funkier, stupidier, and sillier your ideas the better. Think out of the box, and do not propose ideas that do nothing but generate text, like a joke or dance move generator. Random sound effect generators are boring, do not suggest them. Be very creative, do not suggest projects that are too simple.'
        }
    ]
}

def reply(rurl):
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

app = Flask(__name__)

@app.post("/api/try")
def trial():
    thread = threading.Thread(target=reply(request.form.get("response_url")))
    thread.start()

    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Processing"
      }
    }]}

