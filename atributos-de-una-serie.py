import pandas as pd 
#atributos de una serie
# s.size: devuelve el numero de elementos de la serie
serie2 = pd.Series([1,2,3])
tamanio_serie2 = serie2.size
print(tamanio_serie2)
# s.index: devuelve una lista con los nombres de las filas del data frame#
serie3 = pd.Series([1,2,3])
nombre_indice = serie3.index
print(nombre_indice)
#s.dtype:devuelve el tipo de datos de una serie 
serie4 = pd.Series([1,2,3])
tipoDeDato = serie4.dtype
print(tipoDeDato)