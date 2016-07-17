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
						and rule A -> BC, then X<sub>i,i+step-1</sub> := X<sub>i,i+step-1</sub> UNION {A}
4. u is element of L(G) if S is element of X<sub>1,n</sub>
"""
def CYK( contextFreeGrammar, u):
    raise NotImplementedError
