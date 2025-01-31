from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from server.keys_generator import generate_key
from server.messages.imei import ImeiMessage
from server.messages.create_api_key import CreateApiKeyMessage

from database.workers.keys import KeysWorker

from server.api_executor import ApiExecutor

from json_checker import read_config

router = APIRouter(prefix="/imei_api")

data = read_config()

keys_worker = KeysWorker(data["database_path"])
api_executor = ApiExecutor(data["api_key"], data["api_link"])


@router.post("/check_imei")
async def check_imei(message: ImeiMessage):
    if not keys_worker.is_key_available(message.api_key):
        raise HTTPException(403, "Invalid API key")
    phone_data = await api_executor.check_imei(message.imei)
    if len(phone_data) == 0:
        raise HTTPException(404, "Uncorrected IMEI")
    return JSONResponse(phone_data[0], status_code=200)

@router.post("/create_api_key")
def create_new_api_key(message: CreateApiKeyMessage):
    if not keys_worker.is_admin(message.api_key):
        raise HTTPException(403, "Not enough rights")
    new_key = generate_key(keys_worker.count_rows)
    keys_worker.add_new_api_key(new_key)
    return JSONResponse({"new_key": new_key}, status_code=200)
