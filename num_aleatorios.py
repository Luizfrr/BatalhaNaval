from datetime import datetime

def gerar():
    hora = datetime.now()
    milisegundos = hora.microsecond // 1000
    jogada = milisegundos % 10
    return jogada

