#Funcion para aplicar un descuento a un precio dado

def apply_discount(price,discount):
    # se utiliza isinstance que te permite verificar si una variable es de un tipo específico, en este caso se verifica si price y discount son números (int o float), y se usa el operador not para negar la condición y devolver un mensaje de error si no lo son.
    if not isinstance(price,(int,float)): 
        return "The price should be a number"
    if not isinstance(discount,(int,float)):
        return "The discount should be a number"
    # Se verifica si el precio es menor o igual a 0, y si el descuento es menor a 0 o mayor a 100, devolviendo un mensaje de error en caso de que alguna de estas condiciones se cumpla.
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    # Si todas las condiciones anteriores se cumplen, se calcula el precio con descuento aplicando la fórmula: precio - (precio * (descuento / 100)), y se devuelve el precio con descuento.
    else:
        discounted_price = price - (price * (discount / 100))
        return discounted_price
# se llama a la función apply_discount con un precio de 100 y un descuento de 20, y se imprime el resultado.
final_price = apply_discount(100, 20)
print(final_price)  # Output: 80.0SSS