"""
Algorithm 18.2.1
Breadth-First Top-Down Parser

input: context free grammar G = (V, Alphabet, P, S)
		  string p, where p is element of Alphabet*
data structure: queue Q

1. initialize T with root S
   INSERT(S, Q)
2. repeat
		2.1 q := REMOVE(Q) 	(node to be expanded)
		2.2 i := 0 			(number of last rule used)
		2.3 done := false   (Boolean indicator of expansion completion)
		Let q = uAv where A is the leftmost variable in q
		2.4 repeat
			2.4.1 if there is no A rule numbered greater than i the done := true
			2.4.2 if not done then
					Let A -> w be the first A rule with number greater than i and
					let  j be the number of this rule
					2.4.2.1 if uwv is not element of Alphabet* and the terminal prefix of
						uwv matches a prefix of p then
							2.4.2.1.1 INSERT(uwv, Q)
							2.4.2.1.2 Add node uwv to T. Set a pointer from uwv to q
						end if
					end if
			2.4.3 i := j
		    until done or p = uwv
   until EMPTY(Q) or p = uwv
3. if p = uwv then accept else reject
"""
def breadthFirstTopDownParse( contextFreeGrammar, p):
    raise NotImplementedError

"""
Algorithm 18.4.1
Breath-First Bottom-Up Parser

input: context-free grammar G = (V, Alphabet, P, S)
		  string p, where p is element of Alphabet*
data structure: queue Q

1. initialize T with root p
	  INSERT(p, Q)
2. repeat
		q := REMOVE(Q)
		2.1 for each rule A -> w in P do
			2.2.1 for each decomposition uwv of q with v, where v is element of Alphabet* do
					2.1.1.1 INSERT(uAv, Q)
					2.1.1.2 Add node uAv to T. Set a pointer from uAv to q
				  end for
			end for
	  until q = S or EMPTY(Q)
3. if q = S then accept else reject
"""
def breadthFirstBottomUpParser( contextFreeGrammar, p):
    raise NotImplementedError
