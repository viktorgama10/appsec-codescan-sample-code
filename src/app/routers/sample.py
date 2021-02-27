from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

# ---------------------------------------------------------------------------------------
# GET SAMPLE
# ---------------------------------------------------------------------------------------
@router.get("/sample", tags=["v1"])
async def get_sample():
    return {"msg": "hello"}

