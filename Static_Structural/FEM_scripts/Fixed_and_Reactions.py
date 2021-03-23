# Matrix calculations - in NumPy matrix is vector !


from numpy import zeros

# Gaining a vector from a defined point load
def PointLoad(P, x, L, Direction):
    '''

    :param P: load value [N] float
    :param x: location of the point relative to the start of the beam object -> P+
    :param L: define the length of the beam -> P+
    :param Direction: define the direction of the point load - by Y or Z axis -  Fy or Fz (no angle) string
    '''

    b = L - x # distance of the force in coordinate system

    # Create a matrix of 12 lines and 1 column
    MAT = zeros((12, 1))
    # Fill in depending on direction:

    if Direction == "Fy":
        MAT.itemset((1, 0), -P * b ** 2 * (L + 2 * x) / L ** 3)
        MAT.itemset((5, 0), -P * x * b ** 2 / L ** 2)
        MAT.itemset((7, 0), -P * x ** 2 * (L + 2 * b) / L ** 3)
        MAT.itemset((11, 0), P * x ** 2 * b / L ** 2)
    elif Direction == "Fz":
        MAT.itemset((2, 0), -P * b ** 2 * (L + 2 * x) / L ** 3)
        MAT.itemset((4, 0), P * x * b ** 2 / L ** 2)
        MAT.itemset((8, 0), -P * x ** 2 * (L + 2 * b) / L ** 3)
        MAT.itemset((10, 0), -P * x ** 2 * b / L ** 2)

    return MAT

# Gaining a vector from the concentrated moment
def MomentLoad(M, x, L, Direction):
    '''
    :param M: moment value [Nm] float
    :param x: location of the point relative to the start of the beam object -> P+
    :param L: define the length of the beam -> P+
    :param Direction: Direction may be 'My' or 'Mz' applied about Y or Z axis
    :return:
    '''
    b = L - x # distance of the moment in coordinate system

    # Create a matrix of 12 lines and 1 column
    MAT = zeros((12, 1))

    # Fill in depending on direction:
    if Direction == "Mz":
        MAT.itemset((1, 0), 6*M*x*b/L**3)
        MAT.itemset((5, 0), M*b*(2*x-b)/L**2)
        MAT.itemset((7, 0), -6*M*x*b/L**3)
        MAT.itemset((11, 0), M*x*(2*b-x)/L**2)
    elif Direction == "My":
        MAT.itemset((2, 0), -6*M*x*b/L**3)
        MAT.itemset((4, 0), M*b*(2*x-b)/L**2)
        MAT.itemset((8, 0), 6*M*x*b/L**3)
        MAT.itemset((10, 0), M*x*(2*b-x)/L**2)
    return MAT

# Linear distributed load

