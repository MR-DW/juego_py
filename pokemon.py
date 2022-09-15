class Pokemones:
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        self.nombre = nombre
        self.tipo=tipo
        self.ataque_especial = ataque_especial
        self.ataque_comun=ataque_comun
        self.puntos_salud=puntos_salud
    
    def atacar(self,arg):
        a='a'
        b='b'
        if arg == a:
            print(f'Usó {self.ataque_comun}')
        elif arg == b:
            print(f'Usó {self.ataque_especial}')

    def recibir_ataque(self, arg):
        a = 25
        b = 45
        if arg == a:
            self.puntos_salud -= a
            print(f'Perdió puntos de salud, su vida total es: {self.puntos_salud}')
        elif arg == b:
            self.puntos_salud -= b
            print(f'Perdió puntos de salud, su vida total es: {self.puntos_salud}')
        else:
            print('No existe ese ataque')
    
    def esquivar(self):
        print('Esquivó su ataque')
    
    def regresar(self):
        if self.puntos_salud <= 0:
            print('Regresa...') 
        else:
            print('No puede regresar, aún tiene puntos de salud')   


class Pokemon(Pokemones):
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        super().__init__(nombre, tipo, ataque_especial, ataque_comun, puntos_salud)
    
    
charmander = Pokemon('Charmander', 'Fuego', 'Lanza Llamas', 'arañazo', 100)
# print(f' Mi primer pokemon es {pokemon_1.nombre} es de tipo {pokemon_1.tipo} quiero enseñarle {pokemon_1.ataque_especial}, \n solo sabe {pokemon_1.ataque_comun}.')
bolbasur = Pokemon('Bolbasur', 'Planta', 'Hojas Filosas', 'Embestida', 100)
# print(f' Mi segundo pokemon es {pokemon_2.nombre} es de tipo {pokemon_2.tipo} quiero enseñarle {pokemon_2.ataque_especial}, \n solo sabe {pokemon_2.ataque_comun}.')
pikachu = Pokemon('Pikachu', 'Electrico', 'Rayo', 'Embestida', 100)
squirtle = Pokemon('Squirtle', 'Agua', 'Chorro de Agua', 'Embestida', 100)



class Jugador:
    def __init__(self,nombre_jugador):
        self.nombre_jugador=nombre_jugador
    
    def dar_nombre(self):
        self.nombre_jugador = input('Intoruzca su nombre: ')
        print(f'Bienvenido {self.nombre_jugador}')
    
    def elegir_pokemon(self):
        eleccion = input('Seleccione un pokemón: a-Pikachu b-Charmander c-Bolbasur d-Squirtle: ')

        if eleccion == 'a':
           select1 = print(f'Elegiste a {pikachu.nombre}')
        elif eleccion == 'b':
           select1 = print(f'Elegiste a {charmander.nombre}')
        elif eleccion == 'c':
           select1 = print(f'Elegiste a {bolbasur.nombre}')
        elif eleccion == 'd':
           select1 = print(f'Elegiste a {squirtle.nombre}')   
        else:
             print('Selección no válida.')
    
        eleccion2 = input('Seleccione un pokemón oponente: m-Pikachu n-Charmander o-Bolbasur p-Squirtle: ')
        
        if eleccion2 == 'm':
           select2 = print(f'Elegiste a {pikachu.nombre}')
        elif eleccion2 == 'n':
            select2 = print(f'Elegiste a {charmander.nombre}')
        elif eleccion2 == 'o':
           select2 =  print(f'Elegiste a {bolbasur.nombre}')
        elif eleccion2 == 'p':
            select2 = print(f'Elegiste a {squirtle.nombre}')    
        else:
             print('Selección no válida.')

        print(f'Inicia tu combate: {select1} vs {select2}')

    def elegir_movimiento(self):
        eleccion = input('Seleccione un movimiento: a-Atacar b-Esquivar c-Regresar: ')
        a = 'a'
        b= 'b'
        c= 'c'
        if eleccion == a:
            (f'{Pokemon.atacar}')
        elif eleccion == b:
            (f'{Pokemon.esquivar}')
        elif eleccion == c:
            (f'{Pokemon.regresar}')
        else:
            ('Selección no válida.')

class Maquina:
    def __init__(self,nombre_jugador):
        self.nombre_jugador=nombre_jugador
        
    def elegir_movimiento(self):
        eleccion = input('Seleccione un movimiento: a-Atacar b-Esquivar c-Regresar: ')
        a = 'a'
        b= 'b'
        c= 'c'
        if eleccion == a:
            (f'{Pokemon.atacar}')
        elif eleccion == b:
            (f'{Pokemon.esquivar}')
        elif eleccion == c:
            (f'{Pokemon.regresar}')
        else:
            ('Selección no válida.')

player = Jugador('Jugador 1')
# player.dar_nombre()
player.elegir_pokemon()
player.elegir_movimiento()









# print(charmander.nombre)
# charmander.atacar('a')
# print(bolbasur.nombre)
# bolbasur.recibir_ataque(25)
# print(bolbasur.nombre)
# bolbasur.atacar('a')
# print(charmander.nombre)
# charmander.esquivar()
# print(charmander.nombre)
# charmander.atacar('b')
# print(bolbasur.nombre)
# bolbasur.recibir_ataque(45)
# bolbasur.regresar()
# print(charmander.nombre)
# charmander.atacar('b')
# print(bolbasur.nombre)
# bolbasur.recibir_ataque(45)
# print(bolbasur.nombre)
# bolbasur.regresar()