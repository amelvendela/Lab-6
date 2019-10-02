def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1, n):
            if data[j] < data[minst]:
                minst = j
        data[minst], data[i] = data[i], data[minst]
    return data


def insattningssortera(data):
    n = len(data)
    for i in range(1, n):
        varde = data[i]
        plats = i
        while plats > 0 and data[plats-1] > varde:
            data[plats] = data[plats-1]
            plats = plats - 1
        data[plats] = varde
    return data


def main():
    sort_1 = urvalssortera(lista)
    sort_2 = insattningssortera(lista)
    print('Sorteringen tog', sort_1, 'sekunder')
    print('Sorteringen tog', sort_2, 'sekunder')
