class Examen:
    def sum_lista(self, lista):
        if not isinstance(lista, list):  # Verifica si es una lista
            raise ValueError("No es una lista")
        for elemento in lista:
            if not isinstance(elemento, (int, float)):  # Verifica que cada elemento sea número
                raise ValueError("Todos los elementos de la lista deben ser números")
        return sum(lista)  # Retorna la suma total de la lista

    def count_vocal(self, cadena):
        if not isinstance(cadena, str):  # Asegura que el argumento es una cadena
            raise ValueError("El argumento debe ser una cadena")
        vocales = "aeiouAEIOU"  # Define las vocales
        count = 0  # Inicializa contador de vocales
        for char in cadena:
            if char in vocales:  # Comprueba si el carácter es una vocal
                count += 1  # Incrementa el contador
        return count  # Retorna el total de vocales encontradas

    def mult_matrix(self, m1, m2):
        if not (isinstance(m1, list) and isinstance(m2, list)):  # Verifica que ambas entradas son listas
            raise ValueError("Ambos argumentos deben ser listas")
        if len(m1[0]) != len(m2):  # Comprueba si las matrices son compatibles para multiplicar
            raise ValueError("No se pueden multiplicar")

        # Crea una matriz resultante del tamaño adecuado
        result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

        # Realiza la multiplicación de matrices
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j] += m1[i][k] * m2[k][j]  # Acumula el resultado de la multiplicación

        return result  # Retorna la matriz resultante

    def es_primo(self, n):
        if not isinstance(n, (int, float)):  # Verifica que el argumento es un número
            raise ValueError("El argumento debe ser un número")
        if isinstance(n, float) and not n.is_integer():  # No acepta números decimales
            raise ValueError("El número debe ser un entero")
        n = int(n)  # Convierte a entero
        if n <= 1:  # Números menores o iguales a 1 no son primos
            raise ValueError("El número debe ser mayor que 1")
        for i in range(2, n):  # Verifica si hay divisores
            if (n % i) == 0:  # Si hay un divisor, no es primo
                return False
        return True  # Retorna True si es primo

    def invertir_cadena(self, cadena):
        if not isinstance(cadena, str):  # Verifica que el argumento es una cadena
            raise ValueError("El argumento debe ser una cadena")
        cadena_invertida = ""  # Inicializa la cadena invertida
        for i in range(len(cadena) - 1, -1, -1):  # Itera desde el final hacia el inicio
            cadena_invertida += cadena[i]  # Agrega cada carácter a la cadena invertida
        return cadena_invertida  # Retorna la cadena invertida

    def eliminar_duplicados(self, lista):
        if not isinstance(lista, list):  # Verifica que es una lista
            raise ValueError("No es una lista")
        lista_sin_duplicados = []  # Inicializa la lista sin duplicados
        for elemento in lista:
            if elemento not in lista_sin_duplicados:  # Verifica si ya existe en la lista sin duplicados
                lista_sin_duplicados.append(elemento)  # Agrega si no está
        return lista_sin_duplicados  # Retorna la lista sin duplicados

    def tuples_to_dict(self, lista_tuplas):
        if not isinstance(lista_tuplas, list):  # Verifica que es una lista
            raise ValueError("El argumento debe ser una lista de tuplas")
        diccionario = {}  # Inicializa el diccionario
        for clave, valor in lista_tuplas:
            if not isinstance(clave, str):  # Las claves deben ser cadenas
                raise ValueError("Las claves deben ser cadenas")
            diccionario[clave] = valor  # Agrega la clave y el valor al diccionario
        return diccionario  # Retorna el diccionario creado

    def contar_palabras_unicas(self, texto):
        if not isinstance(texto, str):  # Verifica que es una cadena
            raise ValueError("El argumento debe ser una cadena")
        texto = texto.lower()  # Convierte a minúsculas para contar sin distinción
        
        # Elimina signos de puntuación
        for caracter in '.,!?:;\'"':
            texto = texto.replace(caracter, '')
        
        palabras = texto.split()  # Separa el texto en palabras
        palabras_unicas = []  # Inicializa lista de palabras únicas
        
        # Cuenta palabras únicas
        for palabra in palabras:
            if palabra not in palabras_unicas:  # Si no está ya en la lista
                palabras_unicas.append(palabra)  # Agrega la palabra
        return len(palabras_unicas)  # Retorna el número de palabras únicas

    def intercalar_listas(self, lista1, lista2):
        if not (isinstance(lista1, list) and isinstance(lista2, list)):  # Verifica que son listas
            raise ValueError("Ambos argumentos deben ser listas")
        lista_intercalada = []  # Inicializa la lista intercalada
        min_length = min(len(lista1), len(lista2))  # Encuentra la longitud mínima

        # Intercala elementos de ambas listas
        for i in range(min_length):
            lista_intercalada.append(lista1[i])  # Agrega de lista1
            lista_intercalada.append(lista2[i])  # Agrega de lista2
        
        # Agrega los elementos restantes de cada lista
        lista_intercalada.extend(lista1[min_length:])  # Agrega restos de lista1
        lista_intercalada.extend(lista2[min_length:])  # Agrega restos de lista2

        return lista_intercalada  # Retorna la lista intercalada

    def factorial(self, n):
        if not isinstance(n, int):  # Verifica que el argumento es un entero
            raise ValueError("El argumento debe ser un entero")
        if n < 0:  # No acepta negativos
            raise ValueError("El número debe ser un entero no negativo.")
        
        resultado = 1  # Inicializa resultado
        for i in range(1, n + 1):  # Calcula el factorial
            resultado *= i  # Multiplica cada número
        return resultado  # Retorna el factorial

