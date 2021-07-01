import os
from copy import deepcopy

def TestaessaPorra(teste, grade, l, c):
        for i in range (0, 9):
            if grade[i][c] == teste:
                teste = 0
        for j in range (0, 9):
            if grade[l][j] == teste:
                teste = 0
        if l < 3:
            for i in range (0, 3):
                if c < 3:
                    for j in range (0, 3):
                        if grade[i][j] == teste:
                            teste = 0
                elif c >= 3 and c < 6:
                    for j in range (3, 6):
                        if grade[i][j] == teste:
                            teste = 0
                else:
                    for j in range (6, 9):
                        if grade[i][j] == teste:
                            teste = 0
        elif l >= 3 and l < 6:
            for i in range (0, 3):
                if c < 3:
                    for j in range (0, 3):
                        if grade[i][j] == teste:
                            teste = 0
                elif c >= 3 and c < 6:
                    for j in range (3, 6):
                        if grade[i][j] == teste:
                            teste = 0
                else:
                    for j in range (6, 9):
                        if grade[i][j] == teste:
                            teste = 0
        else:
            for i in range (0, 3):
                if c < 3:
                    for j in range (0, 3):
                        if grade[i][j] == teste:
                            teste = 0
                elif c >= 3 and c < 6:
                    for j in range (3, 6):
                        if grade[i][j] == teste:
                            teste = 0
                else:
                    for j in range (6, 9):
                        if grade[i][j] == teste:
                            teste = 0
        if teste == 0:
            print("\nNúmero inválido!! rsrsrs burrinho")
            inutil = input("")
        else:
            grade[l][c] = teste
        return grade

def DesenhaessaPorra(grade):
    os.system('cls')
    print("********************* QUE COMEÇEM OS JOGOS *********************\n")
    print("     1  2  3    4  5  6    7  8  9")
    print("    ---------- ---------- ---------")
    for i in range (0, 9):
        for j in range (0, 9):
            if j == 0:
                naosei = str(i + 1)
                print(naosei + "  ", end = "| ")
                print(grade[i][j], end="  ")
            elif j == 8:
                print(grade[i][j], end=" |\n")
            else:
                print(grade[i][j], end="  ")
            if j == 2 or j == 5:
                    print("|", end=" ")
        if i == 2 or i == 5:
            print("   |----------|----------|---------|")
    print("    ---------- ---------- ---------\n")

def GanhouessaPorra(grade):
    teste = 1
    for i in range (0, 9):
        for j in range (0, 9):
            if grade[i][j] == 0:
                teste = 0
    return teste

def Sudokuzinho(gradinha):
    jogo = 1
    venceu = 1
    safado = 0
    gradeaux = deepcopy(gradinha)
    while jogo:
        DesenhaessaPorra(gradeaux)
        print("\n1 - Continuar\n2 - Reiniciar do inicio\n3 - sair")
        safado = int(input("Escolha uma das opções acima: "))
        if safado == 2:
            gradeaux = deepcopy(gradinha)
        elif safado == 3:
            break
        print("Escolha aonde você irá adicionar um número")
        linha = int(input("Digite o número da linha: ")) - 1 
        coluna = int(input("Digite o número da coluna: ")) - 1
        num = int(input("Digite o número a ser preenchido: "))
        if gradeaux[linha][coluna] == 0:
            gradeaux = TestaessaPorra(num, gradeaux, linha, coluna)
            venceu = GanhouessaPorra(gradeaux)
            if venceu:
                print("Parabéns caralhoooooo você é um grandissíssimo chupa rola vitorioso!!!!")
                inutil = input("")
                break
        else:
            print("Tu é burro mano ? escolhe outro lugar ai porra.")
            inutil = input("")


######################### MAIN #############################
grade1 = [[7,0,0,1,0,0,0,5,2], [9,1,0,5,8,0,0,6,0], [0,0,6,7,3,0,1,0,0], [0,0,0,0,0,0,9,2,5], [0,5,1,0,0,0,6,4,0], [2,4,9,0,0,0,0,0,0], [0,0,5,0,7,3,4,0,0], [0,6,0,0,1,5,0,8,7], [1,9,0,0,0,8,0,0,6]]
grade2 = [[0,0,2,0,0,0,0,0,9], [0,0,0,0,5,0,3,1,4], [5,0,0,0,8,0,0,0,0], [0,8,0,0,0,0,0,0,0], [0,9,0,6,0,8,2,3,7], [0,4,3,9,0,7,6,5,8], [0,1,0,7,2,4,0,6,0], [0,2,0,0,9,0,0,0,3], [0,5,7,0,0,1,4,0,0]]
grade3 = [[0,0,0,0,0,0,0,0,7], [8,4,0,6,0,7,0,5,0], [6,3,0,0,0,0,9,4,0], [5,1,0,3,0,0,8,0,6], [7,0,3,5,1,6,2,9,0], [9,0,0,0,7,4,5,0,0], [2,0,0,4,0,0,0,8,1], [0,0,0,7,8,0,0,0,9], [0,0,0,0,0,2,3,0,0]]
grade4 = [[0,0,0,0,4,0,0,0,0], [0,0,9,5,0,0,7,8,0], [0,0,0,0,8,0,3,2,5], [6,0,0,0,3,0,2,0,7], [0,1,3,9,2,6,0,4,0], [0,8,5,0,0,0,9,0,3], [0,0,1,0,6,7,4,5,9], [0,0,2,0,0,8,1,0,0], [0,0,0,4,0,0,0,0,0]]
grade5 = [[5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0], [0,9,8,0,0,0,0,6,0], [8,0,0,0,6,0,0,0,3], [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6], [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5], [0,0,0,0,8,0,0,7,9]]
op = 0
os.system('cls')
while op != 6:
    print("********************* Bem vindo ao Sudokuzinho *********************")
    print("\nEscolha uma das opções abaixo\n1 - Modalidade fácil\n2 - Modalidade menos fácil\n3 - Modalidade média\n4 - Modalidade difícil\n5 - O pica das galáxias\n6 - Sair\n")
    op = int(input("Resposta: "))
    if op == 1:
        Sudokuzinho(grade1)
    elif op == 2:
        Sudokuzinho(grade2)
    elif op == 3:
        Sudokuzinho(grade3)
    elif op == 4:
        Sudokuzinho(grade4)
    elif op == 5:
        Sudokuzinho(grade5)
    elif op == 6:
        print("Astalavista baby :)")
        inutil = input("")
    else:
        print("Saber ler não desgraça ? Escolhe um número certo ae")
        inutil = input("")
    os.system('cls')
#############################################################