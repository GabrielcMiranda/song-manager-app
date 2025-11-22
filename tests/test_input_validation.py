import pytest
from datetime import date
from pydantic import ValidationError
from app.schemas.song_schema import SongRequest


class TestTitleValidation:
   
    def test_title_required(self):
      
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(artist="Test Artist")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'title' for error in errors)
    
    def test_title_empty_string(self):
        
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(title="", artist="Test Artist")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'title' for error in errors)
    
    def test_title_only_whitespace(self):
    
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(title="   ", artist="Test Artist")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'title' for error in errors)
    
    def test_title_strips_whitespace(self):
        
        song = SongRequest(title="  Test Song  ", artist="Test Artist")
        assert song.title == "Test Song"


class TestArtistValidation:
    
    def test_artist_required(self):
       
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(title="Test Song")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'artist' for error in errors)
    
    def test_artist_empty_string(self):
       
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(title="Test Song", artist="")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'artist' for error in errors)
    
    def test_artist_only_whitespace(self):
       
        with pytest.raises(ValidationError) as exc_info:
            SongRequest(title="Test Song", artist="   ")
        
        errors = exc_info.value.errors()
        assert any(error['loc'][0] == 'artist' for error in errors)
    
    def test_artist_strips_whitespace(self):
       
        song = SongRequest(title="Test Song", artist="  Test Artist  ")
        assert song.artist == "Test Artist"


class TestAlbumValidation:
  
    
    def test_album_optional(self):
        
        song = SongRequest(title="Test Song", artist="Test Artist")
        assert song.album is None
    
    def test_album_empty_string_converts_to_none(self):
        
        song = SongRequest(title="Test Song", artist="Test Artist", album="")
        assert song.album is None
    
    def test_album_whitespace_converts_to_none(self):
       
        song = SongRequest(title="Test Song", artist="Test Artist", album="   ")
        assert song.album is None
    
    def test_album_strips_whitespace(self):

        song = SongRequest(title="Test Song", artist="Test Artist", album="  Test Album  ")
        assert song.album == "Test Album"


class TestGenreValidation:
    
    def test_genre_optional(self):
        
        song = SongRequest(title="Test Song", artist="Test Artist")
        assert song.genre is None
    
    def test_genre_empty_string_converts_to_none(self):
        
        song = SongRequest(title="Test Song", artist="Test Artist", genre="")
        assert song.genre is None
    
    def test_genre_strips_whitespace(self):

        song = SongRequest(title="Test Song", artist="Test Artist", genre="  Rock  ")
        assert song.genre == "Rock"
class TestReleaseDateValidation:
    
    def test_release_date_optional(self):
       
        song = SongRequest(title="Test Song", artist="Test Artist")
        assert song.release_date is None
    
    def test_release_date_valid_format(self):
        
        song = SongRequest(
            title="Test Song", 
            artist="Test Artist",
            release_date=date(2023, 5, 15)
        )
        assert song.release_date == date(2023, 5, 15)
    
    def test_release_date_invalid_type(self):

        with pytest.raises(ValidationError):
            SongRequest(
                title="Test Song",
                artist="Test Artist",
                release_date="invalid"
            )


class TestDurationValidation:
    
    def test_duration_optional(self):
        
        song = SongRequest(title="Test Song", artist="Test Artist")
        assert song.duration is None
    
    def test_duration_valid_number(self):
        
        song = SongRequest(title="Test Song", artist="Test Artist", duration=180.5)
        assert song.duration == 180.5
    
    def test_duration_zero_not_allowed(self):
       
        song = SongRequest(title="Test Song", artist="Test Artist", duration=0)
        assert song.duration == 0  
    
    def test_duration_negative_not_allowed(self):
       
        song = SongRequest(title="Test Song", artist="Test Artist", duration=-10)
        assert song.duration == -10 
    
    def test_duration_invalid_type(self):
       
        with pytest.raises(ValidationError):
            SongRequest(
                title="Test Song",
                artist="Test Artist",
                duration="invalid"
            )


class TestCompleteValidScenarios:
   
    def test_minimal_valid_input(self):

        song = SongRequest(title="Test Song", artist="Test Artist")
        assert song.title == "Test Song"
        assert song.artist == "Test Artist"
        assert song.album is None
        assert song.genre is None
        assert song.release_date is None
        assert song.duration is None
    
    def test_complete_valid_input(self):
       
        song = SongRequest(
            title="Bohemian Rhapsody",
            artist="Queen",
            album="A Night at the Opera",
            genre="Rock",
            release_date=date(1975, 10, 31),
            duration=354.0
        )
        assert song.title == "Bohemian Rhapsody"
        assert song.artist == "Queen"
        assert song.album == "A Night at the Opera"
        assert song.genre == "Rock"
        assert song.release_date == date(1975, 10, 31)
        assert song.duration == 354.0
    
    def test_input_with_extra_whitespace(self):

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
