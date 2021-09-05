import consumo.energia as cs
import data.plantas as pl

op = -1

while op != 0:
    print()
    print('(1)Mostrar consumo de energia por planta y ciudad')
    print('(2)Mostrar megavatios de cada ciudad existente')
    print('(3)Mostrar informacion del consumo de cada region')
    print('(4)Mostrar consumo de energia por mes del año')
    print('(5)Salir')
    print()
    op = int(input('Escoja una opcion: '))
    
    print()
    if op == 1 :
        planta = input("Ingresar planta: ")
        ciudad = input("Ingresar ciudad: ")
        plantas = cs.buscar_planta_ciudad(planta, ciudad)   
        print()    
        print('Total de Megavatios de consumo' + str(plantas))
    elif op == 2:
        newVinculo = {}
        #capitalize sirve para colocar la primera letra en mayuscula
        ciudad = input("Ingrese el nombre de una ciudad: ")
        verifica_ciudad = cs.consultar_ciudad(ciudad.capitalize())
        if(verifica_ciudad):
            newVinculo = cs.ingresar_informacion(ciudad,'ciudad')
            print('La ciudad Ingresada fue:' + str(newVinculo))
            #newVinculo = cs.registrar_plantas(newVinculo, 'Planta1')
            newVinculo = cs.registrar_ciudades(newVinculo, 'Coca Codo Sinclair')
            newVinculo = cs.registrar_ciudades(newVinculo, 'Sopladora')
            print('La Plantas con el total cosumido por ciudad son:' + str(newVinculo))
        else:
            print('La ciudad que ingresaste ya se encuentra registrada')

    elif op == 3:
        luz = input("Ingrese el nombre de una region: ")
        energia = cs.TotalSierra(luz)
        if luz == "Sierra":
           print("Total de dinero recaudado de la region",luz+":", "$",energia)
        else:
            print("Región no disponible")

    elif op == 4:
        planta = str(input("Ingresar planta: "))
        ciudad = str(input("Ingrese una ciudad de acuerdo a la planta de energía: "))
        mes = int(input("Ingrese el número del mes: "))
        total = cs.CalcularMes(planta, ciudad, mes)
        print("Total de consumo por mes:", total)

    elif op == 5:
        print("Hasta la próxima...\nPrograma finalizado.")
        break
    else: 
        print("Opción no válida!")