# Kata 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    texto = texto.replace(" ", "") # Con esto elimino los espacios de la cadena

    frecuencias = {} # En este apartado creo el diccionario

    for letra in texto:
        if letra in frecuencias:
            frecuencias[letra] += 1 # Si la letra ya está en el diccionario, aumenta el contador
        else:
            frecuencias[letra] = 1 # Si no está, se añade con valor inicial 1

    return frecuencias # Devuelve el diccionario resultante

print(frecuencia_letras("estoy practicando Katas"))

# Kata 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doblar(numero):
    return numero * 2  # Defino la función para que reciba un número y me devuelva el doble

numeros = [1, 2, 3, 4, 5]
resultado = list(map(doblar, numeros)) # Uso map() para aplicar la función "doblar" a cada número de la lista

print(resultado)

# Kata 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una 
# lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras(lista_palabras, objetivo):
    resultado = []

    for palabra in lista_palabras:
        if objetivo in palabra:
            resultado.append(palabra)

    return resultado

lista = ["libro", "manuscrito", "película", "cómic", "relato"]
print(buscar_palabras(lista, "pel"))


# Kata 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def restar(a, b):
    return a - b 

def diferencia_listas(lista1, lista2):
    resultado = list(map(restar, lista1, lista2))
    return resultado

lista_a = [10, 20, 30]
lista_b = [1, 2, 3]
print (diferencia_listas(lista_a, lista_b))


# Kata 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
#La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
#Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y 
# el estado.

def media_estado(lista, nota_aprobado=5):
    if len(lista) == 0:
        return (0, "suspenso") # Si la lista está vacía devuelvo 0 y suspenso
    
    suma = 0
    for numero in lista:
        suma += numero # Se acumulan todos los números

    media = suma / len(lista) # Calulo la media

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)

notas = [4, 6, 8, 10, 3]
print(media_estado(notas))
print(media_estado(notas, 7))


# Kata 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))


# kata 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def convertir_a_string(tupla):
    return str(tupla) # Convierto la tupla a string

def tuplas_a_strings(lista_tuplas):
    return list(map(convertir_a_string, lista_tuplas))

lista = [(1, 2), (3, 4), (5, 6)]
print(tuplas_a_strings(lista)) 


# Kata 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta 
#dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numero():
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        resultado = a / b
    except ValueError:
        print("Error: Debes introducir valores numéricos")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
    else:
        print("El resultado de la división es:", resultado)

dividir_numero()


# Kata 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas 
#mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la 
#función filter()

def permitido(mascota):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return mascota not in prohibidas # En este caso devuelve True si no está en la lista de prohibidas

def filtrar_mascotas(mascotas):
    return list(filter(permitido, mascotas))

lista = ["Pero", "Gato", "Mapache", "Canario"]
print(filtrar_mascotas(lista))


# Kata 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción 
#personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass # En este paso creo un excepción personalizada

def promedio_lista(lista):
    if len(lista) == 0:
        raise ListaVaciaError("La lista está vacía") # Lanzo el error si no hay elementos
    return sum(lista) / len(lista)

try:
    print(promedio_lista([5, 7, 9]))
    print(promedio_lista([]))
except ListaVaciaError as e:
    print("Error al calcular el promedio:", e)


# Kata 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera 
#del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango")
    except ValueError as e:
        print("Error:", e)
    else:
        print("Tu edad es:", edad)

pedir_edad()


# Kata 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud(palabra):
    return len(palabra)

def longitudes_palabras(frase):
    palabras = frase.split() # Con esto separo la frase en palabras
    return list(map(longitud, palabras))

print(longitudes_palabras("Practicado ejercicios Kata"))


# Kata 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y 
#minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayus_minus(letra):
    return (letra.upper(), letra.lower())

def letras_unicas(caracteres):
    resultado = []
    for letra in caracteres:
        if letra.lower() not in [l[1] for l in resultado]: # De esta forma se evitan los resultados
            resultado.append(mayus_minus(letra))
    return resultado

print(letras_unicas("aAbBcC"))


# Kata 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
#función filter()

def empieza_por(palabra, letra):
    return palabra.lower().startswith(letra.lower())

def palabras_por_letra(lista, letra):
    def comprobar(palabra):
        return empieza_por(palabra, letra)
    
    return list(filter(comprobar, lista))

palabras = ["Ana", "Pedro", "Alberto", "Lucia"]
print(palabras_por_letra(palabras, "A"))


