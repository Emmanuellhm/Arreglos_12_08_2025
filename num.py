import numpy as np # np es un alias para simplificar en nombre numpy 
vector = np.array([1, 2, 3, 4, 5,]) #Creamos un vector de numpy

vector1 =np.zeros(5) #creamos un vector de 5 ceros 
print(vector1)
vector2 =np.ones(5) #cramos un vector de 5 unos
print(vector2)
vector3 =np.aranje(1,10) #creamos un vector de rango de 1 a 10
print("rango", vector3)
vector4 =np.linspace(1, 10, 5) #Creamos un vector de intervalos de 1, 10 y 5
print("linspace",vector4)
vector5 =np.random.rand(10) #Creamos un vector random de 10 numeros aleatoreos
print("random",vector5)
vector6 =np.random.randint(1, 10, 100) #Creamos un vector random de 1 a 100 numeros aleatorios
print("randint", vector6)