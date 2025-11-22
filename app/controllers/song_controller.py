
from app.schemas.song_schema import SongRequest
from app.services.song_service import SongService
from app.utils.logger import logger
from datetime import datetime
from pydantic import ValidationError

class SongController:

    @staticmethod
    def list_songs():
        try:
            SongService.list()
            input("\nPress Enter to continue...")
        except Exception as e:
            logger.error(f"Error in list_songs: {str(e)}")
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
            logger.error(f"Validation error in create_song: {e.errors()}")
            for error in e.errors():
                field = error['loc'][0] 
                message = error['msg']   
                print(f"\n  - {field}: {message}")
            input("\nPress Enter to continue...")
            
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid input in create_song: {str(e)}")
            print(f"\nInvalid input format: Please check the values you entered.")
            input("\nPress Enter to continue...")
            
        except Exception as e:
            logger.error(f"Error in create_song: {str(e)}")
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
          
    @staticmethod
    def get_song_by_id():
        try:
            song_id = int(input("\n\nEnter song ID: ").strip())
            SongService.get_by_id(song_id)
            input("\nPress Enter to continue...")
            
        except ValueError as e:
            logger.error(f"Invalid ID in get_by_id: {str(e)}")
            print("\nInvalid ID: Please enter a valid number.")
            input("\nPress Enter to continue...")
            
        except Exception as e:
            logger.error(f"Error in get_by_id: {str(e)}")
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
            logger.error(f"Validation error in update_song: {e.errors()}")
            for error in e.errors():
                field = error['loc'][0] 
                message = error['msg']   
                print(f"\n  - {field}: {message}")
            input("\nPress Enter to continue...")
            
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid input in update_song: {str(e)}")
            print(f"\nInvalid input format: Please check the values you entered.")
            input("\nPress Enter to continue...")
            
        except Exception as e:
            logger.error(f"Error in update_song: {str(e)}")
            print(f"\nError: {e}")
            input("\nPress Enter to continue...")
    
    @staticmethod
    def delete_song():
        try:
            song_id = int(input("\n\nEnter song ID to delete: ").strip())
            SongService.delete(song_id)
            print(f"\n\nSong ID {song_id} deleted successfully.")
            input("\nPress Enter to continue...")

        except ValueError as e:
            logger.error(f"Invalid ID in delete_song: {str(e)}")
            print("\nInvalid ID: Please enter a valid number.")
            input("\nPress Enter to continue...")

        except Exception as e:
            logger.error(f"Error in delete_song: {str(e)}")
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

        duration = None
        if duration_input:
            duration = float(duration_input)
            if duration <= 0:
                raise ValueError()
        
        song_data = SongRequest(
            title=title,
            artist=artist,
            album=album,
            genre=genre,
            release_date=release_date,
            duration=duration
        )
        
        return song_data