

from .Pokemon import Pokemon

class Combate:


    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon, recompensa: float) -> None:
        self.turno = 1
        self.recompensa = recompensa
        self.pokemons = [pokemon1, pokemon2]
        self.acciones = {}
        print("\nESTADO INICIAL:")
        for p in self.pokemons:
            print(f"  {p.nombre}: {p.estado()}")
        self.combate_loop()


    def combate_loop(self) -> None:
        self.iniciador_combate()

        while not self.pokemons[0].is_dead() and not self.pokemons[1].is_dead():
            self.gestor_turno()
            self.aplicador_turno()
            self.turno += 1

        self.finalizador_combate()


    def iniciador_combate(self) -> None:
        print(f"\nEl combate entre {self.pokemons[0].nombre} y {self.pokemons[1].nombre} ha comenzado.\n")


    def finalizador_combate(self) -> None:
        ganador = self.pokemons[0] if not self.pokemons[0].is_dead() else self.pokemons[1]
        print(f"\nEl combate ha terminado. El ganador es {ganador.nombre}.\n")


    def gestor_turno(self) -> None:
        print(f"\nTurno {self.turno}:")
        self.acciones.clear()
        for pkm in self.pokemons:
            accion = input(f"{pkm.nombre}, elige una acción (A = Atacar, D = Defender, S = Acelerar): ").strip().upper()
            while accion not in ("A", "D", "S"):
                accion = input("Entrada no válida. Elige A, D o S: ").strip().upper()
            self.acciones[pkm] = accion


    def aplicador_turno(self) -> None:
        p1, p2 = self.pokemons
        orden = sorted([p1, p2], key=lambda p: p.velocidad, reverse=True)
        defensa_original = {pkm: pkm.defensa for pkm in self.pokemons}

        for pkm in orden:
            if pkm.is_dead():
                continue
            self.aplicar_accion(pkm)

        # Restaurar defensa original si se usó "Defender"
        for pkm in self.pokemons:
            pkm.defensa = defensa_original[pkm]

        # Mostrar estado de ambos
        for pkm in self.pokemons:
            print(f"{pkm.nombre}: {pkm.estado()} (vida: {round(pkm.vida, 1)})")


    def aplicar_accion(self, atacante: Pokemon) -> None:
        oponente = [p for p in self.pokemons if p != atacante][0]
        accion = self.acciones[atacante]

        if accion == "D":
            atacante.defensa *= 2
            print(f"{atacante.nombre} se defiende y duplica su defensa temporalmente.")
        elif accion == "A":
            danno = atacante.ataque - oponente.defensa
            danno_real = max(1, danno)
            oponente.vida -= danno_real
            if oponente.vida < 0:
                oponente.vida = 0
            print(f"{atacante.nombre} ataca y hace {danno_real:.1f} de daño a {oponente.nombre}.")
        elif accion == "S":
            atacante.velocidad *= 2
            print(f"{atacante.nombre} duplica su velocidad.")
