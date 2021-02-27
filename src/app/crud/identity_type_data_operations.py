from sqlalchemy.orm import Session
from app import schemas, models
import uuid


# -----------------------------------------------------------------------------
# GET IDENTITY TYPE
# -----------------------------------------------------------------------------
def get_identity_type_by_id(db: Session, identity_type_id: str):
    return db.query(models.IsxIdentityType)\
        .filter(models.IsxIdentityType.type_name == identity_type_id)\
        .first()