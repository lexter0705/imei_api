import os

from database.creator import create_database
from json_checker import read_config

config = read_config()
if not os.path.exists(config["database_path"]):
    create_database(config["database_path"])

from server.router import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
