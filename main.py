import posicionar
import tabuleiros
import num_aleatorios
import verificar
import random

tabuleiro_pc = [[' ','0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['1','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['2','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['3','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['4','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['5','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['6','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['7','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['8','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['9','~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

tabuleiro_jogador = [[' ','0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['1','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['2','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['3','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['4','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['5','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['6','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['7','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['8','~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['9','~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

while True:
    
    escolha_menu = str(input('BATALHA NAVAL \n1 - Começar o jogo\n2 - Placar\n->'))
    if escolha_menu == '1':
        posicao_barco_um = str(input('Vertical ou horizontal?\n->')).lower()
        
        if posicao_barco_um == 'h':
            linha_pc = random.randint(0,9)
            coluna_pc = random.randint(0,9)          
            verificar.barco_em_x(coluna_pc, 4)
            
            while verificar.barco_em_x == False:
                coluna_pc = random.randint(0,9)
            posicionar.barco_em_x(tabuleiro_pc, linha_pc, coluna_pc, 4)
            tabuleiros.imprimir(tabuleiro_pc)
            
        elif posicao_barco_um == 'v':
            linha_pc = random.randint(0,9)
            coluna_pc = random.randint(0,9)          
            
            while verificar.barco_em_x == False:
                linha_pc = random.randint(0,9)
            posicionar.barco_em_y(tabuleiro_pc, linha_pc, coluna_pc, 4)
            tabuleiros.imprimir(tabuleiro_pc)
            
        contador_barco_dois = 0    
        while contador_barco_dois < 3:               
            posicao_barco_dois = str(input('B2Vertical ou horizontal?\n->')).lower()
            if posicao_barco_dois == 'h':
                linha_pc = random.randint(0,9)
                coluna_pc = random.randint(0,9)          
                verificar.barco_em_x(coluna_pc, 3)
                
                while verificar.barco_em_x == False:
                    if verificar.existe_barco(tabuleiro_pc, linha_pc, coluna_pc) == False:
                        coluna_pc = random.randint(0,9)
                    else:
                        continue
                posicionar.barco_em_x(tabuleiro_pc, linha_pc, coluna_pc, 3)
                tabuleiros.imprimir(tabuleiro_pc)
                
            elif posicao_barco_dois == 'v':
                linha_pc = random.randint(0,9)
                coluna_pc = random.randint(0,9)          
                
                while verificar.barco_em_y == False:
                    linha_pc = random.randint(0,9)
                posicionar.barco_em_y(tabuleiro_pc, linha_pc, coluna_pc, 3)
                tabuleiros.imprimir(tabuleiro_pc)
            contador_barco_dois += 1
        
        contador_barco_tres = 0
        while contador_barco_tres < 4:
            posicao_barco_tres = str(input('B3Vertical ou horizontal?\n->')).lower()
            if posicao_barco_tres == 'h':
                linha_pc = random.randint(0,9)
                coluna_pc = random.randint(0,9)          
                verificar.barco_em_x(coluna_pc, 2)
                
                while verificar.barco_em_x == False:
                    if verificar.existe_barco(tabuleiro_pc, linha_pc, coluna_pc) == False:
                        coluna_pc = random.randint(0,9)
                    else:
                        continue
                posicionar.barco_em_x(tabuleiro_pc, linha_pc, coluna_pc, 2)
                tabuleiros.imprimir(tabuleiro_pc)
                
            elif posicao_barco_dois == 'v':
                linha_pc = random.randint(0,9)
                coluna_pc = random.randint(0,9)          
                
                while verificar.barco_em_y == False:
                    linha_pc = random.randint(0,9)
                posicionar.barco_em_y(tabuleiro_pc, linha_pc, coluna_pc, 2)
                tabuleiros.imprimir(tabuleiro_pc)
            contador_barco_tres += 1
        