# Valores de test para las funciones 

# Ejercicio 1: Suma de listas 
ej1=Examen()
ej11=[1,2,3]
ej12=[10,20,30]
ej13=[]



# Ejercicio 2: Contar vocales 
ej2=Examen()
ej21=("Hola Mundo")
ej22=("Alegria")
ej23=("AaEeeeIiiiuuU")


# Ejercicio 3: Multiplicar matrices
ej3 = Examen()
m31 = [[1, 2], [3, 4]]
m32 = [[5, 6], [7, 8]]  

# Ejercicio 4: Verificar números primos
ej4 = Examen()
ej41 = 7
ej42 = 7656
ej43 = 9887



# Ejercicio 5: Invertir cadenas
ej5 = Examen()
ej51 = "Alvaro"
ej52 = "Manzana"
ej53 = "Python"



# Ejercicio 6: Eliminar duplicados
ej6 = Examen()
ej61 = [1, 2, 2, 3, 4, 4,5,6,7,8,8,9,9]
ej62 = ["a", "b", "b", "c","d","j","j"]
ej63 = []



# Ejercicio 7: Convertir tuplas a diccionario
ej7 = Examen()
ej71 = [('A', 1), ('B', 2), ('C', 3)]
ej72 = [('D', 4), ('E', 5), ('F', 6)]
ej73 = [('G', 7), ('H', 8), ('I', 9)]


# Ejercicio 8: Contar palabras únicas
ej8 = Examen()
ej81 = "Hola, mundo. Hola a todos."
ej82 = "¡Adiós! Adiós, mundo."
ej83 = "Python es genial. Python es divertido."


# Ejercicio 9: Intercalar listas
ej9 = Examen()
ej91 = [1, 3, 5]
ej92 = [2, 4, 6, 8, 10]
ej93 = ['a', 'b', 'c']
ej94 = [1, 2, 3, 4]


# Ejercicio 10: Calcular el factorial
ej10 = Examen()
ej101 = 5
ej102 = 0
ej103 = 7



# Resultados finales 
print("Resutlados")

print(f"Ejercicio 1.1: {ej1.sum_lista(ej11)}")
print(f"Ejercicio 1.2: {ej1.sum_lista(ej12)}")
print(f"Ejercicio 1.3: {ej1.sum_lista(ej13)}")
print(f"Ejercicio 2.1: {ej21} tiene {ej2.count_vocal(ej21)} vocales")
print(f"Ejercicio 2.2: {ej22} tiene {ej2.count_vocal(ej22)} vocales")
print(f"Ejercicio 2.3: {ej22} tiene {ej2.count_vocal(ej23)} vocales")
print(f"Ejercicio 3.1: El resultado de la multiplicación de matrices es {ej3.mult_matrix(m31, m32)}") 
print(f"Ejercicio 4.1: {ej41} es primo: {ej4.es_primo(ej41)}")  
print(f"Ejercicio 4.2: {ej42} es primo: {ej4.es_primo(ej42)}")  
print(f"Ejercicio 4.3: {ej43} es primo: {ej4.es_primo(ej43)}")  
print(f"Ejercicio 5.1: La cadena '{ej51}' invertida es '{ej5.invertir_cadena(ej51)}'")  
print(f"Ejercicio 5.2: La cadena '{ej52}' invertida es '{ej5.invertir_cadena(ej52)}'")  
print(f"Ejercicio 5.3: La cadena '{ej53}' invertida es '{ej5.invertir_cadena(ej53)}'")  
print(f"Ejercicio 6.1: La lista sin duplicados es {ej6.eliminar_duplicados(ej61)}")  
print(f"Ejercicio 6.2: La lista sin duplicados es {ej6.eliminar_duplicados(ej62)}")  
print(f"Ejercicio 6.3: La lista sin duplicados es {ej6.eliminar_duplicados(ej63)}")  
print(f"Ejercicio 7.1: El diccionario es {ej7.tuples_to_dict(ej71)}")  
print(f"Ejercicio 7.2: El diccionario es {ej7.tuples_to_dict(ej72)}")  
print(f"Ejercicio 7.3: El diccionario es {ej7.tuples_to_dict(ej73)}") 
print(f"Ejercicio 8.1: El número de palabras únicas es {ej8.contar_palabras_unicas(ej81)}")  
print(f"Ejercicio 8.2: El número de palabras únicas es {ej8.contar_palabras_unicas(ej82)}")  
print(f"Ejercicio 8.3: El número de palabras únicas es {ej8.contar_palabras_unicas(ej83)}") 
print(f"Ejercicio 9.1: La lista intercalada es {ej9.intercalar_listas(ej91, ej92)}")  
print(f"Ejercicio 9.2: La lista intercalada es {ej9.intercalar_listas(ej92, ej91)}")  
print(f"Ejercicio 9.3: La lista intercalada es {ej9.intercalar_listas(ej93, ej94)}") 
print(f"Ejercicio 10.1: El factorial de {ej101} es {ej10.factorial(ej101)}")
print(f"Ejercicio 10.2: El factorial de {ej102} es {ej10.factorial(ej102)}")
print(f"Ejercicio 10.3: El factorial de {ej103} es {ej10.factorial(ej103)}")