dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

# FORMA CON SANGRIA FRANCESA
# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}
