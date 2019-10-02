class Node:
    def __init__(self, x):
        self.value = x
        self.left = None    # Skapar en left-pekare
        self.right = None   # Skapar en right-pekare


class BinTree:
    def __init__(self):
        self.root = None    # Skapar en rot, som i normalläget innehåller None

    def put(self, newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):  # Magisk metod som reagerar på "in"
        # True om value finns i trädet, annars False
        return finns(self.root, value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print('\n')


def putta(p, newvalue):
    if p is None:   # Har vi inget i trädet skapas här en ny nod (value och en next-pekare)
        p = Node(newvalue)
    if newvalue < p.value:  # Om nya värdet är mindre än värdet i roten så hamnar den till vänster
        p.left = putta(p.left, newvalue)
    if newvalue > p.value:  # Om nya värdet är större än värdet i roten så hamnar den till höger
        p.right = putta(p.right, newvalue)
    return p


def finns(p, value):    # Letar efter värden i trädet
    if p is None:   # Om där inte finns något i trädet returneras False
        return False
    if value == p.value:    # Om där finns ett värde som överensstämmer med något i vårt binärträd returneras True
        return True
    if value < p.value:     # Om värdet är mindre än roten, så går vi till vänster och letar efter vårt värde
        return finns(p.left, value)
    if value > p.value:     # Om värdet är större än roten, så går vi till höger och letar efter vårt värde
        return finns(p.right, value)


def skriv(p):   # Skriver ut trädet i inorder, skriv och rita upp metod!
    if p is None:   # Om det finns några värden i trädet händer:
        skriv(p.left)   # Skriver först ut allt som står i vänster och därefter höger, nedifrån och upp
        print(p.value)        # Skriver roten
        skriv(p.right)  # Skriver sedan ut allt som står i höger om roten. Allt som står på vänster sida nedifrån
        # först och sedan de högra värdena
