from typing import Optional

from pydantic import BaseModel

class BaseBreed(BaseModel):
    name: str

class BaseBreedOut(BaseBreed):
    class Config:
        orm_mode = True

class BaseCatShort(BaseModel):
    cat_name: str
    age: int

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
