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
def constructSetOfNullableVars( contextFreeGrammar ):
    raise NotImplementedError

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
def chain( A ):
    raise NotImplementedError

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
def getVariableThatDeriveTerminalStrings( contextFreeGrammar ):
    raise NotImplementedError

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
def constructSetOfReachableVars( contextFreeGrammar ):
    raise NotImplementedError
