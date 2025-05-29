import smartplaylist as sp

song1 = sp.Song("Apple Jack", "Dolly Parton")
song2 = sp.DownloadedSong("Gambler", "Kenny Rogers", 5)

sp.add_song(song1)
sp.add_song(song2)

sp.view_playlist()

sp.remove_song("Apple Jack")
sp.view_playlist()

sp.clear_playlist()
sp.view_playlist()
