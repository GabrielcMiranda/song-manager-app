
import pytest
from datetime import date
from app.models.song import Song
from app.schemas.song_schema import SongRequest


def test_create_song_with_all_fields(test_db, sample_song_data):
   
    song_data = SongRequest(**sample_song_data)
    
    new_song = Song(
        title=song_data.title,
        artist=song_data.artist,
        album=song_data.album,
        genre=song_data.genre,
        release_date=song_data.release_date,
        duration=song_data.duration
    )
    test_db.add(new_song)
    test_db.commit()
    test_db.refresh(new_song)
    
    assert new_song.id is not None
    assert new_song.title == "Bohemian Rhapsody"
    assert new_song.artist == "Queen"
    assert new_song.album == "A Night at the Opera"
    assert new_song.genre == "Rock"
    assert new_song.duration == 354.0
    assert new_song.created_at is not None
    assert new_song.updated_at is not None


def test_create_song_with_required_fields_only(test_db):
   
    song_data = SongRequest(
        title="Test Song",
        artist="Test Artist"
    )
    
    new_song = Song(
        title=song_data.title,
        artist=song_data.artist
    )
    test_db.add(new_song)
    test_db.commit()
    test_db.refresh(new_song)
    
    assert new_song.id is not None
    assert new_song.title == "Test Song"
    assert new_song.artist == "Test Artist"
    assert new_song.album is None
    assert new_song.genre is None
    assert new_song.release_date is None
    assert new_song.duration is None


def test_create_song_with_release_date(test_db):
    
    song_data = SongRequest(
        title="Yesterday",
        artist="The Beatles",
        release_date=date(1965, 9, 13)
    )
    
    new_song = Song(
        title=song_data.title,
        artist=song_data.artist,
        release_date=song_data.release_date
    )
    test_db.add(new_song)
    test_db.commit()
    test_db.refresh(new_song)
    
    assert new_song.release_date == date(1965, 9, 13)


def test_create_song_validates_required_title():
   
    with pytest.raises(Exception): 
        SongRequest(artist="Test Artist")


def test_create_song_validates_required_artist():
    
    with pytest.raises(Exception):  
        SongRequest(title="Test Song")


def test_create_song_strips_whitespace(test_db):
   
    song_data = SongRequest(
        title="  Test Song  ",
        artist="  Test Artist  "
    )
    
    new_song = Song(
        title=song_data.title,
        artist=song_data.artist
    )
    test_db.add(new_song)
    test_db.commit()
    test_db.refresh(new_song)
    
    assert new_song.title == "Test Song" 
    assert new_song.artist == "Test Artist" 
