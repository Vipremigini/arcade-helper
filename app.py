from flask import Flask, request

app = Flask(__name__)

@app.post("/api/try")
def trial():
  name = request.form.get("user_id")
  req = "Hi, " + name
  return{"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": req
      }
    }]}, 200

