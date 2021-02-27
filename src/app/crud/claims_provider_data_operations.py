from sqlalchemy.orm import Session
from app import schemas, models
import uuid


# -----------------------------------------------------------------------------
# GET CLAIM PROVIDER
# -----------------------------------------------------------------------------
def get_claim_provider_by_id(db: Session, provider_id: uuid.uuid4()):
    return db.query(models.IsxClaimProvider)\
        .filter(models.IsxClaimProvider.provider_id == str(provider_id))\
        .first()


# -----------------------------------------------------------------------------
# GET CLAIM PROVIDERS
# -----------------------------------------------------------------------------
def get_claim_providers(db: Session, skip: int = 0, limit: int = 100, **kwargs):
    query = db.query(models.IsxClaimProvider)
    return query.offset(skip).limit(limit).all


# -----------------------------------------------------------------------------
# CREATE CLAIM PROVIDER
# -----------------------------------------------------------------------------
def create_claim_provider(db: Session, role: schemas.ClaimProvider):
    db_claim_provider = models.IsxClaimProvider(**role.dict())
    db_claim_provider.provider_id = uuid.uuid4()
    db.add(db_claim_provider)
    db.commit()
    db.refresh(db_claim_provider)
    return db_claim_provider


# -----------------------------------------------------------------------------
# UPDATE CLAIM PROVIDER
# -----------------------------------------------------------------------------
def update_claim_provider(provider_id: str, db: Session, role: schemas.ClaimProvider):
    role_dict: dict = role.dict()
    role = db.query(models.IsxClaimProvider)\
        .filter(models.IsxClaimProvider.provider_id == uuid.uuid4(provider_id))\
        .first()
    if role:
        for key in role_dict.keys():
            if role_dict.get(key):
                setattr(role, key, role_dict.get(key))
        db.commit()
        db.refresh(role)
    return role


# -----------------------------------------------------------------------------
# SOFT DELETE CLAIM PROVIDER
# -----------------------------------------------------------------------------
def soft_delete_claim_provider(provider_id: str, db: Session, role: schemas.ClaimProvider):
    pass
