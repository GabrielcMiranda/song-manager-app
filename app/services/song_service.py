from app.models.song import Song
from app.database.config import get_session
from app.schemas.song_schema import SongRequest
from app.utils.logger import logger


class SongService:
    
    @staticmethod
    def list():
       
        with get_session() as session:

            result = session.query(Song).all()
            
            if not result:
                logger.warning("No songs found in the database.")
                raise Exception("\n\nNo songs found!")
            
            for song in result:
                print(f"\n\nSong #{song.id}: {song.title} by {song.artist}")
            
    
    @staticmethod
    def create(song_data: SongRequest):
        
        with get_session() as session:
            
            new_song = Song(
                title=song_data.title,
                artist=song_data.artist,
                album=song_data.album,
                genre=song_data.genre,
                release_date=song_data.release_date,
                duration=song_data.duration
            )
            
            session.add(new_song)
            session.commit()
            session.refresh(new_song)
            
            logger.info(f"Song created: ID={new_song.id}, Title='{new_song.title}', Artist='{new_song.artist}'")
            return new_song
            
    
    @staticmethod
    def get_by_id(song_id: int):
        
        with get_session() as session:
            
            song = session.query(Song).filter(Song.id == song_id).first()
            
            if not song:
                logger.warning(f"Song not found: ID={song_id}")
                raise Exception(f"\n\nSong with ID {song_id} not found!")
            
            logger.info(f"Song found: ID={song_id}, Title='{song.title}'")
            
            song_duration = None
            if song.duration is not None:
                minutes = int(song.duration // 60)
                seconds = int(song.duration % 60)
                song_duration = f"{minutes}:{seconds:02d} min"

            print(f"\n\nSong #{song.id}: {song.title} by {song.artist}"
                  f"\n release date: {song.release_date}\n album: {song.album}\n genre: {song.genre}\n duration: {song_duration}"
                  f"\n song created at: {song.created_at}\n last update at: {song.updated_at}")
            
        
    @staticmethod
    def update(song_id: int, song_data: SongRequest):
        
        with get_session() as session:
            
            song = session.query(Song).filter(Song.id == song_id).first()
            
            if not song:
                logger.warning(f"Song not found for update: ID={song_id}")
                raise Exception(f"\n\nSong with ID {song_id} not found!")
            
            song.title = song_data.title
            song.artist = song_data.artist
            song.album = song_data.album
            song.genre = song_data.genre
            song.release_date = song_data.release_date
            song.duration = song_data.duration
            
            session.commit()
            session.refresh(song)
            
            logger.info(f"Song updated: ID={song_id}, Title='{song.title}'")
            return song
            
        
    @staticmethod
    def delete(song_id: int):
        
        with get_session() as session:
            
            song = session.query(Song).filter(Song.id == song_id).first()
            
            if not song:
                logger.warning(f"Song not found for deletion: ID={song_id}")
                raise Exception(f"\n\nSong with ID {song_id} not found!")
            
            song_title = song.title
            session.delete(song)
            session.commit()
            
            logger.info(f"Song deleted: ID={song_id}, Title='{song_title}'")
            
        
    