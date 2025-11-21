
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService


class SongController:

    @staticmethod
    def list_songs():
        try:
            songs = SongService.list()
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
            return []
        return songs

    @staticmethod
    def create_song():
        try:
            song_data = SongController.request_song_data()
            
            new_song = SongService.create(song_data)
            print(f"\n\nSong {new_song.title} created with ID: {new_song.id}")
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
            return None                
        return new_song
          
    @staticmethod
    def get_song_by_id():
        try:
            song_id = int(input("\n\nEnter song ID: ").strip())
            song = SongService.get_by_id(song_id)
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
            return None
        return song
    
    @staticmethod
    def update_song():
        try:
            song_id = int(input("\n\nEnter song ID to update: ").strip())
            song_data = SongController.request_song_data()
            
            updated_song = SongService.update(song_id, song_data)
            print(f"\n\nSong ID {updated_song.id} updated successfully.")
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
            return None
        return updated_song
    

    def request_song_data():

        title = input("\n\nEnter song title: ").strip()
        artist = input("Enter artist name: ").strip()
        album = input("Enter album name (optional): ").strip() or None
        genre = input("Enter genre (optional): ").strip() or None
        year_input = input("Enter year (optional): ").strip() or None
        year = int(year_input) if year_input else None
        duration_input = input("Enter duration in seconds (optional): ").strip() or None
        duration = float(duration_input) if duration_input else None
        
        song_data = SongRequest(
            title=title,
            artist=artist,
            album=album,
            genre=genre,
            year=year,
            duration=duration
        )
        
        return song_data