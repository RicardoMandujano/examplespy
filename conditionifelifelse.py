#Nested if condition
#if elif else
variable = 1000
if variable < 2000:
    print("menor de 2000")
    if variable == 1500:
        print("La cual es 1500")
    elif variable == 1000:
        print("La cual es 1000")
    elif variable == 500:
        print("La cual es 500")
elif variable < 50:
    print("Es menor 50")
else:
    print("No se puede encontrar expresion")

