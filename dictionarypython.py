#python diccionario
#dict
#trabaja con la estructura de tabla hash, se basan en
#pares de key-value, key puede ser de cualquier tipo
#mientras que values cualquier objeto
#los diccionarios se encierran en {}

dict1 = {} #vacio
dict2 = {"nombre": "Carlos", "codigo": "12345", "departamento": "Ventas"}

print(dict2)

#recorrer el dict2
for clave in dict2:
    print(clave, dict2[clave])

print(dict2.keys())
print(dict2.values())
