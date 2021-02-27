from sqlalchemy.orm import Session
from app import schemas, models
import uuid


# -----------------------------------------------------------------------------
# GET IDENTITY
# -----------------------------------------------------------------------------
def get_identity_by_id(db: Session, identity_id: uuid.UUID):
    return db.query(models.IsxIdentity)\
        .filter(models.IsxIdentity.identity_id == str(identity_id))\
        .first()


# -----------------------------------------------------------------------------
# GET IDENTITIES
# -----------------------------------------------------------------------------
def get_identities(db: Session, skip: int = 0, limit: int = 100, **kwargs):
    query = db.query(models.IsxIdentity)
    if "is_enabled" in kwargs and kwargs.get("is_enabled") is not None:
        enabled = True
        if kwargs.get('is_enabled').lower() == 'true':
            enabled = True
        query = query.filter(
            models.IsxIdentity.is_enabled == enabled
        )
    return query.offset(skip).limit(limit).all


# -----------------------------------------------------------------------------
# CREATE IDENTITY
# -----------------------------------------------------------------------------
def create_identity(db: Session, role: schemas.Identity):
    db_identity = models.IsxIdentity(**role.dict())
    db_identity.identity_id = uuid.uuid4()
    db.add(db_identity)
    db.commit()
    db.refresh(db_identity)
    return db_identity


# -----------------------------------------------------------------------------
# UPDATE IDENTITY
# -----------------------------------------------------------------------------
def update_identity(identity_id: str, db: Session, role: schemas.Identity):
    role_dict: dict = role.dict()
    role = db.query(models.IsxIdentity)\
        .filter(models.IsxIdentity.identity_id == uuid.uuid4(identity_id))\
        .first()
    if role:
        for key in role_dict.keys():
            if role_dict.get(key):
                setattr(role, key, role_dict.get(key))
        db.commit()
        db.refresh(role)
    return role


# -----------------------------------------------------------------------------
# SOFT DELETE IDENTITY
# -----------------------------------------------------------------------------
def soft_delete_identity(identity_id: str, db: Session, role: schemas.Identity):
    role = db.query(models.IsxIdentity)\
        .filter(models.IsxIdentity.identity_id == uuid.uuid4(identity_id))\
        .first()
    if role:
        setattr(role, "is_soft_deleted", True)
        db.commit()
        db.refresh(role)
    return role
