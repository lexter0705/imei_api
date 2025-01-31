from pydantic import BaseModel


class CreateApiKeyMessage(BaseModel):
    api_key: str