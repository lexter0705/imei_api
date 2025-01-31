from sqlalchemy import create_engine, Executable
from sqlalchemy.engine.base import Connection


class DatabaseWorker:
    def __init__(self, database_path: str):
        database_url = "sqlite:///" + database_path
        engine = create_engine(database_url)
        self.__connect = engine.connect()

    def commit(self, request: Executable):
        self.__connect.execute(request)
        self.__connect.commit()

    @property
    def connect(self) -> Connection:
        return self.__connect