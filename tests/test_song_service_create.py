from datetime import date
from unittest.mock import patch
from app.models.song import Song
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService


@patch('app.services.song_service.get_session')
def test_create_returns_song_with_id(mock_get_session, test_db):
  
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(title="Hotel California", artist="Eagles")
    
    result = SongService.create(song_data)
    
    assert result is not None
    assert result.id is not None
    assert result.title == "Hotel California"
    assert result.artist == "Eagles"


@patch('app.services.song_service.get_session')
def test_create_with_all_fields(mock_get_session, test_db):
  
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(
        title="Stairway to Heaven",
        artist="Led Zeppelin",
        album="Led Zeppelin IV",
        genre="Rock",
        release_date=date(1971, 11, 8),
        duration=482.0
    )
    
    result = SongService.create(song_data)
    
    assert result.title == "Stairway to Heaven"
    assert result.artist == "Led Zeppelin"
    assert result.album == "Led Zeppelin IV"
    assert result.genre == "Rock"
    assert result.release_date == date(1971, 11, 8)
    assert result.duration == 482.0


@patch('app.services.song_service.get_session')
def test_create_with_optional_fields_as_none(mock_get_session, test_db):
    
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(title="Test Song", artist="Test Artist")
    
    result = SongService.create(song_data)
    
    assert result.album is None
    assert result.genre is None
    assert result.release_date is None
    assert result.duration is None


@patch('app.services.song_service.get_session')
def test_create_persists_to_database(mock_get_session, test_db):
   
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(title="Imagine", artist="John Lennon")
    
    result = SongService.create(song_data)
    
    saved_song = test_db.query(Song).filter(Song.id == result.id).first()
    assert saved_song is not None
    assert saved_song.title == "Imagine"


@patch('app.services.song_service.get_session')
def test_create_sets_timestamps(mock_get_session, test_db):
  
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(title="Test Song", artist="Test Artist")
    
    result = SongService.create(song_data)
    
    assert result.created_at is not None
    assert result.updated_at is not None
