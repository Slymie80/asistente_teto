import unittest
from unittest.mock import Mock, patch

import requests

from app.conversation.service import ConversationService


class TestConversationService(unittest.TestCase):
    @patch("app.conversation.service.requests.post")
    def test_responder_exitoso(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "response": "Hola, ¿cómo estás?"
        }

        mock_post.return_value = mock_response

        servicio = ConversationService()

        resultado = servicio.responder("hola teto")

        self.assertEqual(
            resultado,
            {
                "exito": True,
                "respuesta_texto": "Hola, ¿cómo estás?",
                "datos": {},
            },
        )

        mock_post.assert_called_once()

    @patch("app.conversation.service.requests.post")
    def test_responder_respuesta_vacia(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "response": "   "
        }

        mock_post.return_value = mock_response

        servicio = ConversationService()

        resultado = servicio.responder("hola teto")

        self.assertEqual(
            resultado,
            {
                "exito": False,
                "respuesta_texto": "No pude generar una respuesta.",
                "datos": {},
            },
        )

    @patch("app.conversation.service.requests.post")
    def test_responder_error_conexion(self, mock_post):
        mock_post.side_effect = requests.RequestException(
            "Error de conexión"
        )

        servicio = ConversationService()

        resultado = servicio.responder("hola teto")

        self.assertEqual(
            resultado,
            {
                "exito": False,
                "respuesta_texto": "No pude conectarme con el modelo de lenguaje.",
                "datos": {},
            },
        )


if __name__ == "__main__":
    unittest.main()