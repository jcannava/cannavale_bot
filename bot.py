#!/usr/bin/python

import os
import message
from slackclient import SlackClient

class Bot(object):
    def __init__(self):
        super(Bot, self).__init__()
        self.id = ""
        self.name = "cannavale_bot"
        self.emoji = ":robot_face:"
        self.oauth = {"client_id": os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")
        self.client = SlackClient("")
        self.messages = {}

    def auth(self, code):
        auth_response = self.client.api_call(
                "oauth.access",
                client_id=self.oauth["client_id"],
                client_secret=self.oath['client_secret'],
                code=code)

        self.id = auth_response['user_id']
        print(self.id)
        team_id = auth_response['team_id']
        authed_team[team_id] = {"bot_token":
                                auth_response["bot"]["bot_access_token"]}
        self.client = SlackClient(authed_teams[team_id]["bot_token"])
