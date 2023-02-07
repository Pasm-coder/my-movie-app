from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.reviewer import Reviewer
from models.reviewer import Reviewer as ReviewerModel
from service.reviewer import ReviewerService


reviewer_router = APIRouter()


@reviewer_router.get('/reviewer/{id}', tags=['reviewer'],response_model=list[Reviewer],status_code=200)
def get_reviewer(id:int ):
    db = Session()
    result = ReviewerService(db).get_reviewer(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@reviewer_router.post('/reviewer', tags=['reviewer'],response_model=dict,status_code=201)
def create_reviewer(reviewer:Reviewer)->dict:
    db = Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(content={"message":"Se ha registrado el reviewer","status_code":201})
