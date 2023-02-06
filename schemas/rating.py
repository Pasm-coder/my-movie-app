from typing import Optional
from pydantic import BaseModel, Field


class Rating(BaseModel):

    
    movie_id: int
    rev_id: int
    rev_stars: int
    num_o_ratings: int
    
    class Config:
            schema_extra = {
                "example":{
                    "movie_id":"4",
                    "rev_id":"3",
                    "rev_stars":"5",
                    "num_o_ratings":"8",
                }
            }
