def tiro(lista, linha, coluna):
    
    if lista[linha][coluna] == 0:
        print('Você acertou um barco')
        lista[linha][coluna] = 1
        return True
        
    elif lista[linha][coluna] == '~':
        print('Você não acertou nada')
        lista[linha][coluna] = 'x'
        return False
    
    elif lista[linha][coluna] == 1:
        print('Você acertou o mesmo barco'),
        return False

def barco_em_x(lista, linha, coluna, tamanho):
    linha += 1
    coluna += 1
    
    if tamanho == 4:
        lista[linha][coluna] = 0
        coluna += 1
        lista[linha][coluna] = 0
        coluna += 1
        lista[linha][coluna] = 0
        coluna += 1
        lista[linha][coluna] = 0
        
    if tamanho == 3:
        lista[linha][coluna] = 0
        coluna += 1
        lista[linha][coluna] = 0
        coluna += 1
        lista[linha][coluna] = 0
     
    if tamanho == 2:
        lista[linha][coluna] = 0
        coluna += 1
        lista[linha][coluna] = 0

    
def barco_em_y(lista, linha, coluna, tamanho):
    linha += 1
    coluna += 1
    
    if tamanho == 4:
        lista[linha][coluna] = 0
        linha += 1
        lista[linha][coluna] = 0
        linha += 1
        lista[linha][coluna] = 0
        linha += 1
        lista[linha][coluna] = 0
        
    if tamanho == 3:
        lista[linha][coluna] = 0
        linha += 1
        lista[linha][coluna] = 0
        linha += 1
        lista[linha][coluna] = 0
     
    if tamanho == 2:
        lista[linha][coluna] = 0
        linha += 1
        lista[linha][coluna] = 0

