class Plugboard:
    def __init__(self,plugstring = "lushqoxdmznaikfrepcybwvgtj"):
        self.plugstring = plugstring.lower()

    def forward(self,ch):
        return self.plugstring[ord(ch)-97]