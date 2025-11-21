from app.models.song import Song
from app.database.config import get_session
from app.schemas.song_schema import SongRequest


class SongService:
    
    @staticmethod
    def list():
       
        with get_session() as session:

            result = session.query(Song).all()
            
            if not result:
                raise Exception("No songs found!")
            
            for song in result:
                print(f"Song #{song.id}: {song.title} by {song.artist} - {song.year}")
            
            return result
    
    @staticmethod
    def create(song_data: SongRequest):
        
        with get_session() as session:
            
            new_song = Song(
                title=song_data.title,
                artist=song_data.artist,
                album=song_data.album,
                genre=song_data.genre,
                year=song_data.year,
                duration=song_data.duration
            )
            
            session.add(new_song)
            session.commit()
            session.refresh(new_song) 
            
            return new_song
        
    