from grammar import STARTSYMBOL

"""
Algorithm 4.6.1
CYK Algorithm

input: context-free-grammar G = (V, Alphabet, P, S)
		  string u = x<sub>1</sub>x<sub>2</sub>...x<sub>n</sub>, where x is element of Alphabet*

1. initialize all X<sub>i,j</sub> to EMPTY
2. for i = 1 to n
		for each variable A, if there is a rule A -> x<sub>i</sub> then
	    X<sub>i,i</sub> := X<sub>i,i</sub> UNION {A}
3. for step = 2 to n
		3.1 for i = 1 to n - step + 1
			3.1.1  for k = 1 to i + step - 2
						if there are variables B that are elements of X<sub>i,k</sub>,
						C that are elements of X<sub>k+1,i+step-1</sub>, and
						a rule A -> BC, then X<sub>i,i+step-1</sub> := X<sub>i,i+step-1</sub> UNION {A}
4. u is element of L(G) if S is element of X<sub>1,n</sub>
"""
def CYK( G, u):
    n = len(u)
    X = [[set() for i in range(n)] for j in range(n)]
    # Note: we are using 1-based indexing for the loops, but still have to
    #       access the lists using 0-based indexing. hence "-1" in list subscripts
    for i in range(1, n+1): # 1 to n
        for A in G.vars:
            # if there is a rule A -> x_i
            if any([Rule(A, u[i-1]) == rule for rule in G.rules]):
                X[i-1][i-1] |= {A}
    for step in range(2, n+1): # 2 to n
        for i in range(1, n - step + 1 + 1): # 1 to n - step + 1
            for k in range(1, i + step - 2 + 1) # 1 to i + step -2
                # if there are variables B that are elements of Xik, C
                # that are elements of Xk+1,i+step-1, and a rule
                # A -> BC, then Xi,i+step-1 = Xi,i+step-1 UNION {A}
                for rule in G.rules:
                    if len(rule.rhs) != 2:
                        continue
                    elif (rules.rhs[0] in X[i-1][k-1] and
                          rules.lhs[1] in X[k+1-1][i+step-1-1]):
                          A = rules.lhs[0]
                          X[i-1][i+step-1-1] |= {A}
    return True if STARTSYMBOL in X[1-1][n-1] else False
