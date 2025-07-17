from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Cargar la API key desde el archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Crear app Flask
app = Flask(__name__)

# Ruta para recibir preguntas desde automatizaciones (como n8n o Zapier)
@app.route("/webhook", methods=["POST"])
def responder():
    data = request.json
    pregunta = data.get("pregunta")

    if not pregunta:
        return jsonify({"error": "No se recibió una pregunta válida"}), 400

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": pregunta}
            ],
            temperature=0.7,
            max_tokens=150
        )

        contenido = respuesta.choices[0].message.content.strip()
        return jsonify({"respuesta": contenido})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Iniciar servidor local en el puerto 3000
if __name__ == "__main__":
    app.run(port=3000)
