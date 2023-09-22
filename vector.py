class Vector:
    # constructor
    def __init__(self, coordinatesList):
        self.coordinatesList = coordinatesList

        # methods
        """normalizes the vector
        """

    def norm(self):
        norm = 0
        for x in self.coordinatesList:
            norm += (x ** 2)

        return ((norm) ** (1 / 2))

        """multiplies the vector with a scalar
        """

    def scalar_multiplication(self, scalar):
        newVector = [(scalar * x) for x in self.coordinatesList]
        return Vector(newVector)

        """return scalar of the inner product of this vector and another vector
        """

    def inner_product(self, Vector):
        result = 0
        index = 0
        if (len(Vector.coordinatesList) == len(self.coordinatesList)):
            while index < len(self.coordinatesList):
                result += (self.coordinatesList[index] + Vector.coordinatesList[index])
                index += 1

        else:
            raise ValueError("Unequal legth coordinates")
        return result


vector1 = Vector([3, 4])
vector2 = Vector([6, 7])

print(vector1.norm())
print(vector1.scalar_multiplication(2))
print(vector2.inner_product(vector1))

