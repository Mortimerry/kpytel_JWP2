import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__ (self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__ (self, skalar):
        return Vector3D(self.x * skalar, self.y * skalar, self.z * skalar)

    def dot (self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross (self, other):
        return Vector3D(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y-self.y*other.x)

    @staticmethod
    def are_ortogonal(vector1, vector2):
        return vector1.dot(vector2) == 0

#Przyklady uzycia

v1 = Vector3D(10, 10, 10)
print(v1)
print(v1.x)
v1.x = 15
print(v1)

v2 = Vector3D(1,1,1)

v3 = v1 + v2

print(v3)

print(v1.dot(v2))

print(v1.cross(v2))



