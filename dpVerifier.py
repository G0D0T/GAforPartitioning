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
    # s = [42, 99, 2, 94, 54, 50, 76, 53, 55, 42, 35, 44, 58, 98, 76, 80, 51, 41, 95, 23] #ott
    # s = [82, 24, 85, 94, 1, 89, 99, 75, 50, 8, 39, 33, 47, 8, 35, 49, 66, 96, 98, 1, 7, 72, 36, 53, 1, 13, 78, 2, 42, 91, 63, 57, 74, 99, 64, 22, 12, 80, 84, 50, 60, 83, 64, 65, 35, 74, 1, 73, 98, 26]
    # s = [75, 50, 2, 75, 74, 99, 38, 8, 8, 98, 47, 38, 8, 15, 6, 13, 82, 98, 54, 79, 6, 38, 27, 12, 33, 21, 4, 50, 28, 68, 37, 88, 43, 68, 64, 76, 69, 26, 57, 81, 16, 45, 1, 31, 82, 89, 83, 27, 79, 83]
    # s = [98, 36, 21, 63, 77, 1, 25, 89, 88, 47, 10, 11, 77, 14, 17, 64, 44, 1, 55, 86] #ott
    # s = [33, 80, 1, 60, 25, 95, 19, 10, 66, 29, 21, 23, 58, 53, 55, 13, 27, 89, 99, 83] #not
    # print(s)
    filename = 'solutions.txt'
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    out = extract_data(content)

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
