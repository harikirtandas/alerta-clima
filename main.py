# Menú 
while True:
    print('\n----- AlertasClima -----')
    print('------- OPCIONES -------')
    print('1. Consultar alertas climáticas por ciudad\n2. Ver historial de alertas \n3. Salir')
    
    opcion = input('Ingresa una opción: ').strip()
    
    if opcion == '3':
        print('\nGracias por utilizar nuestra app!\nFin.')
        break
    elif opcion == '1':
        
        pass
    elif opcion == '2':
        pass
    else:
        print('\nAlerta! La opción que ingresaste no es válida. Volvé a intentar! (del 1 al 3)')