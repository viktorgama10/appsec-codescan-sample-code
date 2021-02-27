from typing import List, Dict
import uuid
from datetime import datetime
from pydantic import Schema, BaseModel, Field


# -----------------------------------------------------------------------------
# APPLICATION MODEL
# -----------------------------------------------------------------------------
class Application(BaseModel):

    application_id: uuid.UUID = Field(None, title="Unique identifier for a given application")
    name: str = Field(None, title="Application name", max_length=40)
    description: str = Field(None, title="Application description", max_length=256)
    callback_url: str = Field(None, title="Callback URL where access token is returned after authorization", max_length=4000)
    public_key: str = Field(None, title="Public Cryptographic Key used to validate JWT Signatures", max_length=4096)
    private_key: str = Field(None, title="Private Cryptographic Key used to validate JWT Signatures", max_length=4096)
    environment: str = Field(
        None, title="Tag that describes the application's environment (Ex: Dev, Test, Prod)", max_length=50
    )
    configuration: dict = Field(None, title="Additional configurations for the application")
    last_modified: datetime = Field(
        None, title="Time stamp of the last modification made to the application definition"
    )
    is_enabled: bool = Field(
        None, title='If the application is enabled of not to authorize users'
    )


# -----------------------------------------------------------------------------
# CLAIM PROVIDER MODEL
# -----------------------------------------------------------------------------
class ClaimsProviders(BaseModel):

    provider_id: uuid.UUID = Field(None, title="Unique identifier to a provider id")
    name: str = Field(None, title="Claim Provider name", max_length=40)
    description: str = Field(None, title="Claim Provider description", max_length=256)
    is_local: bool = Field(None, title="If Claim Provider is local or not")
    config: dict = Field(None, title="Additional configuration for the Claim Provider")
    implementation_class: str = Field(None, title="Implementation Class", max_length=200)
    credentials: dict = Field(None, title="Credentials for the Claim Provider")


# -----------------------------------------------------------------------------
# IDENTITY TYPE MODEL
# -----------------------------------------------------------------------------
class IdentityType(BaseModel):

    type_name: str = Field(None, title="Name for an Identity Type", max_length=40)
    description: str = Field(None, title="Description for an Identity Type", max_length=256)


# -----------------------------------------------------------------------------
# APPLICATION PROVIDER MODEL
# -----------------------------------------------------------------------------
class ApplicationProvider(BaseModel):

    provider_id: uuid.UUID = Field(None, title="Unique identifier to a provider id")
    application_id: uuid.UUID = Field(None, title="Unique identifier for a given application")


# -----------------------------------------------------------------------------
# CLAIM MODEL
# -----------------------------------------------------------------------------
class Claim(BaseModel):

    claim_id: uuid.UUID = Field(None, title="Unique identifier for a claim")
    application_id: uuid.UUID = Field(None, title="Unique identifier for an application id")
    value: str = Field(None, title="Value for a claim", max_length=512)
    description: str = Field(None, title="Claim Description", max_length=256)


# -----------------------------------------------------------------------------
# GROUP MODEL
# -----------------------------------------------------------------------------
class Group(BaseModel):

    group_id: uuid.UUID = Field(None, title="Unique identifier for a group id")
    application_id: uuid.UUID = Field(None, title="Unique identifier for an application id")
    name: str = Field(None, title="Group name", max_length=40)
    description: str = Field(None, title="Group description", max_length=256)
    properties: dict = Field(None, title="Additional properties for a group")


# -----------------------------------------------------------------------------
# IDENTITY MODEL
# -----------------------------------------------------------------------------
class Identity(BaseModel):

    identity_id: uuid.UUID = Field(None, title="Unique identifier for an Identity")
    business_id: str = Field(None, title="Business Id", max_length=40)
    identity_data: dict = Field(None, title="Additional information for an Identity")
    created: datetime = Field(None, title="Timestamp when the Identity was created")
    last_modified: datetime = Field(None, title="Timestamp for the last time made to the Identity definition")
    disabled: bool = Field(None, title="If Identity is enabled or not")
    type: str = Field(None, title="", max_length=40)


# -----------------------------------------------------------------------------
# IDENTITY MODEL
# -----------------------------------------------------------------------------
class ApplicationIdentity(BaseModel):

    identity_id: uuid.UUID = Field(None, title="Unique identifier for an Identity")
    application_id: uuid.UUID = Field(None, title="Unique identifier for an Application")
    created: datetime = Field(None, title="Timestamp when the Application Identity was created")


# -----------------------------------------------------------------------------
# APPLICATION OWNERSHIP MODEL
# -----------------------------------------------------------------------------
class ApplicationOwnership(BaseModel):

    identity_id: uuid.UUID = Field(None, title="Unique identifier for an Identity")
    application_id: uuid.UUID = Field(None, title="Unique identifier for an Application")
    created: datetime = Field(None, title="Timestamp when the Application Ownership was created")
    from_date: datetime = Field(None, title="Timestamp for when Application Ownership validity starts")
    until_date: datetime = Field(None, title="Timestamp for when Application Ownership validity ends")
    is_owner: bool = Field(None, title="If the user is owner")
    is_manager: bool = Field(None, title="If the user is manager")
    configuration: dict = Field(None, title="Additional configuration for Application Ownership")


# -----------------------------------------------------------------------------
# GROUP CLAIM MODEL
# -----------------------------------------------------------------------------
class GroupClaim(BaseModel):

    group_id: uuid.UUID = Field(None, title="Unique identifier for Group")
    claim_id: uuid.UUID = Field(None, title="Unique identifier for a claim")
    application_id: uuid.UUID = Field(None, title="Unique identifier for a claim")


# -----------------------------------------------------------------------------
# IDENTITY CLAIM MODEL
# -----------------------------------------------------------------------------
class IdentityClaim(BaseModel):

    claim_id: uuid.UUID = Field(None, title="Unique identifier for a claim")
    application_id: uuid.UUID = Field(None, title="Unique identifier for an application")
    identity_id: uuid.UUID = Field(None, title="Unique identifier for an identity")
    from_date: datetime = Field(None, title="Timestamp for when Identity Claim validity starts")
    until_date: datetime = Field(None, title="Timestamp for when Identity Claim validity ends")


# -----------------------------------------------------------------------------
# IDENTITY GROUP MODEL
# -----------------------------------------------------------------------------
class IdentityGroup(BaseModel):

    group_id: uuid.UUID = Field(None, title="Unique identifier for Group")
    application_id: uuid.UUID = Field(None, title="Unique identifier for an applications")
    identity_id: uuid.UUID = Field(None, title="Unique identifier for an identity")


# -----------------------------------------------------------------------------
# PROFILE MODEL
# -----------------------------------------------------------------------------
class Profile(BaseModel):

    identity_id: uuid.UUID = Field(None, title="Unique identifier for an identity")
    application_id: uuid.UUID = Field(None, title="Unique identifier for an application")
    profile_data: dict = Field(None, title="Additional information for a profile")
