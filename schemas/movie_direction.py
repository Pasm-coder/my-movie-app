from typing import Optional
from pydantic import BaseModel, Field



class MovieDirection(BaseModel):

    dir_id: Optional[int] = None
    mov_id: Optional[int] = None
    
    class Config:
            schema_extra = {
                "example":{
                    "dir_id":1,
                    "mov_id":2,
                }
            }
