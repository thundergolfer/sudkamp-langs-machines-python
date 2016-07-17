"""
Algorithm 5.7.2
Determination of Equivalent States of DFA

input: DFA M = (Q, Alphabet, TransitionFunctoin, q<sub>0</sub>, F)

1. (Initialization)
	  for every pair of states q<sub>i</sub> and q<sub>j</sub>, i < j, do
 		1.1 D[i,j] := 0
 		1.2 S[i,j] := null set
 	  end for
2. for every pair i, j, i < j,  if one of q<sub>i</sub> or q<sub>j</sub> is
 	    and accepting state and the other is not an accepting state, then set D[i,j] := 1
3. for every pair i, j, i < j, with D[i,j] = 0, do
 		3.1 if there exists an a which is element of Alphabet such that delta(q<sub>i</sub>, a) = q<sub>m</sub>,
 		delta(q<sub>j</sub>, a) = q<sub>n</sub> and D[m,n] = 1 or D[n,m] = 1, then DIST(i,j)

 		3.2 else for each a that is element of Alphabet, do: Let delta(q<sub>i</sub>, a) = q<sub>m</sub>,
 			delta(q<sub>j</sub>m a) = q<sub>n</sub>
 				if m < n and [i,j] /= [m,n], then add [i,j] to S[m,n]
 			else if m > n and [i,j] /= [n,m], then add [i,j] to S[n,m]
    end for

DIST(i,j);
begin
	D[i,j] := 1
	for all [m,n] that are elements of S[i,j], DIST(m,n)
end
"""
def determineEquivelantStatesOfDFA( dfa ):
    raise NotImplementedError

"""
input: an NFA-null M = (Q, Alphabet, TransitionFunction, q<sub>0</sub>,F)
		  input transition function t of M

1. initialize Q' to null-closure(q<sub>0</sub>)
2. repeat
	2.1 if there is a node X, X is element of Q' and a symbol a that's element of Alphabet
			with no arc leaving X labeled "a", then
			2.1.1 let Y = UNION over q<sub>i</sub>, where q<sub>i</sub> is element of X of
			  	  t(q<sub>i</sub>,a)
			2.1.2 if Y /= Q', then set Q' := Q UNION {Y}
			2.1.3 add an arc from X to Y labeled a
		else done:= true
	  until done
3. the set of accepting states of DM if F' = {X, where X is element of Q' | X contains
												 an element q<sub>i</sub> that is element of F}
"""
def constructEquivelantDFAFromNFA( nfa ):
    raise NotImplementedError
