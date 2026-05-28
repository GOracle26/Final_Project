"""
Módulo de servidor Flask para la aplicación de detección de emociones.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Ruta que recibe un texto, llama al detector de emociones
    y devuelve la respuesta formateada al cliente.
    """
    # Obtener el texto enviado por el cliente
    text_to_analyze = request.args.get('textToAnalyze')

    # Llamar a la función de detección de emociones
    response = emotion_detector(text_to_analyze)

    # Manejo de error: entrada en blanco o inválida
    if response['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"

    # Extraer valores del resultado
    anger            = response['anger']
    disgust          = response['disgust']
    fear             = response['fear']
    joy              = response['joy']
    sadness          = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Devolver respuesta formateada
    return (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} y 'sadness': {sadness}. "
        f"La emoción dominante es {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Ruta principal que renderiza la página de inicio de la aplicación.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    