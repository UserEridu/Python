'''
Juego de adivina el número
'''
import paquete.utilidades as util

def main() -> None:
    util.encabezado('Juego de adivina el número', 46)
    alias: str = util.leer_texto('ingresa tu alias', 'alias')
    util.linea
    #print(f'Alias: {alias}')
    secreto: int = 17
    número: int = 0
    
    jugar(secreto, número, alias)
    
def jugar(secreto: int, numero: int, alias: str) -> None:
    alias = alias.upper()
    msj: str = ''
    while numero  != secreto:
        numero = util.leer_número_entero('ingresa tu número')
        if numero > secreto:
            msj: str = 'Tu número es mayor que el secreto'
            print(f'{alias}, {msj}')
        elif numero < secreto:
              msj: str = 'Tu número es menor que el secreto'
              print(f'{alias}, {msj}')
        else:
            msj = 'Felicitaciones ganaste.'
            util.linea
            print(f'{alias}, {msj}')
            util.linea(46)


main()
