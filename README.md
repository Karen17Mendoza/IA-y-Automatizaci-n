# 🤖 IA y Automatización con N8N y Flask

Proyecto integrador de **Flask + OpenAI + N8N**, con automatización de mensajes usando un LLM para responder a través de flujos personalizados.

---

## ⚙️ Instalación y ejecución del servidor Flask

### 1. Clona el repositorio

```
git clone https://github.com/Karen17Mendoza/IA-y-Automatizaci-n.git
cd IA-y-Automatizaci-n
````

### 2. Crea un entorno virtual (opcional pero recomendado)

```
python -m venv venv

# En Mac/Linux
source venv/bin/activate

# En Windows
venv\Scripts\activate
```

### 3. Instala las dependencias

```
pip install -r requirements.txt
```

### 4. Ejecuta el servidor Flask

```
python app.py
```

Servidor corriendo en: `http://localhost:5000/`

---

## 🌐 Configuración de N8N

1. Instala y ejecuta N8N.
2. Crea un nuevo flujo.
3. Añade los siguientes nodos:

   * **Webhook**: Método POST, URL: `/mensaje`
   * **Function** (opcional): Para transformar datos si es necesario.
   * **HTTP Request**: Configurado para enviar al endpoint de Flask `http://localhost:5000/chat`
4. Activa el flujo y prueba enviando un mensaje.
   La respuesta será generada por el modelo de lenguaje (LLM) usando OpenAI.

---

## 🔐 Variables sensibles

Crea un archivo `.env` en la raíz del proyecto con tu API Key de OpenAI:

```
OPENAI_API_KEY=tu_api_key_aquí
```

En tu `app.py`, importa la variable de entorno:

```
import os
openai_key = os.environ['OPENAI_API_KEY']
```

---

## 📝 .gitignore sugerido

```
venv/
__pycache__/
.env
*.pyc
```

---

## ✅ Buenas prácticas

* No subas tu archivo `.env` ni credenciales a GitHub.
* Usa entornos virtuales para mantener tus dependencias organizadas.
* Haz commits frecuentes explicando cada cambio.
* Documenta tu flujo de trabajo en este `README.md`.

---

## 📦 Cómo subir a GitHub

```
git init
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin https://github.com/Karen17Mendoza/IA-y-Automatizaci-n.git
git push -u origin main
```

---

## 📸 Capturas 

![Flujo de trabajo ](/Imagenes/Imagen1.png)
![Respuesta ](/Imagenes/imagen2.png)

---

## 💡 Créditos


**Desarrollado por:** Karen Mendoza
**Integración IA y Automatización con N8N y Flask**

---

## 📬 Contacto

* GitHub: [@Karen17Mendoza](https://github.com/Karen17Mendoza)

---

## 🏁 Licencia

Karen Mendoza




