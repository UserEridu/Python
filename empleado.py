'''
Datos del empleado usando un diccionario
'''
from paquete.utilidades import encabezado, linea
type mapa = dict[str, str | int| float]
def main() -> None:
    empleado: mapa = {
        'cedula': '24.125.788',
        'nombre' : 'maritza',
        'apellido': 'gutierrez',
        'edad' : 24,
        'sueldo' : 1245.66,
        
    }
    
    encabezado('ver datos de empleado',50)
    for key, value in empleado.items():
        print(f'{key.upper()}: {value}')

main()