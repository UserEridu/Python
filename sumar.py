""" 
Primer programa en python
programa que suma dos numeros enteros
"""
import paquete.utilidades as util

def main() -> None:
    util.encabezado('sumar números', 36)
    numero1: int = util.leer_número_entero('Ingresa primer número')
    numero2: int = util.leer_número_entero('Ingresa segundo número')
    resultado: int = 0
    
    resultado = numero1 + numero2
    
    util.linea(36)
    print(f'El resultado de la suma es {resultado}')
    util.linea(36)


main()

