import pytest
from datetime import date
from pydantic import ValidationError
from app.schemas.song_schema import SongRequest


class TestRequiredFields:
    
    def test_title_required(self):
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(artist="Test Artist")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'title' for error in errors)
    
    def test_artist_required(self):
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(title="Test Song")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'artist' for error in errors)
    
    def test_empty_string_not_allowed(self):

        with pytest.raises(ValidationError):
            SongRequest(title="", artist="Test Artist")
        
        with pytest.raises(ValidationError):
            SongRequest(title="Test Song", artist="")
    
    def test_whitespace_only_not_allowed(self):
        with pytest.raises(ValidationError):
            SongRequest(title="   ", artist="Test Artist")
        
        with pytest.raises(ValidationError):
            SongRequest(title="Test Song", artist="   ")


class TestWhitespaceStripping:
    
    def test_strips_whitespace_from_all_string_fields(self):
        song = SongRequest(
            title="  Test Song  ",
            artist="  Test Artist  ",
            album="  Test Album  ",
            genre="  Rock  "
        )
        
        assert song.title == "Test Song"
        assert song.artist == "Test Artist"
        assert song.album == "Test Album"
        assert song.genre == "Rock"


class TestOptionalFields:
    
    def test_optional_fields_default_to_none(self):
        song = SongRequest(title="Test Song", artist="Test Artist")
        
        assert song.album is None
        assert song.genre is None
        assert song.release_date is None
        assert song.duration is None
    
    def test_empty_string_converts_to_none(self):
        song = SongRequest(
            title="Test Song",
            artist="Test Artist",
            album="",
            genre=""
        )
        
        assert song.album is None
        assert song.genre is None
    
    def test_whitespace_converts_to_none(self):
        song = SongRequest(
            title="Test Song",
            artist="Test Artist",
            album="   ",
            genre="   "
        )
        
        assert song.album is None
        assert song.genre is None


class TestReleaseDateValidation:

    
    def test_release_date_accepts_valid_date(self):
       
        song = SongRequest(
            title="Test Song",
            artist="Test Artist",
            release_date=date(2023, 5, 15)
        )
        assert song.release_date == date(2023, 5, 15)
    
    def test_release_date_rejects_invalid_type(self):

        with pytest.raises(ValidationError):
            SongRequest(
                title="Test Song",
                artist="Test Artist",
                release_date="2023-05-15"
            )


class TestDurationValidation:
   
    
    def test_duration_accepts_valid_number(self):
        
        song = SongRequest(
            title="Test Song",
            artist="Test Artist",
            duration=180.5
        )
        assert song.duration == 180.5
    
    def test_duration_rejects_invalid_type(self):
     
        with pytest.raises(ValidationError):
            SongRequest(
                title="Test Song",
                artist="Test Artist",
                duration="invalid"
            )
