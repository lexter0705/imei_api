from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column
from server.keys_generator import generate_key


class Base(DeclarativeBase):
    pass


class KeysTable(Base):
    __tablename__ = 'keys_table'
    key: Mapped[str] = mapped_column(primary_key=True)
    is_admin: Mapped[bool] = mapped_column(default=False)


def create_database(path: str):
    engine = create_engine("sqlite:///" + path)
    Base.metadata.create_all(engine)
    connect = engine.connect()

    # для вашего удобства создаю ключ с админ правами
    key = generate_key(0)
    connect.execute(insert(KeysTable).values(key=key, is_admin=True))
    connect.commit()
    print(f"key was created!!\n{key}")
    connect.close()
