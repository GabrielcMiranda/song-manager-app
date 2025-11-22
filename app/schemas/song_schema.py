from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional
from datetime import date


class SongRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(..., min_length=1)
    artist: str = Field(..., min_length=1)
    album: Optional[str] = None
    genre: Optional[str] = None
    release_date: Optional[date] = None
    duration: Optional[float] = None
    
    @field_validator('album', 'genre', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        
        if isinstance(v, str) and not v.strip():
            return None
        return v
    
