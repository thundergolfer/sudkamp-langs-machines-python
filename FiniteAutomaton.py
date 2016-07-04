import random

class ExceptionFSM(Exception):
    pass

class State(object):

    def __init__(self):
        pass

    def isFinalState(self):
        return fState

    def isAcceptState(self):
        return aState

class Transition(object):

    def __init__(self, input_state, symbol, result_state):
        self.state = input_state
        self.symbol = symbol
        self.result_state

class FiniteAutomaton(object):

    def __init__(self, initial_state):
        self.init_state = initial_state
        self.Q = set()
        self.F = set()
        self.alphabet = set()

    def add_transition(self, symbol, state, action, next_state):
        pass

    def getOtherStates(self,state):
        return [s for s in Q if s != state]

    def getNonFinalStates(self):
        return self.Q.difference(self.F)

    def getANonFinalState(self):
        return random.choice(self.getNonFinalStates())
