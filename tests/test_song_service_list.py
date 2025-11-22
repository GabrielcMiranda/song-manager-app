import pytest
from unittest.mock import patch
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService


@patch('app.services.song_service.get_session')
def test_list_returns_songs(mock_get_session, test_db):

    mock_get_session.return_value.__enter__.return_value = test_db
    
    SongService.create(SongRequest(title="Song 1", artist="Artist 1"))
    SongService.create(SongRequest(title="Song 2", artist="Artist 2"))
    
    SongService.list()


@patch('app.services.song_service.get_session')
def test_list_empty_database_raises_exception(mock_get_session, test_db):
   
    mock_get_session.return_value.__enter__.return_value = test_db
    
    with pytest.raises(Exception) as exc_info:
        SongService.list()
    
    assert "no songs found" in str(exc_info.value).lower()
