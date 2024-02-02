from XOR import operation_table as addOperation
from AND import operation_table as multOperation
from elements import elements
import sys 

def add(leftOperand, rightOperand):
    return addOperation[leftOperand][rightOperand]

def multiply(leftOperand, rightOperand):
    return multOperation[leftOperand][rightOperand]



def showAddition():
    for leftOperand in elements:
        for rightOperand in elements:
            string = "{0!s} + {1!s} = {2!s}".format(leftOperand,rightOperand,add(leftOperand,rightOperand))
            print(string)

def showMultiplication():
    for leftOperand in elements:
        for rightOperand in elements:
            string = "{0!s} * {1!s} = {2!s}".format(leftOperand,rightOperand,multiply(leftOperand,rightOperand))
            print(string)

def isSetNonEmpty():
    if len(elements) > 0:
        print("\nThe set is nonempty")
        return 
    print("The set is empty")
    sys.exit()

def isCommutative():
    for a in elements:
        for b in elements:
            if add(a,b) != add(b,a):
                print("Addition is not commutative")
                sys.exit()
    print("\nAddition is commutative")

def isAssociative():
    for a in elements:
        for b in elements:
            for c in elements:
                ab_c = add(a,add(b,c))
                ab_ac = add(add(a,b), c)
                if ab_c != ab_ac:
                    print("Addition is not associative")
                    sys.exit()
    print("\nAddition is associative")

def isClosed() :
    for element1 in elements:
        for element2 in elements:
            if add(element1,element2) not in elements:
                print("The set is not closed under the addition operations")
                sys.exit()
    print("\nThe set is closed under the addition operation")

def getAdditiveIdentity():
    for candidate in elements:
        isID = True
        for element in elements:
            if (add(candidate,element) != element or add(element, candidate) != element):
                isID = False
        if isID == True:
            print("\nAdditive Identity: ", candidate)
            return candidate
    print("There is no additive Identity")
    sys.exit()

def isAdditiveInverses(additiveIdentity):
    for element in elements:
        inverseExists = False
        for inverseCandidate in elements:
            if (add(element,inverseCandidate) == additiveIdentity and add(inverseCandidate,element) == additiveIdentity):
                inverseExists = True 
                break
        if inverseExists == False:
            print("The element {0!s} does not have an inverse".format(element))
            sys.exit()
    print("\nAdditive Inverses Are Defined")

def getMultiplicativeIdentity():
    for candidate in elements:
        isID = True
        for element in elements:
            if (multiply(candidate,element) != element or multiply(element, candidate) != element):
                isID = False
        if isID == True:
            print("\nMultiplicative Identity: ", candidate)
            return candidate
    print("There is no multiplicative Identity")
    sys.exit()  

def isDistributive():
    for a in elements:
        for b in elements:
            for c in elements:
                ab_c = multiply(a,add(b,c))
                ab_ac = add(multiply(a,b), multiply(a,c))
                print("{0!s} * ({1!s} + {2!s}) = {3!s}".format(a,b,c,ab_c)," ::: ", "({0!s} * {1!s}) + ({0!s} * {2!s}) = {3!s}".format(a,b,c,ab_ac))
                if ab_c != ab_ac:
                    print("Multiplication does not distribute over addition")
                    sys.exit()
                
    print("\nMultiplication does distribute over addition")

print("\nAddition Operations Shown Below")
showAddition()
print("\nMultiplication Operations Shown Below")
showMultiplication()
isSetNonEmpty()
additiveIdentity = getAdditiveIdentity()
isAdditiveInverses(additiveIdentity)
isAssociative()
isCommutative()
print("\nThe set is a group under addition")
multiplicativeIdentity = getMultiplicativeIdentity()
isDistributive()
print("The set under the defined operations of addition and multiplication do form a ring!")

