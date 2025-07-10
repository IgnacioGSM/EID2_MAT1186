from Amdahl import Amdahl
from Pila import Pila

def main():
    pila = Pila()

    while True:
        nombre = input("Ingrese el nombre del proceso o elmento a mejorar (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            porcentaje = float(input(f"Ingrese el porcentaje mejorale de  {nombre} (entre 0 y 100): "))
            factor = float(input(f"Ingrese el factor de mejora de {nombre} (mayor que 0): "))

            f = porcentaje / 100
            amdahl_obj = Amdahl(f, factor)
            aceleracion = amdahl_obj.aceleracion()

            print(f"La aceleración de {nombre} es: {aceleracion}")
            pila.apilar((nombre, aceleracion))


        except ValueError as e:
                print(f"Error: {e}")
        
    if pila:
        ultimos = pila.ver_x_elementos(len(pila) if len(pila) < 3 else 3)

        mejor_nombre = None
        mejor_aceleracion = -1
        for nombre, aceleracion in ultimos:
            if aceleracion > mejor_aceleracion:
                mejor_aceleracion = aceleracion
                mejor_nombre = nombre

        print("\nConclusión:")
        print(f"De los últimos {len(pila) if len(pila) < 3 else 3} elementos ingresados,")
        print(f"'{mejor_nombre}' es el más factible de mejorar, con aceleración de {mejor_aceleracion:.4f}x.")
    else:
        print("\nNo se ingresaron elementos para comparar.")


if __name__ == "__main__":
    main()