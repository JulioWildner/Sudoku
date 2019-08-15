import time # Importar modulo time para usar time.sleep() para 2 segundos depois de exibir uma mensagem de erro.
def Tudo(): # def Tudo() que contem todo o jogo, para reiniciá-lo se quiser.
    print('IIIIIIIIII  II      II  IIIIII     IIIIIIIIII  II     II  II      II')#------------\
    print('II          II      II  II    II   II      II  II    II   II      II')#-------------\
    print('II          II      II  II     II  II      II  II   II    II      II')#--------------\
    print('IIIIIIIIII  II      II  II     II  II      II  IIIIII     II      II')#---------------- Print`s para titulo legal e informações a respeito do sudoku.
    print('        II  II      II  II     II  II      II  II   II    II      II')#---------------/
    print('        II  II      II  II    II   II      II  II    II   II      II')#--------------/
    print('IIIIIIIIII  IIIIIIIIII  IIIIII     IIIIIIIIII  II     II  IIIIIIIIII\n')#-----------/
    print('>> O objetivo do jogo é colocar números de 1 a 9 em cada um dos locais\nvazios numa grade de 9x9, constituída por 3x3 subgrade(chamada região).\n')
    print('>> O jogo contem algumas pistas, que são uns números inseridos em alguns locais,\npermitindo uma dedução dos numeros dos locais vazios. \n\n>> Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9.\n')
    print('*Resolve-lo requer lógica e um pouco de tempo. Divirta-se!\n')# ------------------/
    su = [['9',' ',' ','4',' ',' ',' ',' ','1'],#-\
          [' ','7','6',' ','2',' ',' ',' ',' '],#--\
          ['2',' ','1','9',' ',' ',' ',' ','3'],#---\
          [' ',' ',' ',' ',' ','2','4',' ',' '],#----\
          ['6',' ','9','3',' ',' ','7',' ',' '],#------ lista su que compõe o tabuleiro do jogo (sudoku com tabuleiro fixo, nao se altera, é sempre o mesmo).
          ['4',' ',' ','7',' ','5','8',' ',' '],#----/
          [' ','9',' ','5','3',' ','6','8',' '],#---/
          ['3','5','7',' ','6',' ',' ',' ',' '],#--/
          [' ',' ',' ',' ','1',' ',' ','9',' ']]#-/
    def win(): #-----------------------------------------------\
        du = [['9','3','8','4','5','6','2','7','1'],#----------|
              ['5','7','6','1','2','3','9','4','8'],#----------|
              ['2','4','1','9','7','8','5','6','3'],#----------|
              ['7','1','5','6','8','2','4','3','9'],#----------|
              ['6','8','9','3','4','1','7','5','2'],#----------|
              ['4','2','3','7','9','5','8','1','6'],#----------|
              ['1','9','2','5','3','4','6','8','7'],#----------|
              ['3','5','7','8','6','9','1','2','4'],#----------|
              ['8','6','4','2','1','7','3','9','5']]#----------|
        if su == du:                                #--------------- Verifica se o jogador ganhou e se quer reinciar o tabuleiro.
            print('>>>--------------<<<')           #----------|     Caso o tabuleiro estiver completo e nao aparecer mensagem de vitória,
            print('>>> Você ganhou! <<<')           #----------|     significa que algum número inserido no tabuleiro não está em seu local correto.
            print('>>>--------------<<<\n')         #----------|
            while True:                             #----------|
                x = str(input('Reiniciar tabuleiro?(S/N): '))#-|
                x = x.lower()                       #----------|
                if x == 's':                        #----------|
                    Tudo()                          #----------|
                elif x == 'n':                      #----------|
                    exit()                          #----------|
                else:                               #----------|
                    print('Entrada Inválida')#-----------------/
    def tabu():#-----------------------------------------------------------------------------------------------------------------------------\
        print('\n                  Colunas\n     X-----------------------------------X         ')                                             #|
        print('  x--| A | B | C | D | E | F | G | H | I |\n  |  |-----------------------------------|')                                     #|
        print('  |1 |',su[0][0],' ',su[0][1],' ',su[0][2],'|',su[0][3],' ',su[0][4],' ',su[0][5],'|',su[0][6],' ',su[0][7],' ',su[0][8],'|')#|
        print('  |2 |',su[1][0],' ',su[1][1],' ',su[1][2],'|',su[1][3],' ',su[1][4],' ',su[1][5],'|',su[1][6],' ',su[1][7],' ',su[1][8],'|')#|
        print('  |3 |',su[2][0],' ',su[2][1],' ',su[2][2],'|',su[2][3],' ',su[2][4],' ',su[2][5],'|',su[2][6],' ',su[2][7],' ',su[2][8],'|')#|
        print('L |--|-----------------------------------|')                                                                                 #|
        print('i |4 |',su[3][0],' ',su[3][1],' ',su[3][2],'|',su[3][3],' ',su[3][4],' ',su[3][5],'|',su[3][6],' ',su[3][7],' ',su[3][8],'|')#--- def tabu() printa o tabuleiro.
        print('n |5 |',su[4][0],' ',su[4][1],' ',su[4][2],'|',su[4][3],' ',su[4][4],' ',su[4][5],'|',su[4][6],' ',su[4][7],' ',su[4][8],'|')#|
        print('h |6 |',su[5][0],' ',su[5][1],' ',su[5][2],'|',su[5][3],' ',su[5][4],' ',su[5][5],'|',su[5][6],' ',su[5][7],' ',su[5][8],'|')#|
        print('a |--|-----------------------------------|')                                                                                 #|
        print('s |7 |',su[6][0],' ',su[6][1],' ',su[6][2],'|',su[6][3],' ',su[6][4],' ',su[6][5],'|',su[6][6],' ',su[6][7],' ',su[6][8],'|')#|
        print('  |8 |',su[7][0],' ',su[7][1],' ',su[7][2],'|',su[7][3],' ',su[7][4],' ',su[7][5],'|',su[7][6],' ',su[7][7],' ',su[7][8],'|')#|
        print('  |9 |',su[8][0],' ',su[8][1],' ',su[8][2],'|',su[8][3],' ',su[8][4],' ',su[8][5],'|',su[8][6],' ',su[8][7],' ',su[8][8],'|')#|
        print('  x--X-----------------------------------X\n')#-------------------------------------------------------------------------------/
    while True:#----------------------------------------------------------------------------------------------------------
        tabu()                                                                                                           #|
        win()                                                                                                            #|
        cont = True                                                                                                      #|
        while cont:                                                                                                      #|
            x = str(input('>> Na Linha(1-9): '))                                                                         #|
            if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9': #|
                cont = False                                                                                             #|
            else:                                                                                                        #|
                print('A linha deve ser de 1 a 9')                                                                       #----- Para inserir em qual local vazio na linha e coluna do tabuleiro colocar o número digitado.
        while cont == False:                                                                                             #|     Também com avisos caso a entrada for inválida.
            y = input('>> Em Coluna: ')                                                                                  #|
            y = y.lower()                                                                                                #|
            if y == 'a' or y == 'b' or y == 'c' or y == 'd' or y == 'e' or y == 'f' or y == 'g' or y == 'h' or y == 'i': #|
                cont = True                                                                                              #|
            else:                                                                                                        #|
                print('A coluna deve ser de A a I')                                                                      #|
        while cont:                                                                                                      #|
            z = input('>> Insere numero(1-9): ')                                                                         #|
            if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9': #|
                cont = False                                                                                             #|
            else:                                                                                                        #|
                print('O numero deve ser de 1 a 9')#----------------------------------------------------------------------/
        if x == '1':#-------------------------------------------------------------\                                                                                 
            if y == 'b':                                                         #|
                su[0][1] = z                                                     #|
            elif y == 'c':                                                       #|
                su[0][2] = z                                                     #|
            elif y == 'e':                                                       #|
                su[0][4] = z                                                     #|
            elif y == 'f':                                                       #|
                su[0][5] = z                                                     #|
            elif y == 'g':                                                       #|
                su[0][6] = z                                                     #|
            elif y == 'h':                                                       #--- Vários e vários if`s. Em geral, eles vão inserir o número digitado na posição informada do tabuleiro, desde que seja uma posição
                su[0][7] = z                                                     #|   que não tenha um número fixo do tabuleiro nela. 
            elif y == 'a' or y == 'd' or y == 'i':                               #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '2':                                                           #|
            if y == 'a':                                                         #|
                su[1][0] = z                                                     #|
            elif y == 'd':                                                       #|
                su[1][3] = z                                                     #|
            elif y == 'f':                                                       #|
                su[1][5] = z                                                     #|
            elif y == 'g':                                                       #|
                su[1][6] = z                                                     #|
            elif y == 'h':                                                       #|
                su[1][7] = z                                                     #|
            elif y == 'i':                                                       #|
                su[1][8] = z                                                     #|
            elif y == 'b' or y == 'c' or y == 'e':                               #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '3':                                                           #|
            if y == 'b':                                                         #|
                su[2][1] = z                                                     #|
            elif y == 'e':                                                       #|
                su[2][4] = z                                                     #|
            elif y == 'f':                                                       #|
                su[2][5] = z                                                     #|
            elif y == 'g':                                                       #|
                su[2][6] = z                                                     #|
            elif y == 'h':                                                       #|
                su[2][7] = z                                                     #|
            elif y == 'a' or y == 'c' or y == 'd' or y == 'i':                   #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '4':                                                           #|
            if y == 'a':                                                         #|
                su[3][0] = z                                                     #|
            elif y == 'b':                                                       #|
                su[3][1] = z                                                     #|
            elif y == 'c':                                                       #|
                su[3][2] = z                                                     #|
            elif y == 'd':                                                       #|
                su[3][3] = z                                                     #|
            elif y == 'e':                                                       #|                                  
                su[3][4] = z                                                     #|
            elif y == 'h':                                                       #|
                su[3][7] = z                                                     #|
            elif y == 'i':                                                       #|
                su[3][8] = z                                                     #|
            elif y == 'f' or y == 'g':                                           #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '5':                                                           #|
            if y == 'b':                                                         #|
                su[4][1] = z                                                     #|
            elif y == 'e':                                                       #|
                su[4][4] = z                                                     #|
            elif y == 'f':                                                       #|
                su[4][5] = z                                                     #|
            elif y == 'h':                                                       #|
                su[4][7] = z                                                     #|
            elif y == 'i':                                                       #|
                su[4][8] = z                                                     #|
            elif y == 'a' or y == 'c' or y == 'd' or y == 'g':                   #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '6':                                                           #|
            if y == 'b':                                                         #|
                su[5][1] = z                                                     #|
            elif y == 'c':                                                       #|
                su[5][2] = z                                                     #|
            elif y == 'e':                                                       #|
                su[5][4] = z                                                     #|
            elif y == 'h':                                                       #|
                su[5][7] = z                                                     #|
            elif y == 'i':                                                       #|
                su[5][8] = z                                                     #|
            elif y == 'a' or y == 'd' or y == 'f' or y == 'g':                   #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '7':                                                           #|
            if y == 'a':                                                         #|
                su[6][0] = z                                                     #|
            elif y == 'c':                                                       #|
                su[6][2] = z                                                     #|
            elif y == 'f':                                                       #|
                su[6][5] = z                                                     #|
            elif y == 'i':                                                       #|
                su[6][8] = z                                                     #|
            elif y == 'b' or y == 'd' or y == 'e' or y == 'g' or y == 'h':       #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '8':                                                           #|
            if y == 'd':                                                         #|
                su[7][3] = z                                                     #|
            elif y == 'f':                                                       #|
                su[7][5] = z                                                     #|
            elif y == 'g':                                                       #|
                su[7][6] = z                                                     #|
            elif y == 'h':                                                       #|
                su[7][7] = z                                                     #|
            elif y == 'i':                                                       #|
                su[7][8] = z                                                     #|
            elif y == 'a' or y == 'b' or y == 'c' or y == 'e':                   #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)                                                    #|
        elif x == '9':                                                           #|
            if y == 'a':                                                         #|
                su[8][0] = z                                                     #|
            elif y == 'b':                                                       #|
                su[8][1] = z                                                     #|
            elif y == 'c':                                                       #|
                su[8][2] = z                                                     #|
            elif y == 'd':                                                       #|
                su[8][3] = z                                                     #|
            elif y == 'f':                                                       #|
                su[8][5] = z                                                     #|
            elif y == 'g':                                                       #|
                su[8][6] = z                                                     #|
            elif y == 'i':                                                       #|
                su[8][8] = z                                                     #|
            elif y == 'e' or y == 'h':                                           #|
                print('Esta posição não pode ser alterada.\n')                   #|
                time.sleep(2)#---------------------------------------------------#/                                               
Tudo() #Chama a def Tudo(), iniciando todo o jogo.
