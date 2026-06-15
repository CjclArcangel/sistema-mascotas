# ------------------------------------------------------------
# Aqui se define la clase Mascota. Se evidencian los conceptos de
# clase, objeto, atributos, metodos y abstraccion: la clase es un
# molde que representa a cualquier mascota del mundo real.
# ------------------------------------------------------------


class Mascota:
    """Modelo que representa a una mascota y su comportamiento."""

    def __init__(self, nombre, especie, edad):
        # Atributos propios de cada objeto Mascota
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Imprime en pantalla los datos del objeto de forma clara."""
        print("Mascota registrada:")
        print(f"   - Nombre  : {self.nombre}")
        print(f"   - Especie : {self.especie}")
        print(f"   - Edad    : {self.edad} anio(s)")

    def hacer_sonido(self):
        """Devuelve el sonido caracteristico segun la especie."""
        especie = self.especie.lower()

        # Se decide el sonido con una estructura condicional
        if especie == "perro":
            sonido = "Guau!"
        elif especie == "gato":
            sonido = "Miau!"
        elif especie in ("pajaro", "pájaro"):
            sonido = "Pio pio!"
        elif especie == "vaca":
            sonido = "Muuu!"
        elif especie == "caballo":
            sonido = "Iiiih!"
        else:
            sonido = "(sonido desconocido)"

        print(f"   {self.nombre} hace: {sonido}")
