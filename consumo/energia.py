import data.plantas as pl

def buscar_planta_ciudad(planta, ciudad):
    energia = []
    for h in pl.ce:
        if h == planta:
                newObject = pl.ce[h]
                for key in newObject:
                        if key == ciudad:
                                newObject2 = newObject[key]
                                energia.append(sum(newObject2['consumos'])) 
    return energia

#Registrar la ciudad al nuevo diccionario
#data significa el id con el q se va a llenar 
#ciudad es el nombre de la cuidad a ingresar
def ingresar_informacion(data,ciudad):
    newVinculo = {}
    newVinculo[ciudad] = data
    return newVinculo

#Permite registar las dos plantas que existen en nuestra data ejemplo:
# {'ciudad': '1qq', 'Planta1': ['Coca Codo Sinclair', 'Sopladora']}
def registrar_plantas(diccionario,plantas):
    energia = []
    for h in pl.ce :
            energia.append(h)
            diccionario[plantas] = energia
    return diccionario

#Permite registar plantas y ciudades existentes en nuestra data
def registrar_ciudades(diccionario,plantas):
    energia = []
    for h in pl.ce :
            newObject = pl.ce[h]
            for key in newObject :
                    newObject2 = newObject[key] #permite asignar la variable para acceder a las plantas
                    energia.append(sum(newObject2['consumos'])) #Permite obtener el total que se encuentra dentro del arreglo
                    diccionario[plantas] = energia #asigna las ciudades y consumos al diccionario que creamos
    return diccionario

#Consulta si la ciudad ingresada no exista dentro de mi data
def consultar_ciudad(nombre_ciudad):
    verifica_ciudad = True
    for h in pl.ce :
            newObject = pl.ce[h] #Accedo a Coca o Sopladora
            for key in newObject :
                    if key == nombre_ciudad : #Valdio la ciudad es igual a Coca o Sopladora
                            verifica_ciudad = False
    return verifica_ciudad

# Calcular el dinero recaudado de la region sierra

def TotalSierra(region):
    totalDinero = 0
    if region == "Sierra": 
        tarifaQuitoS = pl.ce["Sopladora"]["Quito"]["tarifa"]  
        tarifaLoja = pl.ce["Sopladora"]["Loja"]["tarifa"] 
        tarifaQuitoC = pl.ce["Coca Codo Sinclair"]["Quito"]["tarifa"]
        totalDinero = (tarifaQuitoS*12) + (tarifaQuitoC*12) + (tarifaLoja*12)
        return totalDinero

# Calcular por mes
def Meses(mes):
    if mes == 0:
        return "Enero"
    elif mes == 1:
        return "Febrero"
    elif mes == 2:
        return "Marzo"
    elif mes == 3:
        return "Abril"
    elif mes == 4:
        return "Mayo"
    elif mes == 5:
        return "Junio"
    elif mes == 6:
        return "Julio"
    elif mes == 7:
        return "Agosto"
    elif mes == 8:
        return "Septiembre"
    elif mes == 9:
        return "Octubre"
    elif mes == 10:
        return "Noviembre"
    elif mes == 11:
        return "Diciembre"

def CalcularMes(planta, ciudad, mes):
    totalMes = 0
    if planta == "Coca Codo Sinclair":
        consumo = pl.ce[planta][ciudad]["consumos"][mes]
        tarifa = pl.ce[planta][ciudad]["tarifa"]
        totalMes += consumo * tarifa   
    elif planta == "Sopladora":
        consumo = pl.ce[planta][ciudad]["consumos"][mes]
        tarifa = pl.ce[planta][ciudad]["tarifa"]
        totalMes += consumo * tarifa
    return totalMes