def LinearLoad(w1, w2, x1, L, Direction):
    MAT = zeros((12, 1))

    if Direction == 'Fy':
        MAT.itemset((1, 0), (x1 - x2)*(10*L**3*w1 + 10*L**3*w2 - 15*L*w1*x1**2 - 10*L*w1*x1*x2 - 5*L*w1*x2**2 - 5*L*w2*x1**2 - 10*L*w2*x1*x2 - 15*L*w2*x2**2 + 8*w1*x1**3 + 6*w1*x1**2*x2 + 4*w1*x1*x2**2 + 2*w1*x2**3 + 2*w2*x1**3 + 4*w2*x1**2*x2 + 6*w2*x1*x2**2 + 8*w2*x2**3)/(20*L**3))
        MAT.itemset((5, 0), (x1 - x2)*(20*L**2*w1*x1 + 10*L**2*w1*x2 + 10*L**2*w2*x1 + 20*L**2*w2*x2 - 30*L*w1*x1**2 - 20*L*w1*x1*x2 - 10*L*w1*x2**2 - 10*L*w2*x1**2 - 20*L*w2*x1*x2 - 30*L*w2*x2**2 + 12*w1*x1**3 + 9*w1*x1**2*x2 + 6*w1*x1*x2**2 + 3*w1*x2**3 + 3*w2*x1**3 + 6*w2*x1**2*x2 + 9*w2*x1*x2**2 + 12*w2*x2**3)/(60*L**2))
        MAT.itemset((7, 0), -(x1 - x2)*(-15*L*w1*x1**2 - 10*L*w1*x1*x2 - 5*L*w1*x2**2 - 5*L*w2*x1**2 - 10*L*w2*x1*x2 - 15*L*w2*x2**2 + 8*w1*x1**3 + 6*w1*x1**2*x2 + 4*w1*x1*x2**2 + 2*w1*x2**3 + 2*w2*x1**3 + 4*w2*x1**2*x2 + 6*w2*x1*x2**2 + 8*w2*x2**3)/(20*L**3))
        MAT.itemset((11, 0), (x1 - x2)*(-15*L*w1*x1**2 - 10*L*w1*x1*x2 - 5*L*w1*x2**2 - 5*L*w2*x1**2 - 10*L*w2*x1*x2 - 15*L*w2*x2**2 + 12*w1*x1**3 + 9*w1*x1**2*x2 + 6*w1*x1*x2**2 + 3*w1*x2**3 + 3*w2*x1**3 + 6*w2*x1**2*x2 + 9*w2*x1*x2**2 + 12*w2*x2**3)/(60*L**2))
    elif Direction == 'Fz':
        MAT.itemset((2, 0), (x1 - x2)*(10*L**3*w1 + 10*L**3*w2 - 15*L*w1*x1**2 - 10*L*w1*x1*x2 - 5*L*w1*x2**2 - 5*L*w2*x1**2 - 10*L*w2*x1*x2 - 15*L*w2*x2**2 + 8*w1*x1**3 + 6*w1*x1**2*x2 + 4*w1*x1*x2**2 + 2*w1*x2**3 + 2*w2*x1**3 + 4*w2*x1**2*x2 + 6*w2*x1*x2**2 + 8*w2*x2**3)/(20*L**3))
        MAT.itemset((4, 0), -(x1 - x2)*(20*L**2*w1*x1 + 10*L**2*w1*x2 + 10*L**2*w2*x1 + 20*L**2*w2*x2 - 30*L*w1*x1**2 - 20*L*w1*x1*x2 - 10*L*w1*x2**2 - 10*L*w2*x1**2 - 20*L*w2*x1*x2 - 30*L*w2*x2**2 + 12*w1*x1**3 + 9*w1*x1**2*x2 + 6*w1*x1*x2**2 + 3*w1*x2**3 + 3*w2*x1**3 + 6*w2*x1**2*x2 + 9*w2*x1*x2**2 + 12*w2*x2**3)/(60*L**2))
        MAT.itemset((8, 0), -(x1 - x2)*(-15*L*w1*x1**2 - 10*L*w1*x1*x2 - 5*L*w1*x2**2 - 5*L*w2*x1**2 - 10*L*w2*x1*x2 - 15*L*w2*x2**2 + 8*w1*x1**3 + 6*w1*x1**2*x2 + 4*w1*x1*x2**2 + 2*w1*x2**3 + 2*w2*x1**3 + 4*w2*x1**2*x2 + 6*w2*x1*x2**2 + 8*w2*x2**3)/(20*L**3))
        MAT.itemset((10, 0), -(x1 - x2)*(-15*L*w1*x1**2 - 10*L*w1*x1*x2 - 5*L*w1*x2**2 - 5*L*w2*x1**2 - 10*L*w2*x1*x2 - 15*L*w2*x2**2 + 12*w1*x1**3 + 9*w1*x1**2*x2 + 6*w1*x1*x2**2 + 3*w1*x2**3 + 3*w2*x1**3 + 6*w2*x1**2*x2 + 9*w2*x1*x2**2 + 12*w2*x2**3)/(60*L**2))

    return MAT

    # Returns the fixed end reaction vector for a distributed axial load
    def AxialLoad(p1, p2, x1, x2, L):

        # Create the fixed end reaction vector
        MAT = zeros((12, 1))

        # Populate the fixed end reaction vector
        MAT.itemset((0, 0),
                    1 / (6 * L) * (x1 - x2) * (3 * L * p1 + 3 * L * p2 - 2 * p1 * x1 - p1 * x2 - p2 * x1 - 2 * p2 * x2))
        MAT.itemset((6, 0), 1 / (6 * L) * (x1 - x2) * (2 * p1 * x1 + p1 * x2 + p2 * x1 + 2 * p2 * x2))

        return MAT

    def Torque(T, x, L):
        '''

        :param T: The magnitude of the torque
        :param x: The location of the torque relative to the start of the member
        :param L:
        :return:
        '''

    # Create the fixed end reaction vector
        MAT = zeros((12, 1))

    # Populate the fixed end reaction vector
        MAT.itemset((3, 0), -T * (L - x) / L)
        MAT.itemset((9, 0), -T * x / L)

        return MAT