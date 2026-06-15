# Gestión de Mascotas en Python — Tradicional y POO

Proyecto académico que implementa un mismo problema (registrar y mostrar los datos
de una mascota) bajo dos paradigmas de programación distintos.

## Autor

**Carlos Javier Cedeño Leiton**

## Objetivo

Comparar de manera práctica la **programación tradicional** (basada en funciones)
con la **programación orientada a objetos** (basada en clases y objetos),
resolviendo exactamente el mismo problema en ambos casos. Los datos manejados por
cada mascota son: nombre, especie y edad.

## Organización de las carpetas

| Carpeta / archivo | Contenido |
|---|---|
| `programacion_tradicional/tradicional.py` | Solución con funciones, sin clases ni objetos |
| `programacion_poo/mascota.py` | Definición de la clase `Mascota` |
| `programacion_poo/main.py` | Programa principal que crea y usa los objetos |
| `README.md` | Documentación del proyecto |

## Programa tradicional

El archivo `tradicional.py` resuelve el problema usando solo funciones y variables.
El usuario ingresa los datos por teclado, el programa valida la información
(campos no vacíos y edad numérica) y muestra una ficha ordenada de la mascota.
Incluye además un pequeño menú que permite registrar varias mascotas seguidas.

Ejecución:

```bash
cd programacion_tradicional
python tradicional.py
```

## Programa orientado a objetos

La carpeta `programacion_poo` separa la lógica en dos archivos. En `mascota.py` se
define la clase `Mascota` con los atributos `nombre`, `especie` y `edad`, y con los
métodos `mostrar_informacion()` y `hacer_sonido()`. En `main.py` se importa esa
clase, se crean tres objetos distintos y se ejecutan sus métodos dentro de un ciclo
para mostrar la información de cada uno.

Ejecución:

```bash
cd programacion_poo
python main.py
```

## Reflexión sobre los dos paradigmas

Trabajar el mismo ejercicio dos veces, con enfoques diferentes, me permitió entender
en qué se distingue cada uno:

En la **programación tradicional**, el programa se construye como una secuencia de
funciones que reciben y devuelven datos. La información de la mascota se mueve de una
función a otra como variables o como un diccionario. Funciona muy bien para problemas
cortos y se entiende rápido, pero los datos y las acciones quedan separados.

En la **programación orientada a objetos**, en cambio, los datos (atributos) y las
acciones (métodos) viven juntos dentro de la clase. Cada objeto es una mascota
independiente que conoce su propia información y sabe cómo comportarse. Esto facilita
crear muchas mascotas a partir de un único molde y mantener el código ordenado cuando
el proyecto crece.

Mi conclusión es que ambos enfoques son válidos: la programación tradicional resulta
más simple para tareas pequeñas, mientras que la orientada a objetos aporta más
estructura, reutilización y claridad a medida que el sistema se vuelve más grande.
