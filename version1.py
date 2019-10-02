import timeit
from binTreeFile import BinTree

# vi vill söka efter en artist i listan och se vilken typ av sökning som går snabbast
# linjärsökning i en osorterad. Dvs du skriver in x och ser om det matchar någon artist i listan
# binärsökning i en sorterad lista
# sökning i hashtabell


class Song:
    def __init__(self, trackid, song_time, artist, song_name):
        self.trackid = trackid
        self.song_time = song_time
        self.artist = artist
        self.song_name = song_name

    def __lt__(self, other):
        return self.artist < other.artist

    def __str__(self):
        return "TrackID: " + self.trackid + " Låttid: " + self.song_time + " Artist: " + self.artist + " Låttitel: " + \
               self.song_name


def read_from_file():
    song_list = []
    song_dict = {}
    # song_tree = BinTree()
    artist_tree = BinTree()

    with open('unique_tracks.txt', "r") as file:
        for track_rad in file:
            split_list = track_rad.split("<SEP>")
            track = Song(split_list[0], split_list[1], split_list[2], split_list[3])
            song_list.append(track)
            song_dict[track.artist] = track
            # song_tree.put(track.artist)
            artist_tree.put(track.artist)
    return song_list, song_dict, artist_tree


def linsok(lista, artist):
    for x in lista:
        if x == artist:  # om input är en artist som finns med i listan
            return True
    return False


def binsok(lista, artist):
    """Från föreläsning 3"""
    """Söker i "listan" efter "nyckel". Returnerar True om den hittas, False annars"""
    """Den räknar ut vart mitten är och avgör vänster eller höger. Sedan fortsätter den så tills den hittar nyckeln 
    eller nyckeln inte finns"""
    vanster = 0
    hoger = len(lista) - 1
    found = False

    while vanster <= hoger and not found:
        mitten = (vanster + hoger) // 2
        if lista[mitten].artist == artist:
            found = True
        else:
            if artist < lista[mitten].artist:
                hoger = mitten - 1
            else:
                vanster = mitten + 1
    return found


def main():

    testartist2 = input("Choose an artist: ")

    lista, dictionary, artist_tree = read_from_file()

    smaller_list = lista[0:250000]
    n = len(smaller_list)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist2 = sista.artist

    # To return a new list, use the sorted() built-in function newlist = sorted(ut, key=lambda x: x.count) från stack
    # overflow, inbyggd pythonmetod
    sorted_list = sorted(smaller_list, key=lambda x: x.artist)

    sorting_time = timeit.timeit(stmt=lambda: sorted(smaller_list, key=lambda x: x.artist), number=1)
    print("Sorteringen tog", round(sorting_time, 4), "sekunder")

    linear_time = timeit.timeit(stmt=lambda: linsok(smaller_list, testartist2), number=10)
    print("Linjärsökningen tog", round(linear_time, 4), "sekunder")

    bintid = timeit.timeit(stmt=lambda: binsok(sorted_list, testartist2), number=10)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")

    dicttid = timeit.timeit(stmt=lambda: dictionary[testartist2], number=10)
    print("Dictsökningen tog", round(dicttid, 4), "sekunder")

    bintreetid = timeit.timeit(stmt=lambda: testartist2 in artist_tree, number=10)
    print("Bintreesökningen tog", round(bintreetid, 4), "sekunder")


if __name__ == '__main__':
    main()
