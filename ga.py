import random


# Funzione che calcola il "costo" della partizione, dato il cromosoma e la lista dei valori
def partition(x, y):
    a = b = 0
    for i in range(len(x)):
        # Se nel cromosoma ho 0 all'i-esimo bit, metto nella partizione a l'i-esimo elemento
        if not x[i]:
            a += y[i]
        # Viceversa, con un bit a 1 metto nella partizione b l'i-esimo elemento
        else:
            b += y[i]
    # Ritorno il valore assoluto (più è vicino a 0 e migliore è la partizione)
    return abs(a - b)


def gen_population(s, n):
    population = []
    for i in range(0, s):
        indv = []
        # Ogni cromosoma contiene n bit (contenenti 0 o 1), pari alla dimensione della lista di interi
        for j in range(n):
            indv.append(random.randint(0, 1))
        population.append(indv)
    return population


# Funzione che esegue il crossover a un punto, dati i due genitori e il punto in questione
def crossover(g1, g2, p):
    f1 = g1[:p] + g2[p:]
    f2 = g1[p:] + g2[:p]
    # Ritorna i due figli della coppia
    return f1, f2


# Funzione per gestire la fase di mutazione
def mutate(g1, dim):
    gene = random.randrange(0, dim)
    # In base al numero random generato, inverto il bit a quella posizione nel cromosoma
    if g1[gene]:
        g1[gene] = 0
    else:
        g1[gene] = 1
    # Ritorno il cromosoma modificato
    return g1


# Funzione base dell'algoritmo genetico
def ga(problem, numbers, real_size, xover, mutation, generations):
    # Controllo che la grandezza della popolazione sia pari (per avere tutte coppie)
    size = real_size + real_size % 2
    population = gen_population(size, len(numbers))
    sum_numbers = sum(numbers)

    # Ciclo fino al numero di generazioni dato in input
    for i in range(1, generations + 1):
        print('Generazione: ', i)
        j = 0
        # Lista che raccoglie i risultati della funzione costo
        scores = []
        # SELECTION: Ciclo per ogni coppia della popolazione
        while j <= size - 2:
            # print(population[j])
            # print(population[j+1])
            # CROSSOVER: Genero un numero casuale che determina se la coppia avrà figli (probabilità alta)
            mating = random.random()
            if mating > xover:
                # Genero un secondo numero random per il punto del crossover
                point = random.randrange(0, size)
                figlio1, figlio2 = crossover(population[j], population[j+1], point)

                # MUTATION: Nuovamente genero un numero per eventuali mutazioni di uno o più figli (probabilità bassa)
                evolution1 = random.random()
                evolution2 = random.random()
                if evolution1 > mutation:
                    figlio1 = mutate(figlio1, len(numbers))
                if evolution2 > mutation:
                    figlio2 = mutate(figlio2, len(numbers))

                # Assegno alle seguenti variabili il valore della funzione costo
                oldscore1 = problem(population[j], numbers)
                newscore1 = problem(figlio1, numbers)
                oldscore2 = problem(population[j+1], numbers)
                newscore2 = problem(figlio2, numbers)

                # REPLACE: Controllo chi ha il valore minore (genitore o figlio) e lo inserisco in lista per la prossima generazione
                if newscore1 < oldscore1:
                    population[j] = figlio1
                    scores.append(newscore1)
                else:
                    scores.append(oldscore1)
                if newscore2 < oldscore2:
                    population[j+1] = figlio2
                    scores.append(newscore2)
                else:
                    scores.append(oldscore2)
            # Se i cromosomi non hanno avuto figli, passano direttamente loro alla prossima generazione
            else:
                scores.append(problem(population[j], numbers))
                scores.append(problem(population[j+1], numbers))
            j += 2

        print(scores)
        # Calcolo varie statistiche sulla fitness e stampo su terminale
        gen_avg = sum(scores) / size
        gen_best = min(scores)
        gen_sol = population[scores.index(min(scores))]
        print('> GENERATION AVERAGE:', gen_avg)
        print('> GENERATION BEST:', gen_best)
        print('> BEST SOLUTION:', gen_sol, '\n')

        # controllo se ho trovato la soluzione ottima: smetto di far evolvere la popolazione
        if gen_best == sum_numbers % 2:
            break

    return gen_sol, gen_best


def main():
    # Parametri per l'algoritmo genetico GA
    problem = partition
    dimensione = 50
    y = []
    for i in range(dimensione):
        y.append(random.randrange(1, 100))
    size = 30
    xover = 0.25
    mutation = 0.9
    generazioni = 100

    soluzione, valore = ga(problem, y, size, xover, mutation, generazioni)
    print(y)
    sol = (y, soluzione, valore)

    # Stampo su file per controllo
    with open('solutions.txt', 'a') as f:
        f.write(str(sol)+'\n')


ripeti = 100
while ripeti:
    main()
    ripeti -= 1
