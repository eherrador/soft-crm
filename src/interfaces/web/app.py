import sys
import os

# Con la linea sys.path.append(...) estamos agregando el directorio raíz del proyecto al path de python
# para que pueda importar los módulos que necesite de nuestro proyecto.
# Ejemplo: si tu archivo app.py está en src/interfaces/web/app.py, entonces el  path del proyecto sería src/
# por lo que deberías agregar src/ al path de python.
# Si tu proyecto tiene una estructura diferente, asegurate de agregar el path correcto
# para que python pueda importar los módulos de tu proyecto sin problemas.
# Ejemplo:
# from interfaces.web import algun_modulo  # debe importar el modulo sin ningun problema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# En este caso, estamos importando el módulo chainlit
import chainlit as cl

@cl.on_message
async def on_message(message: cl.Message):
    response = f"Recibí tu mensaje: {message.content}"
    await cl.Message(content=response).send()
