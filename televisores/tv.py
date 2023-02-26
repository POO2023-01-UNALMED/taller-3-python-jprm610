from televisores.control import Control
from televisores.marca import Marca

class TV :
    numTV = 0

    def __init__(self, marca:Marca, estado)  :
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.control = None
        TV.numTV += 1

    # GETS
    def getMarca(self) :
        return self.marca
    
    def getControl(self) :
        return self.control
    
    def getPrecio(self) :
        return self.precio
    
    def getVolumen(self) :
        return self.volumen
    
    def getCanal(self) :
        return self.canal
    
    def getEstado(self) :
        return self.estado
    
    @staticmethod
    def getNumTV() :
        return TV.numTV
    
    # SETS
    def setMarca(self, marca:Marca) :
        self.marca = marca
        return

    def setControl(self, control:Control) :
        self.control = control
        return
    
    def setPrecio(self, precio) :
        self.precio = precio
        return
    
    def setVolumen(self, volumen) :
        if not (0 <= volumen <= 7) or not self.estado : return
        self.volumen = volumen
        return
    
    def setCanal(self, canal) :
        if not (1 <= canal <= 120) or not self.estado : return
        self.canal = canal
        return
    
    @staticmethod
    def setNumTV(num) :
        TV.numTV = num
        return
    
    # METODOS
    def turnOn(self) :
        self.estado = True
        return
    
    def turnOff(self) :
        self.estado = False
        return
    
    def canalUp(self) :
        if self.canal == 120 or not self.estado : return
        self.canal += 1
        return
    
    def canalDown(self) :
        if self.canal == 1 or not self.estado : return
        self.canal -= 1
        return
    
    def volumenUp(self) :
        if self.volumen == 7 or not self.estado : return
        self.volumen += 1
        return
    
    def volumenDown(self) :
        if self.volumen == 0 or not self.estado : return
        self.volumen -= 1
        return
    