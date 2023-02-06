from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_direction import MovieDirection
from models.movie_direction import MovieDirection as MovieDirectionModel
from service.movie_direction import MovieDirectionService


movie_direction_router = APIRouter()


@movie_direction_router.get('/movie/{direction_id}/direction/', tags=['direction'],response_model=list[MovieDirection],status_code=200)
def get_movie_direction(direction_id:int ):
    db = Session()
    result = MovieDirectionService(db).get_movie_direction(direction_id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_direction_router.post('/moviedirection', tags=['moviedirection'],response_model=dict,status_code=201)
def create_movie_direction(moviedirection:MovieDirection)->dict:
    db = Session()
    MovieDirectionService(db).create_movie_direction(moviedirection)
    return JSONResponse(content={"message":"Se ha registrado el movie direction","status_code":201})
