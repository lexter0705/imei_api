from pydantic import BaseModel


class ImeiMessage(BaseModel):
    api_key: str
    imei: str