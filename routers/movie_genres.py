from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_genres import MovieGenres
from models.movie_genres import MovieGenres as MovieGenresModel
from service.movie_genres import MovieGenresService


movie_genres_router = APIRouter()


@movie_genres_router.get('/movie/{gen_id}/genres/', tags=['genres'],response_model=list[MovieGenres],status_code=200)
def get_movie_genres(gen_id:int ):
    db = Session()
    result = MovieGenresService(db).get_movie_genres(gen_id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_genres_router.post('/moviegenres', tags=['moviegenres'],response_model=dict,status_code=201)
def create_movie_genres(moviegenres:MovieGenres)->dict:
    db = Session()
    MovieGenresService(db).create_movie_genres(moviegenres)
    return JSONResponse(content={"message":"Se ha registrado el movie genres","status_code":201})
