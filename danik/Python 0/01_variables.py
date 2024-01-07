#Variables
variable_str = "Hello World"
print(variable_str)

variable_int = 5
print(variable_int)

variable_float = 1.2
print(variable_float)

variable_bool = False
print(variable_bool)

print(variable_str, variable_int, variable_bool)

#Cambia el tipo de dato  / str() int() float()
variable_int_to_str = str(variable_int)
print(variable_int)
print(type(variable_int_to_str))

#Cambio de tipo int -> float
variable_int_to_float = float(variable_int)
print(variable_int)
print(type(variable_int))

#Cuenta cuantos caracteres tiene
print(len(variable_str))

#Variables en una sola linea
name, surname, alias, age = "Daniil", "Loktev", "dankelok", 17
print("Me llamo", name, surname, "y tengo:", age, "años", "pero todos me llaman", alias) #Combinar 'srt' con variables para crear este tipo de textos

#Inputs
name = input("Nombre? ") 
age = input("Edad? ")
print(name)
print(age)
