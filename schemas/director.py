from typing import Optional
from pydantic import BaseModel, Field


class Director(BaseModel):

    
    director_fname: str = Field(max_length=15,min_length=3)
    director_lname: str = Field(max_length=15,min_length=3)
    
    class Config:
            schema_extra = {
                "example":{
                    "director_fname": "Bryan",
                    "director_lname": "Singer",
                }
            }
