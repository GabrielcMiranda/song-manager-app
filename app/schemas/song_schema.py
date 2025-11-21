from pydantic import BaseModel, Field, field_validator
from typing import Optional


class SongRequest(BaseModel):
    """Schema para criar uma nova música"""
    
    title: str = Field(..., min_length=1, strip_whitespace=True)
    artist: str = Field(..., min_length=1, strip_whitespace=True)
    album: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    duration: Optional[float] = None
    
    @field_validator('album', 'genre', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        
        if isinstance(v, str) and not v.strip():
            return None
        return v
    
