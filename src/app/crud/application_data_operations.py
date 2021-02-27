from sqlalchemy.orm import Session
from app import schemas, models
import uuid


def get_application_by_id(db: Session, application_id: uuid.UUID):
    return db.query(models.IsxApplication)\
        .filter(models.IsxApplication.application_id == str(application_id))\
        .first()


# ---------------------------------------------------------------------------------------
# GET APPLICATIONS
# ---------------------------------------------------------------------------------------
def get_applications(db: Session, skip: int = 0, limit: int = 100, **kwargs):
    query = db.query(models.IsxApplication)
    if 'is_enabled' in kwargs and kwargs.get('is_enabled') is not None:
        enabled = False
        if kwargs.get('is_enabled').lower() == 'true':
            enabled = True
        query = query.filter(
            models.IsxApplication.is_enabled == enabled
        )
    return query.offset(skip).limit(limit).all()


# -----------------------------------------------------------------------------
# CREATE APPLICATION
# -----------------------------------------------------------------------------
def create_application(db: Session, role: schemas.Application):
    db_application = models.IsxApplication(**role.dict())
    db_application.application_id = uuid.uuid4()
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


# -----------------------------------------------------------------------------
# UPDATE APPLICATION
# -----------------------------------------------------------------------------
def update_application(application_id: str, db: Session, role: schemas.Application):
    role_dict: dict = role.dict()
    role = db.query(models.IsxApplication)\
        .filter(models.IsxApplication.id == uuid.uuid4(application_id))\
        .first()
    if role:
        for key in role_dict.keys():
            if role_dict.get(key):
                setattr(role, key, role_dict.get(key))
        db.commit()
        db.refresh(role)
    return role


# -----------------------------------------------------------------------------
# SOFT DELETE APPLICATION
# -----------------------------------------------------------------------------
def soft_delete_application(application_id: str, db: Session, role: schemas.Application):
    role = db.query(models.IsxApplication).filter(models.IsxApplication.id == uuid.uuid4(application_id)).first()
    if role:
        setattr(role, "is_soft_deleted", True)
        db.commit()
        db.refresh(role)
    return role
