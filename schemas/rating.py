from pydantic import BaseModel, Field
from typing import Optional 

class Movie(BaseModel):
        mov_id: Optional[int] = None
        rev_id: str = Field(max_length=15,min_length=3)
        overview: str = Field(max_length=300,min_length=10)
        year: int = Field(le=2022)
        time: float = Field(ge=1,le=10)
        date_release : str  = Field(max_length=15,min_length=3)
        release_contry: str = Field(max_length=15,min_length=3)
        rev_srtars = int
        num_o_ratings = int

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'title': 'Avatar',
                    'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                    'year':2002,
                    'time': 1.50,
                    'date_release':'2009',
                    'release_contry':'USA',
                }
            }
