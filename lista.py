'''
Uso de listas en python
'''
from paquete.utilidades import encabezado, linea

def main():
    # crear lista de edades
    edades: list[int] = [21,17,23,19,21,23,17,14,15]
    
    linea(50)
    print(f'Cantidad de edades es {len(edades)}')
    linea(50)
    print(f'La tercera edad es {edades[2]} años')
    linea(50)
    print(f'La quinta edad es {edades[4]} años')
    linea(50)
    print(f'La ultima edad es {edades [- 1]} años')
    linea(50)
    edades.append(26)
    print(edades)
    linea(50)
    edades.extend([25,29,33,])
    print(edades)
    linea(50)
    porcion = edades[2:7]
    print(porcion)
    
    encabezado ('leer la lista de edades (for in)', 50)
    for edad in edades:
        print(f'La edad es {edad}')
    
    encabezado('leer lista de edades con indice',50)
    for i, edad in enumerate(edades):
        print(f'La edad {i} es {edad} años')
        
    encabezado('ver edades únicas', 50)
    edades_unicas = list (set (edades))
    print(f'Original : {edades}')
    edades_unicas.sort()
    print(f'Unicas: {edades_unicas}')
    
    encabezado('edades ordenadas ascendente', 50)
    edades_asc = sorted (edades)
    print(f'Original: {edades}')
    print(f'Ascendente: {edades_asc}')
    
    encabezado(' edades ordenadas descendente', 50)
    edades_des = sorted (edades, reverse=True)
    print(f'Original: {edades}')
    print(f'Descendente: {edades_des}')
    
    encabezado('ver mayores de edad', 50)
    mayores_edad = list( filter(lambda edad : edad >= 18, edades))
    print(f'Original: {edades}')
    mayores_edad.sort()
    print(f'Mayores de edad: {mayores_edad}')
    
    encabezado('ver menores de edad', 50)
    menores_edad = list( filter(lambda edad : edad < 18, edades))
    print(f'Original: {edades}')
    menores_asc = list (set(menores_edad))
    menores_asc.sort()
    print(f'Menores de edad: {menores_asc}')
    
main()