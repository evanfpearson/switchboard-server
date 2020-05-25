from flask import Flask, make_response, request
import random
import string
from service.service import Service
import json
import os
from components.new_player import NewPlayer


class Facade:
    def __init__(self, service: Service):
        self.app = Flask(__name__)
        self.__service = service
        self.app.add_url_rule("/lobby", None, self.new_lobby, methods=["POST"])
        self.app.add_url_rule("/lobby/<group_code>", None, self.join_lobby, methods=["PUT"])
        self.app.add_url_rule("/lobby/<group_code>", None, self.get_lobby_data, methods=["GET"])
        self.app.add_url_rule("/game/<group_code>", None, self.start_game, methods=["POST"])
        #  self.app.add_url_rule("/game")

    def get_lobby_data(self, group_code):
        return self.__service.get_lobby_data(group_code)

    def new_lobby(self):
        request_body = request.get_json()
        first_player = NewPlayer.from_name(request_body["name"])
        group_code = self.__service.new_lobby(first_player)
        response = make_response({"code": group_code})
        response.set_cookie("player", first_player.get_cookie())
        return response

    def join_lobby(self, group_code):
        request_body = request.get_json()
        new_player = NewPlayer.from_name(request_body["name"])
        group_code = self.__service.join_lobby(group_code, new_player)
        response = make_response({"code": group_code})
        response.set_cookie("player", new_player.get_cookie())
        return response

    def start_game(self, group_code):
        response = self.__service.start_game(group_code)
        return response

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)
