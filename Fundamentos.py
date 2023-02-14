def nuevoTema(tema):
    print("\n------", tema, "------\n")


nuevoTema("Operador Aritmetico")
print("Operador division entera (10//3):", 10//3)
print("Operador Potencia  (5 ** 3):", 5**3)
#Comentario de 1 linea
'''Comenetario 
Varias lineas'''
nuevoTema("Operadores Logicos")
print("Operador and (True and False): " , True and False)
print()
#Actividad: Imrpimir la tabla de verdad de los operadores Logicos.
nuevoTema("Tabla de Verdad")
print("AND")
print("Operador and (True and False): " , True and False)
print("Operador and (True and True): " , True and True)
print("Operador and (False and True): " , False and True)
print("Operador and (False and False): " , False and False)
print()
print("OR")
print("Operador or (True or False): " , True or False)
print("Operador and (True or True): " , True or True)
print("Operador and (False or True): " , False or True)
print("Operador and (False or False): " , False or False)
print()
print("NOT")
print("Operador or (not True): "  ,  not True)
print("Operador and (not Falseclear): "  ,  not False)
print()
nuevoTema("Operadores de comparacion")
print("2==3", 2==3)
print("2!=3", 2!=3)
print("2<3" , 2<3)
print("2<=3", 2<=3)
print("2>3" , 2>3 )
print("2>=3" , 2>=3)

nuevoTema("Variables")
variable1 = 10
_variable2 = 6.2456
Variable3 = "Angel"
dosPalabras = "Hola"
dos_palabras = "Daniel"

print(variable1, _variable2, Variable3,dosPalabras,dos_palabras)

a,b,c = 10, 5.16, "palabra"
print(a,b,c)

nuevoTema("Enteros")
w =123
x = 52293342
y = -231
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotantes")
x = 1297.50
print(x, type(x))
y = 0.5637939
print(y, type(y))

nuevoTema("Numeros Complejos")
x = -46j
y = 12 + 45j
z = 2j
print(x, type(x))
print(y , type(y))
print(z, type(z))

nuevoTema("Numeros Booleanos")
lis = [8]
print(lis,"es", bool(lis))
t = ()
print(t, "es", bool(t))
val = None #None equivale a null
print(val,"es", bool(val))

nuevoTema("Listas") #NO son arreglos 
a= [10,20.5, "Python list"]
print(a)
print(a[1])

nuevoTema("Tuplas")#Es inmutable(No se pueden cambiar los valores)
t = (25, "tupla", 1 + 4j, 3.1416)
print(t)
print(t[2])
print("t[1:4]:", t[1:4])