# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSurface(self):
        return 2 * self.a * self.b + 2 * self.a * self.c + 2 * self.c * self.b

    def getVolume(self):
        return self.a * self.b * self.c

my_cuboid = Cuboid(2, 3, 4)
print("The surface of the cuboid is:",my_cuboid.getSurface())
print("The volume of the cuboid is:",my_cuboid.getVolume())
