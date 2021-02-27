from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.dependencies import get_db
from app.crud import application_data_operations as applications
import uuid
router = APIRouter()

# ---------------------------------------------------------------------------------------
# GET IDENTITY
# ---------------------------------------------------------------------------------------
@router.get("/application", tags=["v1"], response_model=List[schemas.Application])
async def list_application_definitions(is_enabled: str = None, skip: int = 0, limit: int = 100,
                                       db: Session = Depends(get_db)):
    return applications.get_applications(db, skip, limit, is_enabled=is_enabled)


# ---------------------------------------------------------------------------------------
# GET SINGLE APPLICATION
# ---------------------------------------------------------------------------------------
@router.get("/application/{application_id}", tags=["v1"], response_model=schemas.Application)
async def list_application_definitions(application_id: str, db: Session = Depends(get_db)):
    return applications.get_application_by_id(db, uuid.UUID(application_id))

