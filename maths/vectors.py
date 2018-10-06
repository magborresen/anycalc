import numpy as np


#  VECTORS IN 2D  #

class VectorsTwo(object):

    def __init__(self, a1, a2, b1, b2):
        self.a = np.array([a1, a2])
        self.b = np.array([b1, b2])

    def addition(self):

        result = self.a + self.b

        return result

    def subtraction(self):

        result = self.a - self.b

        return result

    def multiply(self):

        result = self.a * self.b

        return result

    def divide(self):

        result = self.a / self.b

        return result

    def dot_product(self):

        result = np.dot(self.a, self.b)

        return result

    def scalar_product(self):

        dot = np.dot(self.a, self.b)
        x_modulus = np.sqrt((self.a*self.a).sum())
        y_modulus = np.sqrt((self.b*self.b).sum())

        cos_angle = dot / x_modulus / y_modulus
        angle = np.arccos(cos_angle)
        angle_degrees = angle * 360 / 2 / np.pi

        return angle_degrees


#  VECTORS IN 3D  #

class VectorsThree(object):

        def __init__(self, a1, a2, a3, b1, b2, b3):
            self.a = np.array([a1, a2, a3])
            self.b = np.array([b1, b2, b3])

        def addition(self):

            result = self.a + self.b

            return result

        def subtraction(self):

            result = self.a - self.b

            return result

        def multiply(self):

            result = self.a * self.b

            return result

        def divide(self):

            result = self.a / self.b

            return result

        def dot_product(self):

            result = np.dot(self.a, self.b)

            return result

        def scalar_product(self):

            dot = np.dot(self.a, self.b)
            x_modulus = np.sqrt((self.a*self.a).sum())
            y_modulus = np.sqrt((self.b*self.b).sum())

            cos_angle = dot / x_modulus / y_modulus
            angle = np.arccos(cos_angle)
            angle_degrees = angle * 360 / 2 / np.pi

            return angle_degrees

        def cross_product(self):

            result = np.cross(self.a, self.b)

            return result
