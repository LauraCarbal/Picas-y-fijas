#Picas y fijas 
from random import sample
cifras =  4
fijas = 0
picas = 0
intentos = 0
Jugar = True
ganar = False 
def generar_numero_random ( cantidad_cifras):
    digitos = list(range(10)) #de 0 a 9
    numero_ramdon = sample(digitos, cantidad_cifras)
    return numero_ramdon

#función para obtener si tiene picas y fijas
def retornar_picas_fijas(numero_usuario):
    global fijas, picas
    fijas = 0
    picas = 0
    for digito in range(cifras): # 4 veces
        if numero_usuario[digito] in numero_clave: 
            if numero_usuario[digito] == numero_clave[digito]:
               fijas = fijas + 1
            else:
               picas += 1 
    print(f"tienes fijas: {fijas}, picas: {picas} y llevas {intentos} intentos" )

numero_clave = generar_numero_random(cifras)   
print(numero_clave)


while Jugar:
    numero_jugador = input(f"Ingrese un número de {cifras} cifras: ")
    cantidad_cifras_jugador = len(numero_jugador)
    if cantidad_cifras_jugador == 4:
        numero = list(numero_jugador)
        numero = [int(x) for x in numero]
        intentos = intentos + 1

        if numero == numero_clave:
            ganar = True
            Jugar = False
        else:
            retornar_picas_fijas(numero)
            if intentos == 12:
                print("Mal, este juego no es para ti")
                Jugar = False 
    else: 
        print("Debe ser un numero de 4 cifras")
        intentos = intentos + 1


#Función para mostrar mensaje
def retornar_mensaje(intentos, ganar):
    mensajes = [
        "Excelente, eres un maestro, estas fuera del alcance de los demás ",
        "Muy bueno, puedes ser un gran competidor",
        "Bien, estas progresando, debes buscar tus límites",
        "Regular, aún es largo el camino por recorrer"
    ]

    if ganar:
        if intentos <= 2:
            idx_mensaje = 0
        elif intentos <= 4:
            idx_mensaje = 1
        elif intentos <=8:
            idx_mensaje = 2
        else:
            idx_mensaje = 3

        mensaje = mensajes [idx_mensaje]
        return mensaje.format(intentos)

show_message = retornar_mensaje(intentos, ganar)
print(show_message) 


