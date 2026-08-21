def add_setting(diccionario, tupla):
      """
      Agrega un nuevo ajuste al diccionario de configuración.

         Args:
            diccionario (dict): Diccionario de configuración existente.
            tupla (tuple): Tupla que contiene la clave y el valor del nuevo ajuste.

      Returns:
         dict: Diccionario actualizado con el nuevo ajuste.
      """
      key, value = tupla
      key = key.lower()
      value = value.lower()

      if key in diccionario:
            return f'Setting {key} already exists! Cannot add a new setting with this name.'
      else:
            diccionario[key] = value
            return f'setting {key} added with value {value} successfully!'

def update_setting(diccionario, tupla):
      """
      Actualiza un ajuste existente en el diccionario de configuración.

         Args:
            diccionario (dict): Diccionario de configuración existente.
            tupla (tuple): Tupla que contiene la clave y el nuevo valor del ajuste.

      Returns:
         dict: Diccionario actualizado con el ajuste modificado.
      """
      key, value = tupla
      key = key.lower()
      value = value.lower()

      if key in diccionario:
            diccionario[key] = value
            return f'setting {key} updated to value {value} successfully!'
      else:
            return f'Setting {key} does not exist! Cannot update a non-existing setting.'

def delete_setting(diccionario, key):
      """
      Elimina un ajuste existente del diccionario de configuración.

         Args:
            diccionario (dict): Diccionario de configuración existente.
            key (str): Clave del ajuste que se desea eliminar.

      Returns:
         dict: Diccionario actualizado sin el ajuste eliminado.
      """
      key = key.lower()

      if key in diccionario:
            del diccionario[key]
            return f'setting {key} deleted successfully!'
      else:
            return 'Setting not found!'

def view_settings(diccionario):
      """
      Muestra todos los ajustes existentes en el diccionario de configuración.

         Args:
            diccionario (dict): Diccionario de configuración existente.

      Returns:
         dict: Diccionario con todos los ajustes existentes.
      """
      if diccionario == {}:
            return 'No settings available.'
      else:
            return 'Current user settings: \n' + '\n'.join(f'{key.capitalize()}: {value}' for key, value in diccionario.items())

test_settings = {
      'theme': 'dark',
      'notifications': 'enabled',
      'language': 'english'
      }  


#add_setting(test_settings, ('volume', 'high'))

print(view_settings(test_settings))
print(add_setting(test_settings, ('volume', 'high')))
print(view_settings(test_settings))
print(update_setting(test_settings, ('volume', 'medium')))
print(view_settings(test_settings))
print(delete_setting(test_settings, 'volume'))
print(view_settings(test_settings))