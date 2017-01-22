from unrestricted import UnrestrictedGrammar
from contextSensitive import ContextSensitiveGrammar
from grammar import isVariable

class ContextFreeGrammar(ContextSensitiveGrammar):

    def validRule(self, r ):
        if not super(ContextFreeGrammar, self).validRule(r):
            if r.rhs: return False
        elif len(r.lhs) != 1 or not isVariable(r.lhs[0]):
            return False
        return True


    """
    Algorithm 4.2.1
    Construction of the Set of Nullable Variables

    input: context-free grammar G = (V, Σ, P, S)

    1. NULL := {A | A -> null ∈ P}
    2. repeat
        2.1 PREV := NULL
        2.2 for each variable A ∈ V do
                if there is an A rule A -> w and w ∈ PREV*, then
                        NULL := NULL ∪ {A}
      until NULL = PREV
    """
    def constructSetOfNullableVars( self ):
        NULL = {r.lhs[0] for r.lhs[0] in self.rules if len(r.rhs) == 0}
        while True:
            PREV = NULL.copy()
            for var in self.vars:
                for rule in  self.rules:
                    if rule.lhs[0] == var and all(v in PREV for v in rule.rhs):
                        A = rule.lhs[0]
                        NULL = NULL.union({A})
            if NULL == PREV:
                break
        return NULL

    """
    Algorithm 4.3.1
    Contruction of the Set CHAIN(A)

    input: essentially noncontracting context-free grammar G = (V, Σ, P, S)

    1. CHAIN(A) := {A}
    2. PREV := ∅
    3. repeat
        3.1 NEW := CHAIN(A) - PREV
        3.2 PREV := CHAIN(A)
        3.3 for each variable B ∈ NEW do
                for each rule B -> C do
                    CHAIN(A) := CHAIN(A) ∪ {C}
       until CHAIN(A) = PREV
    """
    def chain( self, A ):
        if A not in self.vars:
            print(A, " not in grammar's variables.")
            return False
        chain_A = set(A)
        prev = set()
        while True:
            new  = set()
            prev = chain_A.copy()
            for var in new:
                for rule in self.rules:
                    if len(rule.lhs) == 1 and isVariable(rule.lhs[0]):
                        if len(rule.rhs) == 1 and isVariable(rule.rhs[0]):
                            # rule is of form B -> C
                            C = rule.rhs[0]
                            chain_A = chain_A.union(set(C))
            if chain_A == prev:
                break
        return chain_A

    """
    Algorithm 4.4.2
    Construction of the Set of Variables That Derive Terminal Strings

    input: context-free grammar G = (V, Σ, P, S)

    1. TERM := {A | there is a rule A -> w ∈ P with w ∈ Σ*}
    2. repeat
        2.1 PREV := TERM
        2.2 for each variable A ∈ V do
                if there is an A rule A -> w and w ∈ (PREV ∪ Σ*) then
                    TERM := TERM ∪ {A}
       until PREV = TERM
    """
    def getVariablesThatDeriveTerminalStrings( self ):
        TERM = {r.lhs[0] for r.lhs[0] in self.rules if all(t in self.terminals for t in r.rhs)}
        while True:
            PREV = TERM.copy()
            for A in self.vars:
                for r in self.rules:
                    if r.lhs[0] == A and all(t in self.terminals.union(PREV) for t in r.rhs):
                        TERM = TERM.union({A})
            if PREV == TERM:
                break
        return TERM

    """
    Algorithm 4.4.4
    Construction of the Set of Reachable Variables

    input: context-free grammar G = (V, Σ, P, S)

    1. REACH := {S}
    2. PREV := ∅
    3. repeat
        3.1 NEW := REACH - PREV
        3.2 PREV := REACH
        3.3 for each variable A ∈ NEW do
                for each rule A -> w do add all variable in w to REACH
       until REACH = PREV
    """
    def constructSetOfReachableVars( self ):
        REACH = {self.getStartSymbol()}
        PREV = {}
        while True:
            NEW = REACH - PREV
            PREV = REACH.copy()
            for A in NEW:
                for r in self.rules:
                    if r.lhs[0] == A:
                        REACH = REACH.union({x for x in r.rhs if isVariable(x)})
            if REACH == PREV:
                break
        return REACH
