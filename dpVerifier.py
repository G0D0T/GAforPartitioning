# Funzione per inserire in una lista quanto scritto nel file delle soluzioni generato da ga.py
def extract_data(content):
    lista = []
    out = []
    for i, c in enumerate(content):
        elem = []
        lista.append(c.split('], '))
        first = lista[i][0][2:]
        temp = [int(n) for n in first.split(', ')]
        elem.append(temp)
        second = lista[i][1][1:]
        temp = [int(n) for n in second.split(', ')]
        elem.append(temp)
        third = lista[i][2][:-1]
        elem.append(int(third))
        out.append(elem)
    return out


# Funzione che sfrutta la programmazione dinamica per riempire una tabella in modo bottom-up
# Per la risoluzione in tempo pseudopolinomiale del Number Partitioning problem
def find_part(s):
    n = len(s)
    k = sum(s)
    if k % 2:
        return False
    k2 = k // 2
    rows = k2 + 1
    cols = n + 1
    p = [[True for i in range(cols)] for j in range(rows)]
    for i in range(1, rows):
        p[i][0] = False
    for i in range(1, rows):
        for j in range(1, cols):
            p[i][j] = p[i][j - 1]
            if i >= s[j - 1]:
                p[i][j] = (p[i][j] or p[i - s[j - 1]][j - 1])

    return p[k2][n]


def main():
    # s = [8, 6, 3, 2, 1, 2, 1, 1]
    # s = [44, 50, 1, 82, 75, 83, 2, 30, 20, 8]
    # s = [21, 97, 68, 38, 13, 30, 87, 70, 6, 43]
    # s = [98, 36, 21, 63, 77, 1, 25, 89, 88, 47, 10, 11, 77, 14, 17, 64, 44, 1, 55, 86] #ott
    # s = [33, 80, 1, 60, 25, 95, 19, 10, 66, 29, 21, 23, 58, 53, 55, 13, 27, 89, 99, 83] #not
    # print(s)
    # Leggo il file con le soluzioni generate da ga.py
    filename = 'solutions.txt'
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    out = extract_data(content)

    # Controllo accuratezza
    success = 0
    for s in range(len(out)):
        if find_part(out[s][0]):
            print('Sottoinsiemi ottimi.')
            if not out[s][2]:
                success += 1
        else:
            print('Non ottimi...')
            if out[s][2]:
                success += 1
        if out[s][2]:
            print('Non ottimi GA.\n')
        else:
            print('Sottoinsiemi ottimi GA!\n')

    success /= len(out)
    print("Il GA ha trovato la soluzione esatta nel", success, "dei", len(out), "casi.")


main()
