

class ContainerManager:
    def __init__(self, client):
        self.__client = client

    def start_game(self, group_code):
        self.__client.containers.run('switchboard')




