'''
Funciones de utilidad
'''

def linea(largo: int) -> None:
    print('═' * largo)

def encabezado(titulo: str, largo: int) -> None:
    linea(largo)
    print(titulo.upper().center(largo))
    linea(largo)
    
def leer_número_entero(msj: str) -> int:
    while True:
        try:
            numero: int = int(input(f'{msj}: '))
            return numero
        except ValueError:
            print('Debe escribir un número entero...')
            
def leer_número_decimal(msj: str) -> float:
    while True:
        try:
            numero: float = float(input(f'{msj}: '))
            return numero
        except ValueError:
            print('Debe escribir un número...')