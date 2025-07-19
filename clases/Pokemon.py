

class Pokemon:


    def __init__(self, nombre: str, vida: float, ataque: float, defensa: float, velocidad: float) -> None:
        self.nombre = nombre
        self.max_vida = self.vida = vida
        self.max_ataque = self.ataque = ataque
        self.max_defensa = self.defensa = defensa
        self.max_velocidad = self.velocidad = velocidad
        self.vivo = not self.is_dead()


    def is_dead(self) -> bool:
        return self.vida <= 0


    def estado(self) -> str:
        if self.vida == 0:
            return f"{self.nombre} está muerto."
        elif self.vida <= 0.2 * self.max_vida:
            return f"{self.nombre} emitió un sonido agónico."
        elif self.vida <= 0.6 * self.max_vida:
            return f"{self.nombre} se encuentra cansado."
        else:
            return f"{self.nombre} está lleno de vitalidad."


    def subida_nivel(self) -> "Pokemon":
        #Se hace como procedimiento para guardar estado y como return para concatenar calls 
        self.max_vida = 1.1 * self.max_vida
        self.max_ataque = 1.1 * self.max_ataque
        self.max_defensa = 1.1 * self.max_defensa
        self.max_velocidad = 1.1 * self.max_velocidad
        return self


    def curar(self) -> "Pokemon":
        self.vida = self.max_vida
        self.ataque = self.max_ataque
        self.defensa = self.max_defensa
        self.velocidad = self.max_velocidad
        return self
