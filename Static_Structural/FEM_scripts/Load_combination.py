
class LoadCombination():
    def __init__(self, name, combination_type = None, factors={}):

        self.name = name # should be defined by user
        self.combination_type = combination_type # what is the type of combination
        self.factors = factors

    def AddLoadCase(self, case_name, factor):

        self.factors[case_name] = factor

    def DeleteLoadCase(self, case_name):

        del self.factors[case_name]