from turtle import forward


wirings = [
            'ekmflgdqvzntowyhxuspaibrcj',
            'ajdksiruxblhwtmcqgznpyfvoe',
            'bdfhjlcprtxvznyeiwgakmusqo',
            'esovpzjayquirhxlnftgkdcmwb',
            'vzbrgityupsdnhlxawmjqofeck'
]


class Rotor:
    def __init__(self,rotor,offset='a'):
        self.offset = offset
        self.window = offset
        self.wiring = wirings[rotor-1]
    
    def rotate(self):
        if self.window=='z':
            self.window = 'a'
        else :
            self.window = chr(ord(self.window)+1)
    
    def forward(self,ch):
        return self.wiring[ord(ch)-97]