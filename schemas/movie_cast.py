from typing import Optional
from pydantic import BaseModel, Field



class MovieCast(BaseModel):
        act_id: int
        mov_id: int
        role: str = Field(max_length=30,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "act_id": 1,
                    "mov_id":1,
                    "role":"Part of family"
                }
            }
