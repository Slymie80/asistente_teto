from piper import PiperVoice
import io
import wave

MODEL_PATH = "app/models/piper/es_MX-ald-medium.onnx"

voice = PiperVoice.load(MODEL_PATH)

def sintetizar_texto(texto: str) -> bytes:
    """
    Sintetiza un texto en audio utilizando el modelo de voz especificado.

    Args:
        texto (str): El texto a sintetizar.

    Returns:
        bytes: El audio sintetizado en formato WAV.
    """


    buffer = io.BytesIO()
    with wave.open(buffer, 'wb') as wav_file:
        voice.synthesize_wav(texto,wav_file)
    return buffer.getvalue()
