import time

from fastapi import APIRouter, FastAPI
from schemas import BaseBreed, BaseCatShort, BaseCatLong, CatIn, CatOutLong, CatOutShort
from typing import List
from database import engine, session
from models import Cats, Breed, Base
from sqlalchemy.future import select
router = APIRouter()


@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@router.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@router.get("/breed", response_model=List[BaseBreed])
async def get_root():
    async with session.begin():
        res = await session.execute(
            select(models.Recipes).order_by(models.Recipes.views.desc(), models.Recipes.time_to_cooking))
    return res.scalars().all()


@router.get("/breed/{breed_name}")
async def get_root():
    pass

@router.get("/cats")
async def get_root():
    pass

@router.get("/cats/{cat_id}")
async def get_root():
    pass



@router.post("/cats")
async def post_route():
    pass


@router.patch("/cats")
async def patch_route():
    pass


@router.delete("/cats")
async def delete_route():
    pass


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app
