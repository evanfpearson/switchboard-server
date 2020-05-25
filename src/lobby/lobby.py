import time
from utils.functions import random_string


class Lobby:
    def __init__(self):
        self.__groups_by_code = dict()

    def get_group_by_code(self, group_code):
        return self.__groups_by_code[group_code]

    def add_player_to_group(self, group_code, new_player):
        self.get_group_by_code(group_code)["players"].append(new_player.marshal())

    def new_group(self, new_player):
        group_code = random_string()
        self.__groups_by_code[group_code] = {"players": [new_player.marshal()], "started": False, "opened": time.time()}
        return group_code

    def start_game(self, group_code):
        self.get_group_by_code(group_code)["started"] = True

    def pop_group_by_code(self, group_code):
        return self.__groups_by_code.pop(group_code)


