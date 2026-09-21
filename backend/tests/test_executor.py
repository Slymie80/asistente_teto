import unittest
from unittest.mock import patch

from app.commands.executor import CommandExecutor


class TestCommandExecutor(unittest.TestCase):
    @patch("app.commands.executor.SystemCommands.consultar_hora")
    def test_ejecutar_consultar_hora(self, mock_consultar_hora):
        mock_consultar_hora.return_value = {
            "exito": True,
            "respuesta_texto": "Son las 12:34",
            "datos": {
                "hora": "12:34",
            },
        }

        executor = CommandExecutor()

        resultado = executor.ejecutar(
            {
                "intencion": "consultar_hora",
                "accion": "consultar_hora",
                "parametros": {},
            }
        )

        mock_consultar_hora.assert_called_once_with()

        self.assertEqual(
            resultado,
            {
                "exito": True,
                "respuesta_texto": "Son las 12:34",
                "datos": {
                    "hora": "12:34",
                },
            },
        )

    @patch("app.commands.executor.ConversationService.responder")
    def test_ejecutar_responder(self, mock_responder):
        mock_responder.return_value = {
            "exito": True,
            "respuesta_texto": "Hola",
            "datos": {},
        }

        executor = CommandExecutor()

        resultado = executor.ejecutar(
            {
                "intencion": "responder",
                "accion": "responder",
                "parametros": {
                    "mensaje": "hola teto"
                },
            }
        )

        mock_responder.assert_called_once_with(
            mensaje="hola teto"
        )

        self.assertEqual(
            resultado,
            {
                "exito": True,
                "respuesta_texto": "Hola",
                "datos": {},
            },
        )

    def test_ejecutar_accion_no_implementada(self):
        executor = CommandExecutor()

        resultado = executor.ejecutar(
            {
                "intencion": "buscar_web",
                "accion": "buscar_web",
                "parametros": {
                    "consulta": "Python"
                },
            }
        )

        self.assertEqual(
            resultado,
            {
                "exito": False,
                "respuesta_texto": "Todavía no puedo ejecutar esa acción.",
                "datos": {
                    "accion": "buscar_web",
                    "parametros": {
                        "consulta": "Python"
                    },
                },
            },
        )


if __name__ == "__main__":
    unittest.main()