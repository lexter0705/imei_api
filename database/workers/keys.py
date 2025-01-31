from sqlalchemy import select, insert, func

from database.creator import KeysTable
from database.worker import DatabaseWorker


class KeysWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(database_path)

    def is_key_available(self, key: str) -> bool:
        response = self.connect.execute(select(KeysTable).where(KeysTable.key == key)).all()
        return len(response) > 0

    def is_admin(self, key: str) -> bool:
        response = self.connect.execute(select(KeysTable.is_admin).where(KeysTable.key == key)).fetchone()
        if response is None:
            return False
        return response[0]

    def add_new_api_key(self, key: str):
        database_request = insert(KeysTable).values(key=key)
        self.commit(database_request)

    @property
    def count_rows(self) -> int:
        response = self.connect.execute(select(func.count()).select_from(KeysTable)).scalar()
        return response