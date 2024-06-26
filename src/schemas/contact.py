from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import date

class ContactSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone_number: str
    birthday: date
    additional_data: Optional[bool] = False

class ContactUpdateSchema(ContactSchema):
    additional_data: bool

class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_data: bool

    class Config:
        orm_mode = True