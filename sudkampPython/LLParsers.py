from grammars.grammar import STARTSYMBOL
from grammars.contextFree import ContextFreeGrammar

"""
 Algorithm 19.4.1
input: context-free grammar G = (V, Alphabet, P, S)

1. for each a that is in Alphabet do F`(a) := {a}
2. for each A that is in V do F(a) := { {null}     if A -> null is rule in P
									  { empty set  otherwise
3. repeat
    3.1 for each A that is in V do F`(A) := F(A)
 	3.2 for each rule A -> u<sub>1</sub>u<sub>2</sub>...u<sub>n</sub> with n > 0 do
 			F(A) := F(A) UNION
 					trunc<sub>k</sub>(F`(u<sub>1</sub>)F`(u<sub>2</sub>)...F`(u<sub>n</sub>))    until F(A) = F`(A) for all A in V
 4. FIRST<sub>k</sub>(A) = F(A)
"""
def FIRSTk( k, G ):
    Fprime, F, first_k = {}, {}, {} # initialise dictionaries
	for a in G.terminals:
        Fprime[a] = {a}
    for A in G.vars:
        {None} if Rule(A, None) in G.rules else {}
    while True:
        for A in G.vars:
            Fprime[A] = F[A]
            for rule in [rule for rule in G.rules if len(rule.rhs) > 0]:
                F[A] = F[A] | trunc_k( Fprime[] for all elements of rhs concatenated)

        if all(F[A] == Fprime[A] for A in G.vars):
            break
    for A in G.vars: # Originally just FIRSTk[A] = F[A]
        first_k[A] = F[A]
    return first_k

"""
Algorithm 19.5.1

input: context-free grammar G = (V, Alphabet, P, S)
		  FIRSTk(A) for every A in V

1. FL(S) := {null}
2. for each A in V - {S} do FL(A) := empty
3. repeat
	3.1 for each A in V do FL`(A) := FL(A)
	3.2 for each rule A -> w  = u<sub>1</sub>u<sub>2</sub>...u<sub>n</sub> with
		w NOT a terminal string do
		3.2.1 L := FL`(A)
		3.2.2 if u<sub>n</sub> in V then FL(u<sub>n</sub>) := FL(u<sub>n</sub>) UNION L
		3.2.3 for i := n - 1 to 1 do
			3.2.3.1 L := trunc<sub>k</sub>(FIRST<sub>k</sub>(u<sub>i+1</sub>)L)
			3.2.3.2 if u<sub>i</sub> in V then FL(u<sub>i</sub>) := FL(u<sub>i</sub>) UNION L
    until FL(A) = FL`(A) for every A in V
4. FOLLOW<sub>k</sub>(A) := FL(A)
"""
def FOLLOWk(k, G, FIRSTk ):
    follow_k, FLprime = {}, {} # initialise
    FL = { STARTSYMBOL : {None} }
    for A in (G.vars - {STARTSYMBOL}): FL[A] = {}
    while True: # repeat
        for A in G.vars: FLprime[A] = FL[A]
        for rule in [r for r in G.rules if any(u.isupper() for u in r.rhs)]:
            A = rule.lhs[0]
            L = FLprime[A]
            n = len(rule.rhs)
            u = rule.rhs
            if u[n-1] in G.vars: FL[u[n-1]] = FL[u[n-1]] | L
            for i in range(len(r.rhs)-2, -1, -1): # equiv to n-1, n-2, n-3, ..., 1
                L = trunc_k( k, FIRSTk( k, u[n+1]).update(L) ) # TODO: this could be wrong!!
                if u[i] in G.vars:
                    FL[u[i]] = FL[u[i]] | L
        if all(FL[A] = FLprime[A] for A in G.vars): # until
            break
    for A in G.vars:
        follow_k[A] = FL[A]
    return follow_k

"""
Introduced to simplify the definition of the fixed-length lookahead sets,
trunc_k is a function from powerset(Σ*) to powerset(Σ*) defined by:
    trunc_k(X) = {u | u ϵ X with len(u) <= k or uv ϵ X with len(u) = k}
"""
def trunc_k( k, X ):
    result = set()
    for uv in X:
        if len(uv) <= k:
            result.add( uv ) # uv is u ϵ X
        else:
            result.add( uv[:k] )
    return result

def LA_k( k, A ):
    return trunc_k( k, LA(A))

"""
The lookahead set of the variable A, LA(A), is defined by
    LA(A) = {x | S *-> uAv *-> ux ϵ Σ*}
For each rule A -> w in P, the lookahead set of the rule A -> w is defined by
    LA(A->w) = {x | wv *-> x where x ϵ Σ* and S *-> uAv}
"""
def LA( X ):
    if type(X) == str: # X is variable, A
        pass # TODO
        #return {x | S *-> uAv *-> ux ϵ Σ*} # TODO: this is complicated
    else: # X is a rule A -> w
        pass # TODO
        #return {x | wv *-> x where x ϵ Σ* and S *-> uAv}
