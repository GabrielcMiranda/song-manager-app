import pytest
from unittest.mock import patch
from app.models.song import Song
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService


@patch('app.services.song_service.get_session')
def test_delete_existing_song(mock_get_session, test_db):
   
    mock_get_session.return_value.__enter__.return_value = test_db
    
    song = SongService.create(
        SongRequest(title="Test Song", artist="Test Artist")
    )
    song_id = song.id
    
    SongService.delete(song_id)
    
    deleted_song = test_db.query(Song).filter(Song.id == song_id).first()
    assert deleted_song is None


@patch('app.services.song_service.get_session')
def test_delete_not_found_raises_exception(mock_get_session, test_db):
    
    mock_get_session.return_value.__enter__.return_value = test_db
    
    with pytest.raises(Exception) as exc_info:
        SongService.delete(9999)
    
    assert "not found" in str(exc_info.value).lower()


@patch('app.services.song_service.get_session')
def test_delete_removes_only_specified_song(mock_get_session, test_db):

    mock_get_session.return_value.__enter__.return_value = test_db
    
    song1 = SongService.create(SongRequest(title="Song 1", artist="Artist 1"))
    song2 = SongService.create(SongRequest(title="Song 2", artist="Artist 2"))
    song3 = SongService.create(SongRequest(title="Song 3", artist="Artist 3"))
    
    SongService.delete(song2.id)
    
    assert test_db.query(Song).filter(Song.id == song1.id).first() is not None
    assert test_db.query(Song).filter(Song.id == song2.id).first() is None
    assert test_db.query(Song).filter(Song.id == song3.id).first() is not None
