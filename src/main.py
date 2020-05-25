from facade.facade import Facade
from lobby.lobby import Lobby
from containers.manager import ContainerManager
from file_storage.manager import FileManager
from service.service import Service
import docker


def main():
    lobby = Lobby()
    docker_client = docker.from_env()
    container_manager = ContainerManager(docker_client)
    file_manager = FileManager()
    service = Service(container_manager, file_manager, lobby)
    facade = Facade(service)
    facade.app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
