class Amdahl:
    def __init__(self, f: float, k: float):
        
        self.f = f
        self.k = k

    def aceleracion(self):
        
        if not 0 <= self.f <= 1:
            raise ValueError("f tiene que estar entre 0 y 1")
        if self.k <= 0:
            raise ValueError("k tiene que ser mayor que 0")
        return 1 / (1 - self.f + self.f / self.k)

def main():
    pila = []

    while True:
        nombre = input("Ingrese el nombre del proceso o elmento a mejorar (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            porcentaje = float(input(f"Ingrese el porcentaje mejorale de  {nombre} (entre 0 y 100): ")) / 100
            factor = float(input(f"Ingrese el factor de mejora de {nombre} (mayor que 0): "))

            f = porcentaje / 100
            amdahl_obj = Amdahl(f, factor)
            aceleracion = amdahl_obj.aceleracion()

            print(f"La aceleración de {nombre} es: {aceleracion:.4f}")
            pila.append((nombre, aceleracion))

            if len(pila) > 3:
                pila.pop(0)

        except ValueError as e:
                print(f"Error: {e}")
        
    if pila:
        ultimos = pila[::-1]

        mejor_nombre = None
        mejor_aceleracion = -1
        for nombre, aceleracion in ultimos:
            if aceleracion > mejor_aceleracion:
                mejor_aceleracion = aceleracion
                mejor_nombre = nombre

        print("\nConclusión:")
        print(f"De los últimos {len(pila)} elementos ingresados,")
        print(f"'{mejor_nombre}' es el más factible de mejorar, con aceleración de {mejor_aceleracion:.4f}x.")
    else:
        print("\nNo se ingresaron elementos para comparar.")


if __name__ == "__main__":
    main()