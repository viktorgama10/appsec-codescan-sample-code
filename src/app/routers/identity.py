from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.dependencies import get_db
from app.crud import application_data_operations as applications
import uuid
router = APIRouter()
