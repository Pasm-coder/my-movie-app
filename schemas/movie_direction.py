from typing import Optional
from pydantic import BaseModel, Field



class MovieDirection(BaseModel):

    direction_id: int
    movie_id: int
    
    class Config:
            schema_extra = {
                "example":{
                    "direction_id":1,
                    "movie_id":2,
                }
            }
