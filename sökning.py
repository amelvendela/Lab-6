import timeit

# vi vill söka efter en artist i listan och se vilken typ av sökning som går snabbast
# linjärsökning i en osorterad. Dvs du skriver in x och ser om det matchar någon artist i listan
# binärsökning i en sorterad lista
# sökning i hashtabell


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
            #print(track)
    return tracklist
read_from_file("unique_tracks.txt")


def linsok(lista, artist):
    for x in lista:
        if x == artist:  # om input är en artist som finns med i listan
            return True
    return False


def main():

    filename = "/Users/amelbjorkbom/PycharmProjects/Lab-6/unique_tracks.txt"

    lista = read_from_file(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")