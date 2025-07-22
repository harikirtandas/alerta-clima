from clima_api import clima_actual_weatherapi

historial = []  # Lista para guardar consultas (por ahora en memoria)

# Menú 
if __name__ == "__main__":
    while True:
        print('\n----- AlertasClima -----')
        print('------- OPCIONES -------')
        print('1. Consultar clima por ciudad')
        print('2. Ver historial de consultas')
        print('3. Salir')

        
        opcion = input('Ingresa una opción: ').strip()
        
        if opcion == '3':
            print('\nGracias por utilizar nuestra app!\nFin.')
            break
        
        elif opcion == '1':
            ciudad = input("Ingresá una ciudad: ").strip()
            resultado = clima_actual_weatherapi(ciudad)
            print(resultado)
            historial.append({'ciudad': ciudad, 'resultado': resultado})      
            
        elif opcion == '2':
            if not historial:
                print('\nNo hay consultas en el historial aún.')
            else:
                print('Historial de consultas:')
                for i, consulta in enumerate(historial, 1):
                    print(f"{i}. {consulta['ciudad']} -> {consulta['resultado']}")
        else:
            print('\nAlerta! La opción que ingresaste no es válida. Volvé a intentar! (del 1 al 3)')
            


    
    