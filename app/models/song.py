from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from datetime import datetime
from app.database.config import Base


class Song(Base):

    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    artist = Column(String(200), nullable=False)
    album = Column(String(200), nullable=True)
    genre = Column(String(100), nullable=True)
    release_date = Column(Date, nullable=True)
    duration = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)