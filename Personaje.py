class Personaje:
    nombre = ""
    clase = "" ## esto pasaria a ser una clase
    arma = "" ## esto tambien seria una clase
    vida = 100

    def __init__(self, nombre, clase, vida, arma):
        self.vida = vida
        self.nombre = nombre
        self.arma = arma
        self.clase = clase
    def presentar(self,nombre,clase,arma):
        print(f"Hola aventurero, me llamo {nombre} , mi clase es {clase} y uso {arma}.")
    def atacar(self):
        return

    def defender(self):
        return

