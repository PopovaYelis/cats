import time
from http.client import HTTPException

from fastapi import APIRouter, FastAPI

from schemas import BaseBreed, BaseCatShort, BaseCatLong, CatIn, CatOutLong, CatOutShort, BaseBreedOut
from typing import List
from database import engine, session
from models import Cats, Breed, Base
from sqlalchemy.future import select
router = APIRouter()


@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@router.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@router.get("/breed", response_model=List[BaseBreedOut])
async def get_breeds():
    async with session.begin():
        res = await session.execute(
            select(Breed))
    return res.scalars().all()

@router.post("/breed", response_model=BaseBreedOut)
async def post_breed(breed: BaseBreed):
    new_breed = Breed(**breed.dict())
    async with session.begin():
        session.add(new_breed)
    return new_breed


@router.get("/cats/{breed_name}", response_model=List[CatOutLong])
async def get_cat_bred(bread_name):
    async with session.begin():
        res = await session.execute(
            select(Cats).where(Cats.breed.name == bread_name))
    return res.scalars().all()

@router.get("/cats", response_model=List[CatOutShort])
async def get_cats():
    async with session.begin():
        res = await session.execute(
            select(Cats))
    return res.scalars().all()

@router.get("/cats/{cat_id}", response_model=CatOutLong)
async def get_cat_id(cat_id):
    async with session.begin():
        res = await session.execute(
            select(Cats).where(Cats.id == cat_id))
    return res.scalar()


@router.post("/cats", response_model=CatOutLong)
async def post_route(cat: CatIn):
    new_cat = Cats(**cat.dict())
    async with session.begin():
        session.add(new_cat)
    return new_cat


@router.patch("/cats/{cat_id}", response_model=CatOutLong)
async def update_cat(cat_id: int, cat_update: CatIn):
    existing_cat = await session.query(Cats).filter(Cats.id == cat_id).first()
    if existing_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")

    # Обновление данных о коте
    for field, value in cat_update.dict(exclude_unset=True).items():
        setattr(existing_cat, field, value)

    # Сохранение изменений
    async with session.begin():
        session.add(existing_cat)

    return existing_cat


@router.delete("/cats")
async def delete_route(cat_id):
    async with session.begin():
        await session.query(Cats).filter(Cats.id == cat_id).delete()
    return "SUCCESS", 200


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app
