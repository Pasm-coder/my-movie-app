from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.rating import Rating
from models.rating import Rating as RatingModel
from service.rating import RatingService


rating_router = APIRouter()


@rating_router.get('/rating/{id}', tags=['rating'],response_model=list[Rating],status_code=200)
def get_rating(id:int ):
    db = Session()
    result = RatingService(db).get_rating(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@rating_router.post('/rating', tags=['rating'],response_model=dict,status_code=201)
def create_rating(rating:Rating)->dict:
    db = Session()
    RatingService(db).create_rating(rating)
    return JSONResponse(content={"message":"Se ha registrado el rating","status_code":201})
