import unittest
import configuracion
import funciones

class TestJuegoCartas(unittest.TestCase):
    """
    Funciones probadas:
    - test_fuerza_simple: Verifica que la función fuerza sume correctamente los valores de fuerza de las cartas en el campo.
    - test_fuerza_vacia: Comprueba que fuerza devuelve 0 cuando el campo está vacío.
    - test_aplicar_efecto_sangrado: Asegura que los efectos persistentes (como "Sangrado") se apliquen correctamente al campo enemigo.
    - test_nueva_ronda_resetea_turnos: Confirma que al iniciar una nueva ronda se reinicia el contador de turnos y se reparte una nueva mano al jugador.
    """
    def test_fuerza_simple(self):
        campo = [("Soldado", 3), ("Mago", 5), ("Bestia", 2)]
        resultado = funciones.fuerza(campo)
        self.assertEqual(resultado, 10)

    def test_fuerza_vacia(self):
        campo = []
        resultado = funciones.fuerza(campo)
        self.assertEqual(resultado, 0)

    def test_aplicar_efecto_sangrado(self):
        campo = [("Soldado", 5), ("Arquero", 3)]
        def sangrado(campo):
            return [(n, max(f - 1, 0)) for n, f in campo]
        configuracion.efectos_enemigo = [{"nombre": "Sangrado", "funcion": sangrado}]
        configuracion.campo_enemigo = campo.copy()
        funciones.aplicar_efectos_persistentes()
        esperado = [("Soldado", 4), ("Arquero", 2)]
        self.assertEqual(configuracion.campo_enemigo, esperado)

    def test_nueva_ronda_resetea_turnos(self):
        configuracion.turno = 3
        configuracion.jugador_rondas = 1
        funciones.nueva_ronda()
        self.assertEqual(configuracion.turno, 0)
        self.assertEqual(len(configuracion.mano_jugador), 5)

if __name__ == "__main__":
    unittest.main()