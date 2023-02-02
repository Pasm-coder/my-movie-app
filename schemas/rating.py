from typing import Optional
from pydantic import BaseModel, Field


class Director(BaseModel):

    id = Optional[int] = None
    mov_id: int
    rev_id: int
    rev_stars: int
    num_o_ratings: int
    
    class Config:
            schema_extra = {
                "example":{
                    "mov_id":"4",
                    "rev_id":"3",
                    "rev_stars":"5",
                    "num_o_ratings":"8",
                }
            }
