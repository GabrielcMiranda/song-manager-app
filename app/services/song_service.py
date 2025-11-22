from app.models.song import Song
from app.database.config import get_session
from app.schemas.song_schema import SongRequest


class SongService:
    
    @staticmethod
    def list():
       
        with get_session() as session:

            result = session.query(Song).all()
            
            if not result:
                raise Exception("\n\nNo songs found!")
            
            for song in result:
                print(f"\n\nSong #{song.id}: {song.title} by {song.artist} - {song.year}")
            
    
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
            
    
    @staticmethod
    def get_by_id(song_id: int):
        
        with get_session() as session:
            
            song = session.query(Song).filter(Song.id == song_id).first()
            
            if not song:
                raise Exception(f"\n\nSong with ID {song_id} not found!")
            
            song_duration = str(song.duration) + " seconds" if song.duration is not None else None
            print(f"\n\nSong #{song.id}: {song.title} by {song.artist} - {song.year}"
                  f"\n album: {song.album}\n genre: {song.genre}\n duration: {song_duration}\n"
                  f" song created at: {song.created_at}\n last update at: {song.updated_at}")
            
        
    @staticmethod
    def update(song_id: int, song_data: SongRequest):
        
        with get_session() as session:
            
            song = session.query(Song).filter(Song.id == song_id).first()
            
            if not song:
                raise Exception(f"\n\nSong with ID {song_id} not found!")
            
            song.title = song_data.title
            song.artist = song_data.artist
            song.album = song_data.album
            song.genre = song_data.genre
            song.year = song_data.year
            song.duration = song_data.duration
            
            session.commit()
            session.refresh(song)
            
        
    @staticmethod
    def delete(song_id: int):
        
        with get_session() as session:
            
            song = session.query(Song).filter(Song.id == song_id).first()
            
            if not song:
                raise Exception(f"\n\nSong with ID {song_id} not found!")
            
            session.delete(song)
            session.commit()
            
        
    