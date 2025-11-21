
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService


class SongController:

    @staticmethod
    def list_songs():
        try:
            songs = SongService.list()
        except Exception as e:
            print(f"Error: {e}")
            return []
        return songs

    @staticmethod
    def create_song():
        try:
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            album = input("Enter album name (optional): ") or None
            genre = input("Enter genre (optional): ") or None
            year_input = input("Enter year (optional): ") or None
            year = int(year_input) if year_input else None
            duration_input = input("Enter duration in seconds (optional): ") or None
            duration = float(duration_input) if duration_input else None
            
            song_data = SongRequest(
                title=title,
                artist=artist,
                album=album,
                genre=genre,
                year=year,
                duration=duration
            )
            
            new_song = SongService.create(song_data)
            print(f"Song {new_song.title} created with ID: {new_song.id}")

        except Exception as e:
            print(f"Error: {e}")
            return None

        return new_song