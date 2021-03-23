# create a class representing a node in FEM

class Node():

    def __init__(self, Name, X, Y, Z):
        # define a new node
        self.Name = Name # node name N1, N2, N3...
        self.X = X # X coordinate ...
        self.Y = Y
        self.Z = Z
        self.NodeLoads = [] # A list of loads applied to the node (Direction, P (or L), case)

        # create dicts to calculate node displacement
        self.DX = {} # DISPLACEMENT
        self.DY = {}
        self.DZ = {}
        self.RX = {} # ROTATE
        self.RY = {}
        self.RZ = {}

        # create dicts to calculate node reactions
        self.RxnFY = {}  # DISPLACEMENT
        self.RxnFY = {}
        self.RxnFZ = {}
        self.RxnMX = {}  # ROTATE
        self.RxnMY = {}
        self.RxnMZ = {}

        # Boundary conditions from scratch

        # Initialize all support conditions to 'False'
        self.SupportDX = False
        self.SupportDY = False
        self.SupportDZ = False
        self.SupportRX = False
        self.SupportRY = False
        self.SupportRZ = False

        # Initialize all enforced displacements to 'None'
        self.EnforcedDX = None
        self.EnforcedDY = None
        self.EnforcedDZ = None
        self.EnforcedRX = None
        self.EnforcedRY = None
        self.EnforcedRZ = None
