from flask import Flask

app = Flask(__name__)

@app.post("/api/try")
def trial():
  data = request.get_json()
  name = data["user_id"]
  req = "Hi, " + name
  return{"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": req
      }
    }]}, 200

