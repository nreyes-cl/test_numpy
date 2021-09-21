import numpy as np

a = np.array([1, 2, 3], dtype=np.int16)
print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

#Get dimensions
print(a.ndim) #1 un vector
print(b.ndim) #2 una matriz

#Get shape
print(a.shape) # es un vector por lo tanto muestra cantidad de columnas en este caso 3
print(b.shape) # es una matriz por lo tanto muestra cantidad de filas y columnas en este caso 2 y 3

#Get type
print(a.dtype) #int32 se puede cambiar 
print(b.dtype) #float64

#Get size
print(a.itemsize) #4 bytes
print(b.itemsize) #8 bytes

#Get total size
print(a.size) #3 cantidad total de elementos
print(b.size) #6 cantidad total de elementos

a = np.array([[1, 2, 3, 4, 5,6,7], [8, 9, 10, 11, 12,13,14]])
print(a)

#Get a specific element [row, column]
print(a[1,-2]) #13 
print(a[0,6]) #7

#Get a specific row
print(a[1,:]) #[8 9 10 11 12 13 14]

#Get a specific column
print(a[:,1]) #[2 9]

#Get a specific row and column 
print(a[0,1:6]) #[2 3 4 5 6]

#3d example
b = np.array([[[1, 2], [3,4]], [[5,6], [7,8]]])
print(b)

#get a specific element in 3d format (work outside in)
print(b[1,1,1]) #8

#replace element in 3d format
b[:,1,:] = [[9,9],[8,8]]
print(b)

#all 0s matrix
print(np.zeros((3,3)))

#all 1s matrix
print(np.ones((3,3)))

#any other number
print(np.full((3,3),5))

#any other number (full_like)
print(np.full_like(a,4))

#random decimal number
print(np.random.random((3,3)))#numeros aleatorios entre 0 y 1

#random interger number
print(np.random.randint(0,10,(3,3)))#entre 0 a 10 y una matriz de 3x3

#the identity matrix
#ambas funcionan de igual manera pero si quiero mantener la diagonal debo ocupar identity, en eye la diagonal puede terminar desviada
print(np.eye(4))
print(np.identity(4))

#repeat number of a matrix
arr= np.array([1,2,3])
r1=np.repeat(arr,3,axis=0)
print(r1)

#reshape matrix
output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1] = 9
print(z)
output[1:4,1:4] = z
print(output)