from rotor import Rotor
from plugboard import Plugboard
from const import plugstring

class Enigma:
    def __init__(self,plug=plugstring,r1=4,r2=2,r3=5):
        self.plugboard = Plugboard(plug)
        self.rotor1 = Rotor(r1)
        self.rotor2 = Rotor(r2)
        self.rotor3 = Rotor(r3)
        
    def cipher(self,plain:str):
        self.ciphertext = ""
        for ch in plain.lower().replace(" ",''):
            plug = self.plugboard.forward(ch)
            r = self.rotor_cycle(plug)
            revplug = self.plugboard.forward(r)
            self.ciphertext = self.ciphertext + revplug
        return self.ciphertext

    def rotor_cycle(self,plug):
        r1 = self.rotor1.forward(plug)
        r2 = self.rotor2.forward(r1)
        r3 = self.rotor3.forward(r2)
        return r3