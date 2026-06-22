'''
Lista de ciudades agregagadas desde teclado
'''

from paquete.utilidades import encabezado, linea, leer_texto
from typing import Final
NRO_CIUDADES: Final = 6

def main () -> None:
    #declarar variables
    ciudades: list[str] = []
    avisos: tuple[str, ...] = (
        'primera',
        'segunda',
        'tercera',
        'cuarta',
        'quinta',
        'sexta',
    )
    ciudad: str = ''
    
    encabezado('ingreso de ciudades', 46)
    for i in range(NRO_CIUDADES):
        ciudad = leer_texto(f'Ingresa {avisos[i]} ciudad', 'ciudad')
        ciudades.append(ciudad)
        
        encabezado('mostrar ciudades', 46)
        for ciudad in ciudades:
            print(f'La ciudad es {ciudad.upper()}')

main()