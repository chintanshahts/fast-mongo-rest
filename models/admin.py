from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class Admin(Document):
    fullname: str
    email: EmailStr
    password: str

    class Collection:
        name = "admin"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John doe",
                "email": "john.doe@yopmail.com",
                "password": "123123@aA",
            }
        }


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {"username": "john.doe@yopmail.com", "password": "123123@aA"}
        }


class AdminData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "john.doe@yopmail.com",
            }
        }
