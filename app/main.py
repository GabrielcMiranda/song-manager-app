from app.controllers.song_controller import SongController
import os

while(True):
    os.system('cls')
    print("\n\n\n\n\n================================ SONG MANAGER ================================\n\n\n")
    print("Choose an option:")
    print("1. List songs")
    print("2. Store a new song")
    print("3. Search song by ID")
    print("4. Update song by ID")
    print("5. Exit\n\n")

    choice = input("Option: ")

    if choice == "1":
        SongController.list_songs()

    if choice == "2":
        SongController.create_song()

    if choice == "3":
        SongController.get_song_by_id()

    if choice == "4":
        SongController.update_song()

    if choice == "5":
        break