# Kata 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda numero: numero + 3

def aplicar_sumar_tres(lista):
    return list(map(sumar_tres, lista))

print(aplicar_sumar_tres([1, 2, 3]))


# Kata 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las 
#palabras que sean más largas que n. Usa la función filter()

def mas_larga_que(palabra, n):
    return len(palabra) > n

def palabras_mas_largas(frase, n):
    lista_palabras = frase.split()
    def comprobar(palabra): 
        return mas_larga_que(palabra, n)
    return list(filter(comprobar, lista_palabras))

texto = "Estoy aprendiendo Python con katas"
print(palabras_mas_largas(texto, 5))


# Kata 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al 
#número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def juntar_digitos(a, b):
    return a * 10 + b # Con este paso multiplico el acumulador por 10 y sumo el siguiente dígito

def digitos_a_numero(lista_digitos):
    return reduce(juntar_digitos, lista_digitos)

print(digitos_a_numero([5, 7, 2]))


# Kata 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, 
#calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def es_sobresaliente(estudiante):
    return estudiante["calificacion"] >= 90

def filtrar_estudiantes(estudiantes):
    return list(filter(es_sobresaliente, estudiantes))

alumnos = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Marta", "edad": 21, "calificacion": 90}
]
print(filtrar_estudiantes(alumnos))


# Kata 19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

print(filtrar_impares([1, 2, 3, 4, 5, 6]))


# Kata 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def es_entero(elemento):
    return isinstance(elemento, int) # En este paso se comprueba si el elemento es de tipo int

def solo_enteros(lista):
    return list(filter(es_entero, lista))

mezcla = [1, "dos", 3, "cuatro", 5]
print(solo_enteros(mezcla))


# Kata 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda numero: numero ** 3 # Función lambda que devuelvo el cubo de un número

print(cubo(3))


# Kata 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce().

def multiplicar(a, b):
    return a * b

def producto_total(lista):
    return reduce(multiplicar, lista)

print(producto_total([2, 3, 4]))


# Kata 23. Concatena una lista de palabras.Usa la función reduce().

def concatenar(a, b):
    return a + b

def concatenar_palabras(lista):
    return reduce(concatenar, lista)

palabras = ["Hola", " ", "mundo", "!"]
print(concatenar_palabras(palabras))


# Kata 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

def restar(a, b):
    return a - b

def diferencia_total(lista):
    return reduce(restar, lista)

print(diferencia_total([10, 3, 2]))


# Kata 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)

print(contar_caracteres("Estoy aprendiendo Python"))


# Kata 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda a, b: a % b

print(resto(10, 3))


# Kata 27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    if len(lista) == 0:
        return 0 # Esto hace que si la lista esté vacía devuelva 0
    return sum(lista) / len(lista)

print(promedio([4, 6, 8]))


# Kata 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = [] # aquí se guardan los elementos que ya se han visto
    for elemento in lista:
        if elemento in vistos:
            return elemento # si ya estaba en la lista, es el primer duplicado
        else:
            vistos.append(elemento)
    return None # si no hay duplicados, se devuelve None

print(primer_duplicado([1, 2, 3, 2, 4, 5]))
print(primer_duplicado([1, 2, 3, 4, 5]))


# Kata 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', 
#excepto los últimos cuatro.

def enmascarar(texto):
    texto = str(texto)
    if len(texto) <= 4:
        return texto # si tiene 4 o menos caracteres no se enmascara
    else:
        return "#" * (len(texto) - 4) + texto[-4:] # enmascara todo menos los últimos 4
    
print(enmascarar("123456789"))


# Kata 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en 
#diferente orden.

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    return sorted(palabra1) == sorted(palabra2)

print(son_anagramas("roma", "amor"))
print(son_anagramas("hola", "halo"))
print(son_anagramas("hola", "adios"))


# Kata 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
#Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

class NombreEncontradoError(Exception):
    pass

def buscar_nombre():
    try:
        lista = input("Introduce nombres separados por comas: ").split(",")
        nombre = input("Introduce el nombre a buscar")
        lista = [n.strip() for n in lista]
        if nombre in lista:
            print("El nombre", nombre, "ha sido encontrado")
        else:
            raise NombreEncontradoError("El nombre no está en la lista")
        
    except NombreEncontradoError as e:
        print("Error:", e)

buscar_nombre()


