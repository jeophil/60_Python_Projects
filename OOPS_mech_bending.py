class RectangleStress():
    #defined the parameters inside the constructor
    def __init__(self, width,thickness,bendingMoment,shearstress):
        self.width = width
        self.thickness = thickness
        self.bendingMoment = bendingMoment
        self.shearstress =shearstress

    #def methods

    def Area(self):
        return self.width*self.thickness

    def Moi(self):
        return (1/12) * (self.width) * (self.thickness**3)
    
    def max_shear_stress(self):
        return (3/2)* (self.shearstress/self.Area())

    def max_bending_stress(self):
        return (-self.bendingMoment * (self.thickness/2)) / self.Moi()

x = RectangleStress(3,4,20,10)

print(x.Area())
print("The max shear stress", x.max_shear_stress())
print("The max bending stress", x.max_bending_stress())