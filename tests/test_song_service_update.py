import pytest
from datetime import date
from unittest.mock import patch
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService


@patch('app.services.song_service.get_session')
def test_update_existing_song(mock_get_session, test_db):

    mock_get_session.return_value.__enter__.return_value = test_db
    
    original = SongService.create(
        SongRequest(title="Original Title", artist="Original Artist")
    )
    
    updated_data = SongRequest(title="Updated Title", artist="Updated Artist")
    result = SongService.update(original.id, updated_data)
    
    assert result.id == original.id
    assert result.title == "Updated Title"
    assert result.artist == "Updated Artist"


@patch('app.services.song_service.get_session')
def test_update_all_fields(mock_get_session, test_db):
    
    mock_get_session.return_value.__enter__.return_value = test_db
    
    original = SongService.create(
        SongRequest(title="Test Song", artist="Test Artist")
    )
    
    updated_data = SongRequest(
        title="New Title",
        artist="New Artist",
        album="New Album",
        genre="Rock",
        release_date=date(2023, 5, 15),
        duration=240.0
    )
    result = SongService.update(original.id, updated_data)
    
    assert result.title == "New Title"
    assert result.artist == "New Artist"
    assert result.album == "New Album"
    assert result.genre == "Rock"
    assert result.release_date == date(2023, 5, 15)
    assert result.duration == 240.0


@patch('app.services.song_service.get_session')
def test_update_sets_optional_fields_to_none(mock_get_session, test_db):
 
    mock_get_session.return_value.__enter__.return_value = test_db
    
    original = SongService.create(
        SongRequest(
            title="Test Song",
            artist="Test Artist",
            album="Test Album",
            genre="Rock",
            duration=180.0
        )
    )
    
    updated_data = SongRequest(
        title="Updated Song",
        artist="Updated Artist",
        album=None,
        genre=None,
        duration=None
    )
    result = SongService.update(original.id, updated_data)
    
    assert result.album is None
    assert result.genre is None
    assert result.duration is None


@patch('app.services.song_service.get_session')
def test_update_not_found_raises_exception(mock_get_session, test_db):

    mock_get_session.return_value.__enter__.return_value = test_db
    
    updated_data = SongRequest(title="New Title", artist="New Artist")
    
    with pytest.raises(Exception) as exc_info:
        SongService.update(9999, updated_data)
    
    assert "not found" in str(exc_info.value).lower()


@patch('app.services.song_service.get_session')
def test_update_updates_timestamp(mock_get_session, test_db):
    
    mock_get_session.return_value.__enter__.return_value = test_db
    
    original = SongService.create(
        SongRequest(title="Test Song", artist="Test Artist")
    )
    original_updated_at = original.updated_at
    
    updated_data = SongRequest(title="Updated Title", artist="Updated Artist")
    result = SongService.update(original.id, updated_data)
    
    assert result.updated_at >= original_updated_at
