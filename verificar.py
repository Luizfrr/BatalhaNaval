def barco_em_y(linha, tamanho):
    
    if tamanho == 4:
        if linha > 6:
            return False
        else:
            return True
    
    if tamanho == 3:
        if linha >=7:
            return False
        else:
            return True
        
    if tamanho == 2:
        if linha > 8:
            return False
        else:
            return True
    
def barco_em_x(coluna, tamanho):
    
    if tamanho == 4:
        if coluna > 6:
            return False
        else:
            return True
    
    if tamanho == 3:
        if coluna >=7:
            return False
        else:
            return True
        
    if tamanho == 2:
        if coluna > 8:
            return False
        else:
            return True
    
def existe_barco(lista, linha, coluna):
    if lista[linha][coluna] == 0 or lista[linha][coluna] == 'x':
        return True
    else:
        return False