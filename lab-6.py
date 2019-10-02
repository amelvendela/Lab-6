class Song:
    def __init__(self, track_rad):
        self.track_list = []
        rensad = track_rad.strip()
        uppdelad = rensad.split("<, >")
        self.artist = uppdelad[0]

    def store(self, object):
        return self.track_list.append(object)

    def __str__(self):
        return "Artist name " + str(self.artist)

    def __lt__(self, other):
        return self.artist < self.other

tracklist = Song("hej")

def read_from_file(filename):
    with open(filename, "r") as file:
        for track_rad in file:
            track = Song(track_rad)
            tracklist.store(track)
            print(track)
    return tracklist
read_from_file("unique_tracks.txt")




