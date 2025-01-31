from fastapi import APIRouter


router = APIRouter(prefix="/imei_api")


@router.post("/check_imei")
def check_imei(imei: str):
    pass