# Kata 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el 
#puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(lista_empleados, nombre_completo):
    for empleado in lista_empleados:
        if empleado["nombre_completo"] == nombre_completo:
            return empleado["puesto"]
        
    return "La persona no trabaja aquí"

empleados = [{"nombre_completo": "Juan Pérez", "puesto": "Manager"}]
print(buscar_empleado(empleados, "Juan Pérez"))
print(buscar_empleado(empleados, "Ana López"))


# Kata 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda a, b: a + b, lista1, lista2))

print(sumar_listas([1, 2, 3], [4, 5, 6]))


# Kata 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular 
#la estructura del árbol.
#Código a seguir:
    #1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    #2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    #3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    #4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    #5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    #6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de 
    # lasmismas.
#Caso de uso:
    #1. Crear un árbol.
    #2. Hacer crecer el tronco del árbol una unidad.
    #3. Añadir una nueva rama al árbol.
    #4. Hacer crecer todas las ramas del árbol una unidad.
    #5. Añadir dos nuevas ramas al árbol.
    #6. Retirar la rama situada en la posición 2.
    #7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición Inválida")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas 
        }

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(1)
print(arbol.info_arbol())


# Kata 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
#Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#Código a seguir:
    #1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
    #2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    #3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
    # Lanzará un error en caso de no poder hacerse.
    #4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#Caso de uso:
    #1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    #2. Agregar 20 unidades de saldo de "Bob".
    #3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    #4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo and not self.cuenta_corriente:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo and not otro_usuario.cuenta_corriente:
            raise ValueError("Saldo insuficiente en el usuario origen")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
alicia.transferir_dinero(bob, 80)
alicia.retirar_dinero(50)
print("Saldo Alicia:", alicia.saldo)
print("Saldo Bob:", bob.saldo)


# Kata 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
#contar_palabras , reemplazar_palabras , eliminar_palabra . 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
#Código a seguir:
    #1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver 
    # un diccionario.
    #2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver 
    # el texto con el remplazo de palabras.
    #3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
    #4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos 
    # variable según la opción indicada.
#Caso de uso:
    #Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    resultado = [p for p in palabras if p != palabra]
    return " ".join(resultado)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"
    
print(procesar_texto("hola hola mundo", "contar")) 
print(procesar_texto("hola mundo", "reemplazar", "hola", "adiós"))  
print(procesar_texto("hola mundo cruel", "eliminar", "mundo"))  


# Kata 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia(hora):
    if 6 <= hora < 12:
        return "día"
    elif 12 <= hora < 18:
        return "tarde"
    elif 0 <= hora < 24:
        return "noche"
    else:
        return "Hora inválida"
    
print(momento_del_dia(10))
print(momento_del_dia(15))
print(momento_del_dia(22))
print(momento_del_dia(45))


# kata 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
    #- 0 - 69 insuficiente
    #- 70 - 79 bien
    #- 80 - 89 muy bien
    #- 90 - 100 excelente

def calificación_texto(nota):
    if nota < 0 or nota > 100:
        return "Nota inválida"
    elif nota <= 69:
        return "insuficiente"
    elif nota <= 79:
        return "bien"
    elif nota <= 89:
        return "muy bien"
    else:
        return "excelente"

print(calificación_texto(85))
print(calificación_texto(95))
print(calificación_texto(15))
print(calificación_texto(120))


# Kata 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) 
# y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def area(figura, datos):
    if figura == "rectangulo":
        return datos[0] * datos[1]
    elif figura == "circulo":
        return math.pi * datos[0] ** 2
    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2
    else:
        return "Figura no válida"
    
print(area("rectangulo", (4, 5)))
print(area("circulo", (3,)))
print(area("triangulo", (4,6)))


# Kata 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final 
# de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
    #1. Solicita al usuario que ingrese el precio original de un artículo.
    #2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    #3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    #4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). 
    # Por ejemplo, descuento de 15€.
    #5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
    #6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def precio_final():
    try:
        precio = float(input("Introduce el precio original: "))
        tiene_cupon = input("¿Tienes cupón de descuento? (Sí/No): ").lower().strip()

        if tiene_cupon in ["si", "sí"]:
            valor_cupon = float(input("Introduce el valor del cupón: "))
            if valor_cupon > 0:
                precio -= valor_cupon
                if precio < 0:
                    precio = 0

        print("El precio final es:", precio)

    except ValueError:
        print("Error: Debes introducir valores numéricos")

precio_final()