class Amdahl:
    def __init__(self, porcentaje_de_mejora: float, factor_de_mejora: float):
        self.porcentaje_de_mejora = porcentaje_de_mejora
        self.factor_de_mejora = factor_de_mejora
    
    def aceleracion(self) -> float:
        if not 0 <= self.porcentaje_de_mejora <= 1:
            raise ValueError("El porcentaje de mejora debe estar entre 0 y 1")
        if self.factor_de_mejora <= 0:
            raise ValueError("El factor de mejora debe ser mayor que 0")
        
        return 1 / (1 - self.porcentaje_de_mejora + self.porcentaje_de_mejora / self.factor_de_mejora)

if __name__ == "__main__":
    # Ejemplo de uso
    # Crear un objeto Amdahl con un 25% de mejora y un factor de mejora de 6
    obj = Amdahl(0.25, 6)
    print(obj.aceleracion())