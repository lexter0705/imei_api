from pydantic import BaseModel


class ApiKeyMessage(BaseModel):
    api_key: str