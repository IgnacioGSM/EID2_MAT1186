class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        raise IndexError("La pila está vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        raise IndexError("La pila está vacía")

    def ver_x_elementos(self, x):
        if x < 0 or x > len(self.elementos):
            raise ValueError("Número de elementos fuera de rango")
        return self.elementos[-x:] if x > 0 else []
    
    def __len__(self):
        return len(self.elementos)