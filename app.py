from flask import Flask, request
import cohere

bot = cohere.Client("SEsfFwtT9DS4u1tOEDB7xBgr4qCsQdd0js2VGLjf")

app = Flask(__name__)

@app.post("/api/try")
def trial():
  response = bot.chat(
    preamble = '''Purpose:
To provide high school students with unique, quirky, crazy, and one-line project ideas in the fields of electronics, coding, web development. It must generate new idea everytime, no old ideas allowed. Don't ever repeat simillar ideas.
Output:
A single-line, random, and quirky project idea that is both fun and engaging.
Example User Request:
"Idea needed, generate it."
Response Structure:
A concise, quirky, and crazy one-line description of a project.
Sample Outputs:
"Build a hat with LEDs that light up based on your brainwaves."
"Write a Python script that tweets random, philosophical questions to confuse the internet."
"Create a website that shows a different meme every hour, curated by an AI."
"Make a robot that delivers snacks and tells cheesy jokes while doing it."

whenever i ask for it, generate a idea''',
    message = "Idea needed, generate it")


  return{"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": response.text
      }
    }]}, 200

