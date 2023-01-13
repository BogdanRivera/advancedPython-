"""
Para resolver este desafío, tu reto completar la función message_creator para que retorne un mensaje distinto dependiendo del artículo de tecnología que reciba como entrada.

La función message_creator recibirá como entrada un string que indica el artículo de tecnología. Luego, deberás evaluar el valor de este string y retornar un mensaje distinto dependiendo del valor que reciba.

La implementacion debe responder al siguiente comportamiento:

Si recibes una computadora, debes retornar el mensaje Con mi computadora puedo programar usando Python.
Si recibes un celular, debes retornar el mensaje "En mi celular puedo aprender usando la app de Platzi.
Si recibes un cable, debes retornar el mensaje ¡Hay un cable en mi bota!.
Y si no recibes ninguno de estos valores, debes retornar el mensaje Artículo no encontrado.
"""

articles = {
    "computadora":"Con mi computadora puedo programar usando Python",
    "celular":"En mi celular puedo aprender usando la app de Platzi",
    "cable":"¡Hay un cable en mi bota!"
  }

def message_creator(text):
  if text in articles.keys():
    return articles[text]
  else:
    return 'Artículo no encontrado'


text = 'computadora'
response = message_creator(text)
print(response)


