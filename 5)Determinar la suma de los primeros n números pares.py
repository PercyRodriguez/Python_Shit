#Determinar la suma de los primeros n numeros pares
n = int(input("Ingrese numero n:"))
i = 0
s = 0
while (i < n):
    i = i + 1
    p = 2 * i
    s = s + p

print("La suma de los" , n , "Nros pares es",s)
    
