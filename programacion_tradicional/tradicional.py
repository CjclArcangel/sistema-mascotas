# ------------------------------------------------------------
# Este programa resuelve el problema sin clases ni objetos.
# Se apoya en funciones, variables y un diccionario para guardar
# temporalmente los datos de la mascota ingresada por el usuario.
# ------------------------------------------------------------


def pedir_texto(mensaje):
    """Pide un texto por teclado y evita que quede vacio."""
    dato = input(mensaje).strip()
    while dato == "":
        print("   * El campo no puede quedar vacio.")
        dato = input(mensaje).strip()
    return dato


def pedir_edad(mensaje):
    """Pide la edad y se asegura de que sea un numero entero valido."""
    while True:
        valor = input(mensaje).strip()
        try:
            edad = int(valor)
            if edad < 0:
                print("   * La edad no puede ser negativa.")
                continue
            return edad
        except ValueError:
            print("   * Debe ingresar un numero entero.")


def capturar_datos():
    """Captura los datos de la mascota y los guarda en un diccionario."""
    print("\n--- Registro de una nueva mascota ---")
    datos = {
        "nombre": pedir_texto("Nombre de la mascota: "),
        "especie": pedir_texto("Especie de la mascota: "),
        "edad": pedir_edad("Edad de la mascota (anios): ")
    }
    return datos


def imprimir_ficha(datos):
    """Muestra la informacion de la mascota de forma ordenada."""
    print("\n+----------------------------------+")
    print("|        FICHA DE LA MASCOTA       |")
    print("+----------------------------------+")
    print(" Nombre  ->", datos["nombre"])
    print(" Especie ->", datos["especie"])
    print(" Edad    ->", datos["edad"], "anio(s)")
    print("+----------------------------------+")


def ejecutar():
    """Controla el flujo general del programa con un pequeno menu."""
    print("====== SISTEMA DE GESTION DE MASCOTAS ======")
    continuar = "s"

    while continuar.lower() == "s":
        # Se capturan y luego se muestran los datos
        mascota = capturar_datos()
        imprimir_ficha(mascota)

        continuar = input("\nDesea registrar otra mascota? (s/n): ").strip()

    print("\nPrograma finalizado. Gracias por usarlo.")


# Inicio del programa
if __name__ == "__main__":
    ejecutar()
