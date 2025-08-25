class Logica:    
    def AND(self, a, b):
        return a and b
    def OR(self, a, b):
        return a or b 
    def NOT(self, a):
        return not a
    def XOR(self, a, b):
        return(a and not b) or (not a and b)
    def NAND(self, a, b):
        return not(a and b)
    def NOR(self, a, b):
        return not (a or b)
    def XNOR(self, a, b):
       return not ((a and not b) or (not a and b))
    def implicacion(self, a, b):
        return (not a) or b 
    def bi_implicacion(self, a, b):
        return a==b
    
    
