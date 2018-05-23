#	Ecuación de 2® grado dado a,b,c determinar raíces: 〖ax〗^2+bx+c=0 
a = float(input("ingrese primer numero"))
b = float(input("ingrese segundo numero"))
c = float(input("ingrese tercer numero"))
if a == 0:
    print("a debe ser mayor a cero")
else:
    d = (b**2-4*a*c)
    if d == 0 :
        print("Las racies son iguales ", -b/(2*a))
    else:
        x1 = (-b + (d)**.5)/(2*a)
        x2 = (-b - (d)**.5)/(2*a)
        print ("Las raices son x1,x2:",x1,",",x2)

