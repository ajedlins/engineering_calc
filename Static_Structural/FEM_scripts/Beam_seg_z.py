# define a beam segment - mathematically

class BeamSegZ():

    def __init__(self):
        self.x1 = None  # Start location of beam segment (relative to start of beam)
        self.x2 = None  # End location of beam segment (relative to start of beam)
        self.w1 = None  # Linear distributed transverse load at start of segment
        self.w2 = None  # Linear distributed transverse load at end of segment
        self.p1 = None  # Linear distributed axial load at start of segment
        self.p2 = None  # Linear distributed axial load at end of segment
        self.V1 = None  # Internal shear force at start of segment
        self.M1 = None  # Internal moment at start of segment
        self.P1 = None  # Internal axial force at start of segment
        self.T1 = None  # Torsional moment at start of segment
        self.theta1 = None  # Slope at start of beam segment
        self.delta1 = None  # Displacement at start of beam segment
        self.delta_x1 = None  # Axial displacement at start of beam segment
        self.EI = None  # Flexural stiffness of the beam segment
        self.EA = None  # Axial stiffness of the beam segment

    def Length(self):
        return self.x2 - self.x1

    def Shear(self, x):

        V1 = self.V1
        w1 = self.w1
        w2 = self.w2
        L = self.Length()

        return V1 + w1*x + x**2*(-w1 + w2)/(2*L)

    def Moment(self, x):

        V1 = self.V1
        M1 = self.M1
        w1 = self.w1
        w2 = self.w2
        L = self. Length()

        return M1 - V1*x - w1*x**2/2 - x**3*(-w1 + w2)/(6*L)

    def Axial(self, x):

        P1 = self.P1
        p1 = self.p1
        p2 = self.p2
        L = self.Length()

        return P1 + (p2 - p1)/(2*L)*x**2 + p1*x

    def Torsion(self):
        return self.T1

    def Slope(self, x):
        V1 = self.V1
        M1 = self.M1
        w1 = self.w1
        w2 = self.w2
        theta1 = self.theta1
        L = self.Length()
        EI = self.EI

        return theta1 - (M1 * x - V1 * x ** 2 / 2 - w1 * x ** 3 / 6 + x ** 4 * (w1 - w2) / (24 * L)) / (EI)

    def Deflection(self, x):
        V1 = self.V1
        M1 = self.M1
        w1 = self.w1
        w2 = self.w2
        theta1 = self.theta1
        delta1 = self.delta1
        L = self.Length()
        EI = self.EI

        return delta1 + theta1 * x - M1 * x ** 2 / (2 * EI) + V1 * x ** 3 / (6 * EI) + w1 * x ** 4 / (24 * EI) + x ** 5 * (-w1 + w2) / (120 * EI * L)

    def AxialDeflection(self, x):

        delta_x1 = self.delta_x1
        P1 = self.P1
        p1 = self.p1
        p2 = self.p2
        L = self.Length()
        EA = self.EA

        return delta_x1 - 1/EA*(P1*x + p1*x**2/2 + (p2 - p1)*x**3/(6*L))

    def MaxShear(self):
        w1 = self.w1
        w2 = self.w2
        L = self.Length()

        if w1 - w2 == 0:
            x1 = 0
        else:
            x1 = w1 * L / (w1 - w2)

        if round(x1, 10) < 0 or round(x1, 10) > round(L, 10):
            x1 = 0

        x2 = 0
        x3 = L

        # Find the shear at each location of interest
        V1 = self.Shear(x1)
        V2 = self.Shear(x2)
        V3 = self.Shear(x3)

        # Return the maximum shear
        return max(V1, V2, V3)

    def MinShear(self):

        w1 = self.w1
        w2 = self.w2
        L = self.Length()

        # Determine possible locations of minimum shear
        if w1 - w2 == 0:
            x1 = 0
        else:
            x1 = w1 * L / (w1 - w2)

        if round(x1, 10) < 0 or round(x1, 10) > round(L, 10):
            x1 = 0

        x2 = 0
        x3 = L

        # Find the shear at each location of interest
        V1 = self.Shear(x1)
        V2 = self.Shear(x2)
        V3 = self.Shear(x3)

        # Return the minimum shear
        return min(V1, V2, V3)

    def MaxMoment(self):

        w1 = self.w1
        w2 = self.w2
        V1 = self.V1
        L = self.Length()

        # Find the quadratic equation parameters
        a = -(w2 - w1) / (2 * L)
        b = -w1
        c = -V1

        # Determine possible locations of maximum moment
        if a == 0:
            if b != 0:
                x1 = -c / b
            else:
                x1 = 0
            x2 = 0
        elif b ** 2 - 4 * a * c < 0:
            x1 = 0
            x2 = 0
        else:
            x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
            x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

        x3 = 0
        x4 = L

        if round(x1, 10) < 0 or round(x1, 10) > round(L, 10):
            x1 = 0

        if round(x2, 10) < 0 or round(x2, 10) > round(L, 10):
            x2 = 0

        # Find the moment at each location of interest
        M1 = self.Moment(x1)
        M2 = self.Moment(x2)
        M3 = self.Moment(x3)
        M4 = self.Moment(x4)

        # Return the maximum moment
        return max(M1, M2, M3, M4)

    # %%
    # Returns the minimum moment in the segment
    def MinMoment(self):

        w1 = self.w1
        w2 = self.w2
        V1 = self.V1
        L = self.Length()

        # Find the quadratic equation parameters
        a = -(w2 - w1) / (2 * L)
        b = -w1
        c = -V1

        # Determine possible locations of minimum moment
        if a == 0:
            if b != 0:
                x1 = -c / b
            else:
                x1 = 0
            x2 = 0
        elif b ** 2 - 4 * a * c < 0:
            x1 = 0
            x2 = 0
        else:
            x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
            x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

        x3 = 0
        x4 = L

        if round(x1, 10) < 0 or round(x1, 10) > round(L, 10):
            x1 = 0

        if round(x2, 10) < 0 or round(x2, 10) > round(L, 10):
            x2 = 0

        # Find the moment at each location of interest
        M1 = self.Moment(x1)
        M2 = self.Moment(x2)
        M3 = self.Moment(x3)
        M4 = self.Moment(x4)

        # Return the minimum moment
        return min(M1, M2, M3, M4)

    # %%
    # Returns the maximum axial force in the segment
    def MaxAxial(self):

        p1 = self.p1
        p2 = self.p2
        L = self.Length()

        # Determine possible locations of maximum axial force
        if p1 - p2 != 0:
            x1 = L * p1 / (p1 - p2)
        else:
            x1 = 0

        if round(x1, 10) < 0 or round(x1, 10) > round(L, 10):
            x1 = 0

        x2 = 0
        x3 = L

        # Find the axial force at each location of interest
        P1 = self.Axial(x1)
        P2 = self.Axial(x2)
        P3 = self.Axial(x3)

        # Return the maximum axial force
        return max(P1, P2, P3)

    # %%
    # Returns the minimum axial force in the segment
    def MinAxial(self):

        p1 = self.p1
        p2 = self.p2
        L = self.Length()

        # Determine possible locations of minimum axial force
        if p1 - p2 != 0:
            x1 = L * p1 / (p1 - p2)
        else:
            x1 = 0

        if round(x1, 10) < 0 or round(x1, 10) > round(L, 10):
            x1 = 0

        x2 = 0
        x3 = L

        # Find the axial force at each location of interest
        P1 = self.Axial(x1)
        P2 = self.Axial(x2)
        P3 = self.Axial(x3)

        # Return the minimum axial force
        return min(P1, P2, P3)

    # %% Returns the maximum torsional moment in the segment
    def MaxTorsion(self):

        return self.T1

    # %% Returns the minimum torsional moment in the segment
    def MinTorsion(self):

        return self.T1