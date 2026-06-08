""" 
Primer programa en python
programa que suma dos numeros enteros
"""
import paquete.utilidades as util

def main() -> None:
    util.encabezado('sumar números', 36)
    numero1: int = util.leer_número_entero('Ingresa primer número')
    numero2: int = util.leer_número_entero('Ingresa segundo número')
    numero3: int = util.leer_número_entero('Ingresa tercer número')
    numero4: int = util.leer_número_entero('Ingresa cuarto número')
    resultado: int = 0
    
    resultado = calcular_suma(numero1, numero2, numero3, numero4)
    
    util.linea(36)
    print(f'El resultado de la suma es {resultado}')
    util.linea(36)
    
def calcular_suma(*numeros) -> int:
    return sum(numeros)


main()

