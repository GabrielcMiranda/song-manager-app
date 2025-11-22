import pytest
from unittest.mock import patch
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService


@patch('app.services.song_service.get_session')
def test_get_by_id_returns_existing_song(mock_get_session, test_db):
   
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(title="Test Song", artist="Test Artist")
    created_song = SongService.create(song_data)
    
    SongService.get_by_id(created_song.id)


@patch('app.services.song_service.get_session')
def test_get_by_id_with_duration(mock_get_session, test_db):
  
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(
        title="Test Song",
        artist="Test Artist",
        duration=354.0  
    )
    created_song = SongService.create(song_data)
    
    SongService.get_by_id(created_song.id)


@patch('app.services.song_service.get_session')
def test_get_by_id_with_none_duration(mock_get_session, test_db):
    
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song_data = SongRequest(
        title="Test Song",
        artist="Test Artist",
        duration=None
    )
    created_song = SongService.create(song_data)
    
    SongService.get_by_id(created_song.id)


@patch('app.services.song_service.get_session')
def test_get_by_id_not_found_raises_exception(mock_get_session, test_db):
   
    mock_get_session.return_value.__enter__.return_value = test_db
    
    with pytest.raises(Exception) as exc_info:
        SongService.get_by_id(9999)
    
    assert "not found" in str(exc_info.value).lower()
