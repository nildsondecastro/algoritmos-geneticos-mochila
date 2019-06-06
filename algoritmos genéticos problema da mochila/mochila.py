"""
==============================================================================================================
                             APLICAÇÃO DE ALGORITMOS GENÉTICOS NO PROBLEMA DA MOCHILA
==============================================================================================================
        Observação: As pastas low-dimensional e low-dimensional-optimum contêm os arquivos txt utilizados
        como base para execução do algoritmo, sendo assim, fundamentais para a execução do código.
        
        Nildson de Castro Pinheiro Mello
==============================================================================================================

==============================================================================================================
"""
import random
import csv
import numpy as np

def peso_individuo (indi, n):
    p=0
    for i in range(n):
        if(indi[i] == 1):
            p += peso[0][i]
    return p

def ajusta_peso(indi, n, wmax):
    while(peso_individuo(indi, n) > wmax):
        ponto = random.randint(0, n-1)
        while( indi[ponto] == 0):
            ponto = random.randint(0, n - 1)
        indi[ponto] = 0
    return indi

def individuo (n, wmax):
    indi = [random.randint(0,1)
            for i in range(n)]
    if (peso_individuo(indi, n) > wmax):
        indi = ajusta_peso(indi, n, wmax)
    return indi

def fitness (individuo, n):
    fit=0
    for i in range(n):
        if(individuo[i] == 1):
            fit += lucro[0][i]
    return fit

def populacao (tamanho, n, wmax):
    return [individuo(n, wmax)
            for i in range(tamanho)]

def mutacao (pop, taxa_mutacao, pressao, n, wmax):
    for i in range(len(pop)-pressao):
        if (random.random() <= taxa_mutacao):
            alterado = random.randint(0, n-1)
            if (pop[i][alterado] == 1):
                pop[i][alterado] = 0
            else:
                pop[i][alterado] = 1
        ajusta_peso(pop[i], n, wmax)
    return pop

def crossover (pop, selecionados, pressao, n, wmax):
    for i in range(len(pop)-pressao):
        corte = random.randint(1, n-1)
        metades = random.sample(selecionados,2)
        pop[i][:corte] = metades[0][:corte]
        pop[i][corte:] = metades[1][corte:]
        ajusta_peso(pop[i], n, wmax)
    return pop

def selecao (pop, pressao, n, wmax):
    indi=[(fitness(i, n),i) for i in pop]
    indi=[i[1] for i in sorted(indi)]
    pop=indi
    selecionados=indi[(len(indi)-pressao):]
    pop=crossover(pop,selecionados, pressao, n, wmax)
    return pop

def menu():
    while (True):
        print("==================== MENU =====================")
        print("Há 10 arquivos sobre o problema da mochila binária!")
        print("Digite um número de 1 a 10 para abrir um dos arquivos!")
        print("Digite 0 para encerrar!")
        print("digite sua opção:")
        try:
            a = int(input())
            return a
        except ValueError:
            print("Digite um número válido!")
            print("")

continua = 1
while(continua != 0):
    continua = menu()
    if ( continua < 0 or continua > 10):
        print("Opção Inválida!!!\n")
        continue
    elif (continua == 1):
        arquivo = csv.reader(open('low-dimensional/f1_l-d_kp_10_269.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f1_l-d_kp_10_269.txt'), delimiter=" ")

    elif (continua == 2):
        arquivo = csv.reader(open('low-dimensional/f2_l-d_kp_20_878.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f2_l-d_kp_20_878.txt'), delimiter=" ")

    elif (continua == 3):
        arquivo = csv.reader(open('low-dimensional/f3_l-d_kp_4_20.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f3_l-d_kp_4_20.txt'), delimiter=" ")

    elif (continua == 4):
        arquivo = csv.reader(open('low-dimensional/f4_l-d_kp_4_11.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f4_l-d_kp_4_11.txt'), delimiter=" ")

    elif (continua == 5):
        arquivo = csv.reader(open('low-dimensional/f5_l-d_kp_15_375.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f5_l-d_kp_15_375.txt'), delimiter=" ")

    elif (continua == 6):
        arquivo = csv.reader(open('low-dimensional/f6_l-d_kp_10_60.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f6_l-d_kp_10_60.txt'), delimiter=" ")

    elif (continua == 7):
        arquivo = csv.reader(open('low-dimensional/f7_l-d_kp_7_50.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f7_l-d_kp_7_50.txt'), delimiter=" ")

    elif (continua == 8):
        arquivo = csv.reader(open('low-dimensional/f8_l-d_kp_23_10000.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f8_l-d_kp_23_10000.txt'), delimiter=" ")

    elif (continua == 9):
        arquivo = csv.reader(open('low-dimensional/f9_l-d_kp_5_80.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f9_l-d_kp_5_80.txt'), delimiter=" ")

    elif (continua == 10):
        arquivo = csv.reader(open('low-dimensional/f10_l-d_kp_20_879.txt'), delimiter=" ")
        arquivo_otimo = csv.reader(open('low-dimensional-optimum/f10_l-d_kp_20_879.txt'), delimiter=" ")

    else:
        continue

    if (continua == 5):
        i = -1
        for linha in arquivo:
            if (i == -1):
                n = int(linha[0])
                wmax = int(linha[1])
                i += 1
                lucro = np.zeros((1, n), dtype=float)
                peso = np.zeros((1, n), dtype=float)
                continue
            lucro[0][i] = float(linha[0])
            peso[0][i] = float(linha[1])
            i += 1
        for j in arquivo_otimo:
            otimo = float(j[0])

    else:
        i = -1
        for linha in arquivo:
            if (i == -1):
                n = int(linha[0])
                wmax = int(linha[1])
                i += 1
                lucro = np.zeros((1, n), dtype=int)
                peso = np.zeros((1, n), dtype=int)
                continue
            lucro[0][i] = int(linha[0])
            peso[0][i] = int(linha[1])
            i += 1
        for j in arquivo_otimo:
            otimo = int(j[0])

    geracoes = 50
    pressao = 10
    taxa_mutacao = 0.3
    tamanho_populacao = 40
    pop=populacao(tamanho_populacao, n, wmax)

    print("Arquivo %d aberto. Informações do arquivo:" %(continua))
    print("número de itens = %d, peso máximo = %d" %(n, wmax))

    for i in range(geracoes):
        pop=selecao(pop, pressao, n, wmax)
        pop=mutacao(pop, taxa_mutacao, pressao, n, wmax)

    pop=[(fitness(i, n),i) for i in pop]
    pop=[i[1] for i in sorted(pop, reverse=True)]

    print("População final: ")
    print(pop)
    print("melhor individuo encontrado: \n%s" %(pop[0]))
    print("peso do melhor individuo encontrado: \n%s" %(peso_individuo(pop[0], n)))
    print("fitness do melhor individuo encontrado: \n%s" %(fitness(pop[0], n)))
    print("fitness do otimo do arquivo: \n%s\n" %(otimo))
