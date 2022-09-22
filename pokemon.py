class Pokemones:
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        self.nombre = nombre
        self.tipo=tipo
        self.ataque_especial = ataque_especial
        self.ataque_comun = ataque_comun
        self.puntos_salud=puntos_salud
    
    #función para atacar
    def atacar_comun(self):
        print(f'Usó {self.ataque_comun}')
        
    def atacar_especial(self):
        print(f'Usó {self.ataque_especial}')
    
    #función para restar vida
    def recibir_danio_comun(self):
        self.puntos_salud -= 25
        print(f'Perdió 25 puntos de salud, su vida total es: {self.puntos_salud}')
    
    def recibir_danio_especial(self):
        self.puntos_salud -= 45
        print(f'Perdió 45 puntos de salud, su vida total es: {self.puntos_salud}')
        
    
    #función para recuperar vida
    def recuperar_salud(self):
        if self.puntos_salud <= 70: 
            self.puntos_salud += 30
            print(f'Recuperó 30 puntos de salud, su vida total es: {self.puntos_salud}')
        else: 
            print('No puede recuperar más vida')
    #función para regresar tu pokemon
    def regresar(self):
        if self.puntos_salud <= 0:
            print('Regresa...') 
        else:
            print('No puede regresar, aún tiene puntos de salud')   

#Creación de pokemon especifico.
class Pokemon(Pokemones):
    def __init__(self, nombre, tipo, ataque_especial, ataque_comun, puntos_salud):
        super().__init__(nombre, tipo, ataque_especial, ataque_comun, puntos_salud)

#Pokemon ya creados.
charmander = Pokemon('Charmander', 'Fuego', 'Lanza Llamas', 'arañazo', 100)
bolbasur = Pokemon('Bolbasur', 'Planta', 'Hojas Filosas', 'Embestida', 100)
pikachu = Pokemon('Pikachu', 'Electrico', 'Rayo', 'Ataque Rápido', 100)
squirtle = Pokemon('Squirtle', 'Agua', 'Chorro de Agua', 'Embestida', 100)



#Creación de jugador
class Jugador:

    def __init__(self,nombre_jugador,):
        self.nombre_jugador=nombre_jugador
        


    #función para dar identidad al jugador.
    def dar_nombre(self):
        self.nombre_jugador = input('Intoruzca su nombre: ')
        print(f'Bienvenido entrenador {self.nombre_jugador}')

    #Creación de lista que contendrá a los combatientes.
    combate = []       
    #función para elegir un pokemon ya creado.
    def elegir_pokemon(self,combate):
      
        eleccion = input(f'Seleccione un pokemón: Pikachu Charmander Bolbasur Squirtle: ')
        eleccion = eleccion.lower()
        
        if eleccion == 'pikachu':
            combate.append(pikachu)
            print(f'Elegiste a {combate[0].nombre}') 
        elif eleccion == 'charmander':
            combate.append(charmander)
            print(f'Elegiste a {combate[0].nombre}') 
        elif eleccion == 'bolbasur':
            combate.append(bolbasur)
            print(f'Elegiste a {combate[0].nombre}') 
        elif eleccion == 'squirtle':
            combate.append(squirtle)    
            print(f'Elegiste a {combate[0].nombre}') 

        eleccion2 = input(f'Seleccione un pokemón rival: Pikachu Charmander Bolbasur Squirtle: ')
        eleccion2 = eleccion2.lower()
        
        if eleccion2 == 'pikachu':
            combate.append(pikachu)
            print(f'Elegiste a {combate[1].nombre}') 
        elif eleccion2 == 'charmander':
            combate.append(charmander)
            print(f'Elegiste a {combate[1].nombre}') 
        elif eleccion2 == 'bolbasur':
            combate.append(bolbasur)
            print(f'Elegiste a {combate[1].nombre}') 
        elif eleccion2 == 'squirtle':
            combate.append(squirtle)    
            print(f'Elegiste a {combate[1].nombre}') 
        
        print(f'El combate será entre {combate[0].nombre} vs {combate[1].nombre}')

    def luchar(self,combate):
        eleccion_mov= input(f'Seleccione un movimiento para {combate[0].nombre}: a-{combate[0].ataque_comun} b-{combate[0].ataque_especial} c-Recuperar Salud d-Regresar: ')
        
        if eleccion_mov == 'a': 
            print(combate[0].nombre) 
            combate[0].atacar_comun()       
            print(combate[1].nombre)    
            combate[1].recibir_danio_comun()
        
        elif eleccion_mov == 'b':
            print(combate[0].nombre)
            combate[0].atacar_especial()
            print(combate[1].nombre)
            combate[1].recibir_danio_especial()   

        elif eleccion_mov == 'c':
            print(combate[0].nombre)
            combate[0].recuperar_salud()
        
        elif eleccion_mov == 'd':
            print(combate[0].nombre) 
            combate[0].regresar()
        else:
            ('Selección no válida, pierde turno.')   

 #función de ataque de rival bot
    def luchar_rival(self,combate):
        eleccion_mov_bot= ['a','b','c','d','e']
        
        
            
        for letra in eleccion_mov_bot:
                        
            if letra == 'a': 
                print(combate[1].nombre)
                combate[1].atacar_comun()       
                print(combate[0].nombre)    
                combate[0].recibir_danio_comun()
                break
            elif letra == 'b':
                print(combate[1].nombre)
                combate[1].atacar_especial()
                print(combate[0].nombre)
                combate[0].recibir_danio_especial()   
                break
            elif letra == 'c':
                print(combate[1].nombre)
                combate[1].recuperar_salud()
                break
            elif letra == 'd':
                print(combate[1].nombre) 
                combate[1].regresar()
                break
            else:
                print('Selección no válida, pierde turno.')
                break   
  #función para asignar los movimientos a tu pokemon rival. usar un while que seleccione random los movimientos que sabe el obj pokemon hasta que combste[1].puntos_salud == 0       
    
    def turnos(self, combate):
        while combate[1].puntos_salud >= 0 or combate[0].puntos_salud >= 0:
            player.luchar(player.combate)
            player.luchar_rival(player.combate)
               
            if combate[1].puntos_salud <= 0 and combate[0].puntos_salud > 0:
                print(f'Fin de combate el ganador es {combate[0].nombre}')
            elif combate[0].puntos_salud <= 0 and combate[1].puntos_salud > 0:
                print(f'Fin de combate el ganador es {combate[1].nombre}')
            elif combate[0].puntos_salud <= 0 and combate[1].puntos_salud <= 0:
                print(f'Fin de combate es un empate')


player = Jugador('Jugador 1')
player.dar_nombre()
player.elegir_pokemon(player.combate)
player.turnos(player.combate)
