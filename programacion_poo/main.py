# ------------------------------------------------------------
# Programa principal. Importa la clase Mascota, crea varios objetos
# y ejecuta sus metodos para mostrar la informacion de cada uno.
# ------------------------------------------------------------

from mascota import Mascota


def main():
    print("############################################")
    print("#   GESTION DE MASCOTAS - VERSION POO      #")
    print("############################################\n")

    # Se crean varios objetos (instancias) de la clase Mascota.
    # Se requieren al menos dos; aqui se usan tres.
    perro = Mascota("Toby", "Perro", 5)
    gato = Mascota("Luna", "Gato", 3)
    caballo = Mascota("Relampago", "Caballo", 7)

    # Se agrupan los objetos para procesarlos en un ciclo
    mascotas = [perro, gato, caballo]

    # Se recorre cada objeto mostrando su numero, datos y sonido
    for numero, mascota in enumerate(mascotas, start=1):
        print(f"----- Mascota #{numero} -----")
        mascota.mostrar_informacion()
        mascota.hacer_sonido()
        print()

    print("Total de mascotas registradas:", len(mascotas))


if __name__ == "__main__":
    main()
