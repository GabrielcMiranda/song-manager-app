
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService
from datetime import datetime
from pydantic import ValidationError

class SongController:

    @staticmethod
    def list_songs():
        try:
            SongService.list()
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")

    @staticmethod
    def create_song():
        try:
            song_data = SongController.request_song_data()
            
            new_song = SongService.create(song_data)
            print(f"\n\nSong {new_song.title} created with ID: {new_song.id}")
            input("\nPress Enter to continue...")
            
        except ValidationError as e:
            for error in e.errors():
                field = error['loc'][0] 
                message = error['msg']   
                print(f"\n  - {field}: {message}")
            input("\nPress Enter to continue...")
            
        except (ValueError, TypeError) as e:
            print(f"\nInvalid input format: Please check the values you entered.")
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
          
    @staticmethod
    def get_song_by_id():
        try:
            song_id = int(input("\n\nEnter song ID: ").strip())
            SongService.get_by_id(song_id)
            input("\nPress Enter to continue...")
            
        except ValueError:
            print("\nInvalid ID: Please enter a valid number.")
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
    
    @staticmethod
    def update_song():
        try:
            song_id = int(input("\n\nEnter song ID to update: ").strip())
            song_data = SongController.request_song_data()
            
            updated_song = SongService.update(song_id, song_data)
            print(f"\n\nSong ID {updated_song.id} updated successfully.")
            input("\nPress Enter to continue...")
        
        except ValidationError as e:
            for error in e.errors():
                field = error['loc'][0] 
                message = error['msg']   
                print(f"\n  - {field}: {message}")
            input("\nPress Enter to continue...")
            
        except (ValueError, TypeError) as e:
            print(f"\nInvalid input format: Please check the values you entered.")
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
    
    @staticmethod
    def delete_song():
        try:
            song_id = int(input("\n\nEnter song ID to delete: ").strip())
            SongService.delete(song_id)
            print(f"\n\nSong ID {song_id} deleted successfully.")
            input("\nPress Enter to continue...")

        except ValueError:
            print("\nInvalid ID: Please enter a valid number.")
            input("\nPress Enter to continue...")

        except Exception as e:
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
            
    

    def request_song_data():

        title = input("\n\nEnter song title: ").strip()
        artist = input("Enter artist name: ").strip()
        album = input("Enter album name (optional): ").strip() or None
        genre = input("Enter genre (optional): ").strip() or None
        date_input = input("Enter release date (YYYY-MM-DD, optional): ").strip() or None
        release_date = datetime.strptime(date_input, "%Y-%m-%d").date() if date_input else None
        duration_input = input("Enter duration in seconds (optional): ").strip() or None
        duration = float(duration_input) if duration_input else None
        
        song_data = SongRequest(
            title=title,
            artist=artist,
            album=album,
            genre=genre,
            release_date=release_date,
            duration=duration
        )
        
        return song_data