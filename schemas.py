from datetime import datetime
from enum import Enum
from pydantic import BaseModel, field_validator


class GenderURLChoice(str, Enum):
    female = 'female'
    male = 'male'
    agender ='agender'
    
class GenderChoice(str, Enum):
    Female = 'Female'
    Male = 'Male'
    Agender ='Agender'

class JobTitle(BaseModel):
    title: str
    date_start : datetime

class PersonBase(BaseModel):
    fullname: str
    email: str
    gender: GenderChoice
    jobtitles: list[JobTitle] = []
    
class PersonCreate(PersonBase):
    @field_validator('gender', mode="before")
    def title_case_gender(cls, value):
        return value.title()

class PersonWithID(PersonBase):
    id: int    