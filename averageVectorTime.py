import vector
import random
import time

"""adding random elements to a list"""
def addRand(myList, i):
    for k in range(1, i + 1):
        rand = random.randint(0, 10)
        myList.append(rand)
    return myList


"""measuring time it takes for inner product"""
def measureTime(Vector1, Vector2):
    t1 = time.time()
    Vector1.inner_product(Vector2)
    t2 = time.time()
    return t2 - t1


"""checking for 20 ropunds or 2**i Vectors"""
def avTime():
    resultTime = 0
    exps = []
    testList1 = []
    testList2 = []

    # creating list with exponents of 2
    for j in range(0, 16):
        number = 2 ** j
        exps.append(number)

    # creeating vectors for all exponents of 2
    for k in exps:
        average = 0
        for l in range(1, 21):
            testList1.clear()
            testList2.clear()

            # creating lists
            testList1 = addRand(testList1, k)
            testList2 = addRand(testList2, k)

            # creating vectors from lists
            testVector1 = vector.Vector(testList1)
            testVector2 = vector.Vector(testList2)
            average += measureTime(testVector1, testVector2)
        average = average / 20
        print("For vectors length:", k, "Average time:", average)


avTime()