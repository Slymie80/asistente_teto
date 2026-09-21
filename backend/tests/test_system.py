import unittest
from unittest.mock import patch

from app.commands.system import SystemCommands


class TestSystemCommands(unittest.TestCase):
    @patch("app.commands.system.datetime")
    def test_consultar_hora(self, mock_datetime):
        mock_datetime.now.return_value.strftime.return_value = "12:34"

        system = SystemCommands()

        resultado = system.consultar_hora()

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


if __name__ == "__main__":
    unittest.main()