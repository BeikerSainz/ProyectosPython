full_dot = '●'
empty_dot = '○'

# creacion de personaje
def create_character(nombre_personaje,fuerza,inteligencia,carisma):
    if not isinstance(nombre_personaje, str): # Se valida que el nombre del personaje sea una cadena de texto
        return "The character name should be a string"
    if nombre_personaje == "": # Se valida que el nombre del personaje no sea una cadena vacía
        return "The character should have a name"
    if len(nombre_personaje) > 10: #se valida que el nombre del personaje no sea mayor a 10 caracteres
        return "The character name is too long"
    if " " in nombre_personaje: # se valida que el nombre del personaje no contenga espacios
        return "The character name should not contain spaces"
    if not isinstance(fuerza, int) or not isinstance(inteligencia, int) or not isinstance(carisma, int): #se valida que los stats sean enteros
        return "All stats should be integers"
    if fuerza < 1 or inteligencia < 1 or carisma < 1: #se valida que los stats sean mayores a 0
        return "All stats should be no less than 1"
    if fuerza > 4 or inteligencia > 4 or carisma > 4: #se valida que los stats sean menores a 5
        return "All stats should be no more than 4"
    if fuerza + inteligencia + carisma != 7: #se valida que la suma de los stats sea igual a 7
        return "The character should start with 7 points."
    else:
        # Se crean las lineas de stats del personaje
        line_str = f'STR: {full_dot * fuerza}{empty_dot * (10 - fuerza)}\n'
        line_int = f'INT: {full_dot * inteligencia}{empty_dot * (10 - inteligencia)}\n'
        line_cha = f'CHA: {full_dot * carisma}{empty_dot * (10 - carisma)}'
        return f'Character: {nombre_personaje}\n{line_str}\n{line_int}\n{line_cha}'

new_personaje = create_character("Hero", 2, 3, 2)
print(new_personaje)