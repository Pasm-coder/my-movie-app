from typing import Optional
from pydantic import BaseModel, Field


class Actor(BaseModel):
        act_id: Optional[int] = None
        act_fname: str = Field(max_length=15,min_length=3)
        act_lname: str = Field(max_length=15,min_length=3)
        act_gender: str = Field(max_length=15,min_length=1)

        class Config:
            schema_extra = {
                "example":{
                    "act_fname": "Vin",
                    "act_lname":"Diesel",
                    "act_gender":"M"
                }
            }
