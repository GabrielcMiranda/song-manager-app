
import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.song import Song
from app.database.config import Base


@pytest.fixture(scope="function")
def test_db():
    
    engine = create_engine("sqlite:///:memory:", echo=False)
    
    Base.metadata.create_all(engine)
    
    TestSessionLocal = sessionmaker(bind=engine)
    session = TestSessionLocal()
    
    yield session  

    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def sample_song_data():
    
    return {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "album": "A Night at the Opera",
        "genre": "Rock",
        "release_date": None,
        "duration": 354.0
    }
