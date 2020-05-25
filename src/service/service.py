import string
from utils.constants import DATA_JSON
from utils.functions import random_string
import random
from flask import make_response, request
from file_storage.manager import FileManager
from components.new_player import NewPlayer


class Service:
    def __init__(self, container_manager, file_manager: FileManager, lobby):
        self.__container_manager = container_manager
        self.__file_manager = file_manager
        self.__lobby = lobby

    def get_lobby_data(self, group_code):
        return self.__lobby.get_group_by_code(group_code)

    def new_lobby(self, first_player: NewPlayer):
        group_code = self.__lobby.new_group(first_player)
        return group_code

    def join_lobby(self, group_code, new_player: NewPlayer):
        self.__lobby.add_player_to_group(group_code, new_player)
        return group_code

    def start_game(self, group_code):
        group_data = {group_code: self.__lobby.pop_group_by_code(group_code)}
        file_path = self.__file_manager.make_container_folder(group_code)
        self.__file_manager.dict_to_file(group_data, file_path + DATA_JSON)
        self.__container_manager.start_game(group_code)
        return group_code
