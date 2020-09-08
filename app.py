#!/usr/bin/python
import json
import bot
from flask import Flask, request, make_response, render_template

pyBot = bot.Bot()
slack = pyBot.client

app = Flask(__name__)


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content-type":
                                                             "application/json"})
    if pyBot.verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s \npyBot has: \
                   %s\n\n" % (slack_event["token"], pyBot.verification)
        make_response(message, 403, {'X-Slack-No-Retry': 1})

    if "event" in slack_event:
        event_type = slack_event['event']['type']
        print(slack_event)


    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you are looking for.", 404, {"X-Slack-No-Retry": 1})

if __name__ == "__main__":
    app.run(debug=True)

