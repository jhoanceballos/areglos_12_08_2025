import numpy as np # np es un aleas para recortar el nombre de la numpy
vector = np.array([1, 2, 3, 4, 5]) # Creamos un vector de numpy
print(vector) # Imprimimos el vector
# quieros imprimir el tercer elemento del vector
print(vector[2]) # Imprimimos el tercer elemento del vector (indice 2)
"""los vectores son como las listas,no tienen un metodo
append() para agregar elementos
o tienen un metodo pop() para eliminar elementos, pero si tienen
metodo reshape() para cambiar su forma, adicionalmente despues
creado no se pueden cambiar de tamaño del vector """
vector1 =np.zeros(5) # Creamos un vector de ceros de tamaño 5
print(vector1) # Imprimimos el vector de ceros
vector2 = np.ones(5) # Creamos un vector de unos de tamaño 5
print(vector2) # Imprimimos el vector de unos  
vector3 =np.random(1,10) # creamos un vector de numeros aleatorios entre 1 al 10
print("range",vector3) # Imprimimos el vector de numeros rango
vector4 = np.arange(1, 10, 4) # Creamos un vector de numeros del 1 al 10 con paso de 2
print("arange", vector4) # Imprimimos el vector de numeros con paso de
vector5 = np.linspace(1, 10, 5) # Creamos un vector de numeros del 1 al 10 con 5 elementos
print("range", vector5) # Imprimimos el vector de numeros con 5
vector6 = np.random.randint(1, 10, 10) # Creamos un vector de numeros aleatorios enteros entre 1 al 10 con 10 elementos
print("randint", vector6) # Imprimimos el vector de numeros aleatorios enteros entre 1 al 10 con 10 
