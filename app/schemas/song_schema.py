from pydantic import BaseModel, Field
from typing import Optional


class SongRequest(BaseModel):
    
    title: str
    artist: str
    album: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    duration: Optional[float] = None
    
