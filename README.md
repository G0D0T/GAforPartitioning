# GAforPartitioning
Algoritmo genetico per l'ottimizzazione del Number Partitioning problem

L'algoritmo utilizzato è riassumibile con il seguente pseudocodice:

```
1. Inizializzo una popolazione di individui con le caratteristiche determinate dai parametri in input

2. While i < generazioni do
  3. For each coppia di individui in popolazione
    4. Eseguo il crossover a un punto e genero una nuova coppia di individui
    5. Eseguo la mutazione sui nuovi individui
    6. Seleziono i migliori individui che formeranno la popolazione della prossima generazione e salvo il migliore come best_solution
    
  7. If best_solution è soluzione ottima then
    8. Break
      Else
    9. incremento i e torno allo step #3
    
10. Return best_solution
```

Lo script ```ga.py``` restituisce in output (su terminale e su file) la soluzione trovata dall'algoritmo genetico per una lista di numeri generata casualmente. I parametri (modificabili a piacimento) che l'algoritmo va a valutare sono:


* ```dimensione``` ovvero la lunghezza della lista da partizionare;
* ```y``` il contenuto della lista (impostato per inizializzato con numeri random da 0 a 99);
* ```size``` quanti individui formano la popolazione;
* ```xover``` valore che stabilisce la probabilità che avvenga il crossover (compreso fra 0 e 1, più è basso è più è probabile);
* ```mutation``` probabilità che un individuo subisca una mutazione (compreso fra 0 e 1, più è basso è più è probabile);
* ```generazioni``` quante volte la popolazione viene fatta evolvere.


Per valutare quanto prodotto dall'algoritmo, eseguire lo script ```dpVerifier.py```, il quale legge in input il file ```solutions.txt``` (che contiene l'output di ```ga.py```) e stampa a schermo la percentuale di accuratezza insieme alla risposta per ogni riga del file.
