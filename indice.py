'''
Calculadora de indice de masa corporal (IMC)
'''
from paquete.utilidades import encabezado, linea, leer_número_decimal

def main() -> None:
    encabezado('calculadora de indice de masa corporal', 50)
    peso: float = leer_número_decimal('Ingrese su peso (kg)')
    altura: float = leer_número_decimal('Ingrese su altura (mts)')
    imc: float = 0.0
    imc = calcular_imc(peso, altura)
    
    
    linea(50)
    msj: str = 'El indice de masa corporal es'
    print(f'{msj} {imc:.2f} ({status_imc(imc).upper()})')
    linea(50)
    
def calcular_imc(peso: float, altura: float) -> float:
    return peso / pow(altura, 2)

def status_imc(imc: float) -> str:
    if imc < 18.5:
        return 'bajo peso'
    elif imc >= 18.5 and imc < 24.99:
        return 'peso normal'
    elif imc >= 24.99 and imc < 29.99:
        return 'sobrepeso'
    else:
        return 'obesidad'
    
main()