edad = int(input("Ingrese su edad: "))

if edad > 0 and edad <= 12:
    print("Eres un niño.")
elif edad > 12 and edad <= 19:
    print("Eres un adolescente.")
elif edad > 19 and edad <= 39: 
    print("Eres un adulto joven.")
elif edad > 39 and edad <= 59:
    print("Eres un adulto.")
elif edad > 59 and edad <= 79:
    print("Eres un adulto mayor.")
else:
    print("Eres un anciano.")