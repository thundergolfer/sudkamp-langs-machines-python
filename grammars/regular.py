from contextFree import ContextFreeGrammar
from grammar import isVariable, isTerminal

class RegularGrammar(ContextFreeGrammar):

    def validRule(self, r ):
        if not super(RegularGrammar, self).validRule(r):
            return False
        elif not r.rhs: # rhs is null - valid
            return True
        elif len(r.rhs) == 2 and isTerminal(r.rhs[0]) and isVariable(r.rhs[1]):
            return True
        elif len(r.rhs) == 1 and isTerminal(r.lhs[0]):
            return True
        return False
