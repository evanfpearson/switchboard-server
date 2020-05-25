import json
import os
from utils.constants import CONTAINER_DATA_PATH


class FileManager:
    def __init__(self):
        pass

    @staticmethod
    def dict_to_file(dictionary, file_path):
        with open(file_path, "w") as f:
            json.dump(dictionary, f)

    @staticmethod
    def make_container_folder(group_code):
        path = CONTAINER_DATA_PATH + group_code + "/"
        os.mkdir(path)
        return path
