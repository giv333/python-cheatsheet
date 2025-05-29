playlist = []

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def describe(self):
        print(f"Song: {self.title} by {self.artist}")

class DownloadedSong(Song):
    def __init__(self, title, artist, file_size):
        super().__init__(title, artist)
        self.file_size = file_size

    def describe(self):
        print(f"Downloaded: {self.title} by {self.artist} - {self.file_size}MB")

def add_song(song_obj):
    playlist.append(song_obj)
    print(f"Added to playlist: {song_obj.title}")

def remove_song(title):
    for song in playlist:
        if song.title == title:
            playlist.remove(song)
            print(f"Removed from playlist: {title}")
            return
    print(f"Song not found: {title}")

def view_playlist():
    if playlist:
        print("\nCurrent Playlist:")
        for i, song in enumerate(playlist, start=1):
            print(f"{i}. ", end="")
            song.describe()
    else:
        print("Playlist is empty.")

def clear_playlist():
    playlist.clear()
    print("Playlist cleared.") 
