from typing import Optional

from pydantic import BaseModel

class BaseBreed(BaseModel):
    breed_name: str


class BaseCatShort(BaseModel):
    cat_name: str
    age: str

class BaseCatLong(BaseCatShort):
    color: str
    description: str
    breed_id: Optional[int]


class CatIn(BaseCatLong):
    ...


class CatOutShort(BaseCatShort):

    class Config:
        orm_mode = True

class CatOutLong(BaseCatLong):

    class Config:
        orm_mode = True
