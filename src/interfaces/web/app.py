import chainlit as cl

@cl.on_message
async def on_message(message: cl.Message):
    response = f"Recibí tu mensaje: {message.content}"
    await cl.Message(content=response).send()
