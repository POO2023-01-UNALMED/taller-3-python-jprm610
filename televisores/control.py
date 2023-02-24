from televisores.tv import TV

class Control :
    def __init__(self) :
        self.tv:TV = None
        return
    
    # GETS
    def getTv(self) :
        return self.tv
    
    # SETS
    def setTv(self, tv) :
        self.tv = tv
        return

    # METHODS
    def turnOn(self) :
        self.tv.turnOn()
        return
    
    def turnOff(self) :
        self.tv.turnOff()
        return
    
    def canalUp(self) :
        self.tv.canalUp()
        return
    
    def canalDown(self) :
        self.tv.canalDown()
        return
    
    def volumenUp(self) :
        self.tv.volumenUp()
        return
    
    def volumenDown(self) :
        self.tv.volumenDown()
        return
    
    def setCanal(self, canal) :
        if not (1 <= canal <= 120) or not self.tv.estado : return
        self.tv.canal = canal
        return
    
    def enlazar(self, tv:TV) :
        self.tv = tv
        tv.setControl(self)
