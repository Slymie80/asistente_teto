import unittest
from unittest.mock import patch

from app.nlu.intent_parser import IntentParser


class TestIntentParser(unittest.TestCase):
    @patch("app.nlu.intent_parser.LLMClient.interpretar_con_llm")
    def test_interpretar_consultar_hora(self, mock_interpretar):
        mock_interpretar.return_value = {
            "intencion": "consultar_hora",
            "accion": "consultar_hora",
            "parametros": {},
        }

        parser = IntentParser()

        resultado = parser.interpretar("qué hora es")

        self.assertEqual(
            resultado,
            {
                "intencion": "consultar_hora",
                "accion": "consultar_hora",
                "parametros": {},
            },
        )

    @patch("app.nlu.intent_parser.LLMClient.interpretar_con_llm")
    def test_interpretar_responder_usa_texto_original(self, mock_interpretar):
        mock_interpretar.return_value = {
            "intencion": "responder",
            "accion": "responder",
            "parametros": {
                "saludo": "hola"
            },
        }

        parser = IntentParser()

        resultado = parser.interpretar("hola teto")

        self.assertEqual(
            resultado,
            {
                "intencion": "responder",
                "accion": "responder",
                "parametros": {
                    "mensaje": "hola teto"
                },
            },
        )

    @patch("app.nlu.intent_parser.LLMClient.interpretar_con_llm")
    def test_interpretar_accion_no_permitida(self, mock_interpretar):
        mock_interpretar.return_value = {
            "intencion": "hacer_algo_raro",
            "accion": "borrar_sistema",
            "parametros": {},
        }

        parser = IntentParser()

        resultado = parser.interpretar("haz algo raro")

        self.assertEqual(
            resultado,
            {
                "intencion": "desconocida",
                "accion": "ninguna",
                "parametros": {},
            },
        )

if __name__ == "__main__":
    unittest.main()