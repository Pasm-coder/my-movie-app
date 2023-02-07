from typing import Optional
from pydantic import BaseModel, Field


class Reviewer(BaseModel):

    
    rev_id: int
    rev_name: str = Field(max_length=15,min_length=3)
    
    class Config:
            schema_extra = {
                "example":{
                    "rev_id":"4",
                    "rev_name":"hola",
                }
            }
