#import animales
from animales import Tortuga

class TortugaMarina(Tortuga):
    def moverse(self):
        super().moverse()
        print("Nadando ando")


tortuguita= TortugaMarina('Manuelita','Tortuga','Verde')
tortuguita.comer()
tortuguita.moverse()