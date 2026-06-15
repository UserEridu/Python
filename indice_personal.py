'''
Calculadora de índice de masa corporal (IMC) - Versión Personalizada
'''
from paquete.utilidades import encabezado, linea, leer_número_decimal

def main() -> None:
    encabezado('🌸 CALCULADORA DE IMC PERSONALIZADA 🌸', 55)
    print("✨ Bienvenido/a, vamos a conocer tu índice de masa corporal ✨\n")
    
    peso: float = leer_número_decimal('⚖️  Ingrese su peso (kg)')
    altura: float = leer_número_decimal('📏 Ingrese su altura (metros)')
    imc: float = 0.0
    imc = calcular_imc(peso, altura)
    
    linea(55)
    msj: str = '📊 TU ÍNDICE DE MASA CORPORAL ES'
    estado = status_imc(imc).upper()
    
    # Personalización del mensaje según el estado
    if estado == "BAJO PESO":
        icono = "⚠️"
    elif estado == "PESO NORMAL":
        icono = "✅"
    elif estado == "SOBREPESO":
        icono = "📈"
    else:
        icono = "🔴"
    
    print(f'{msj} {imc:.2f} ({icono} {estado} {icono})')
    linea(55)
    print("💡 Recuerda: El IMC es solo una referencia, consulta a un profesional de la salud.")
    linea(55)

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