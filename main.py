import random
import statistics as stats
capMax=30
probmutatie=0.5
nrturnir=20
generatii=100
def generate_population(marime):
    populatie = []
    global capMax
    for i in range(marime):
        cromozom = [random.randint(0, 1) for _ in range(10)]
        fitness = calculate_fitness(cromozom , capMax)
        individ = (cromozom, fitness)
        populatie.append(individ)
    return populatie



def calculate_fitness(cromozom, weight_max):
    fitness=0
    weight=0
    Valori=[15,5,8,32,17,3,13,17,9,10]
    Greutati=[1,2,3,4,5,6,7,8,9,10]

    for j in range(10):
         if cromozom[j] == 1:
             fitness = fitness + Valori[j]
             weight = weight + Greutati[j]
    if weight > weight_max:
        fitness = 0
    # print("Greutati")
    # print(weight)
    return fitness

def tournament_selection(populatie, marime_turneu ):
    parinti = []
    turneu = random.sample(populatie, marime_turneu)
    turneu = sorted(turneu, key=lambda x: x[1], reverse=True)
    turneu2 = random.sample(populatie, marime_turneu)
    turneu2 = sorted(turneu2, key=lambda x: x[1], reverse=True)
    parinti.append(turneu[0])
    parinti.append(turneu2[0])
    return parinti

#incrucisare binara simpla
def crossover(parinte1, parinte2):
    punct_crossover = random.randint(1, len(parinte1)-1)
    copil1 = parinte1[:punct_crossover] + parinte2[punct_crossover:]
    copil2 = parinte2[:punct_crossover] + parinte1[punct_crossover:]
    return copil1, copil2

# Mutatie binara tare
def mutatie(cromozom, probabilitate_mutatie):
    for i in range(len(cromozom)):
        if random.random() < probabilitate_mutatie:
            cromozom[i] = 0 if cromozom[i] == 1 else 1
    return cromozom

def main():
    marime_populatie = 100
    populatie = generate_population(marime_populatie)
    parinti=[]
    for iq in range (generatii):
        # print("Populatie initiala:")
        # print(populatie)
        sumainit = 0
        for i in populatie:
             sumainit = sumainit + i[1]
        sumainit = sumainit / marime_populatie
        print("Medie ",(iq),"este",(sumainit))

        x4, minimul2 = populatie[0]
        x5, maximul2 = populatie[0]
        for i in range (len(populatie)):
            x6,variabila=populatie[i]
            if variabila < minimul2:
                minimul2 = variabila
            if variabila > maximul2:
                maximul2 = variabila
        print(populatie[1])
        dispersion = stats.stdev(populatie[1])
        print(dispersion)
        print("Dispersie ",(iq),"este",(dispersion))

        for i in range (0,nrturnir):
            parinti.append(tournament_selection(populatie, 50))
            x, y = parinti[i]
            x2,y2=crossover(x,y)
            x3=(mutatie(x2[0],probmutatie))
            #print(x3)
            fitness = calculate_fitness(x3, capMax)
            individ = (x3, fitness)

            populatie.append(individ)
            y3 = (mutatie(x2[0], probmutatie))
            #print(y3)
            fitness = calculate_fitness(y3, capMax)
            individ2 = (y3, fitness)

            populatie.append(individ2)

        populatie = sorted(populatie, key=lambda x: x[1], reverse=True)

        for i in range (len(populatie)-1,marime_populatie-1,-1):
            del populatie[i]

        # suma=0
        # for i in populatie:
        #     suma= (suma+i[1])
        # suma=suma/marime_populatie
        # print ("  ")
        # x4,minimul=populatie[0]
        # x5, maximul = populatie[0]
        # for i in range (len(populatie)):
        #     x6,variabila=populatie[i]
        #     if variabila < minimul:
        #         minimul = variabila
        #     if variabila > maximul:
        #         maximul = variabila
        #
        # dispersie=(maximul-minimul)/(maximul+minimul)

main()
