from collections import deque

from grammars.grammar import STARTSYMBOL

"""
Algorithm 18.2.1
Breadth-First Top-Down Parser

input: context free grammar G = (V, Alphabet, P, S)
          string p, where p is element of Alphabet*
data structure: queue Q

1. initialize T with root S
   INSERT(S, Q)
2. repeat
        2.1 q := REMOVE(Q)     (node to be expanded)
        2.2 i := 0             (number of last rule used)
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
def breadthFirstTopDownParse( G, p, Q):
    S = Node( STARTSYMBOL )
    T = SearchTree( S )
    INSERT( S, Q )
    while True: # repeat
        q = REMOVE(Q)
        i = 0
        done = False
        u, A, v = uAv_structure( q.sentForm )
        while True: # repeat
            validRules = [(j, rule) for j, rule in enumerate(G.rules) if (rule.lhs == A) and (j > i)]
            if not validRules:
                done = True
            if not done:
                A, w = validRules[0][1].lhs, validRules[0][1].rhs # rule A -> w
                j = validRules[0][0]
                if (not all(x.islower() for x in u+w+v) and
                    ***the terminal prefix of uwv matches a prefix of p***):
                    uwv = Node(u+w+v)
                    INSERT( uwv, Q )
                    uwv.parent = q # and add uwv to T
            i = j
            if done or p == uwv: break # until
        if EMPTY(Q) or p == uwv
    return True if p == uwv else False

def uAv_structure( sentForm ):
    raise NotImplementedError

def INSERT( x, Q ):
    """ places the string x at the rear of the queue """
    return Q.append(x)

def REMOVE( Q ):
    """ returns the item at the front of Q and deletes it from Q. """
    return Q.popleft()

def EMPTY( Q ):
    """ boolean function that returns true if queue is empty, false otherwise. """
    return len(Q) == 0

class Node( object ):
    """ A node to be a part of the search tree T. Contains a sentential form. """
    def __init__(self, sentForm, parent=None ):
        self.parent = parent
        self.sentForm = sentForm

class SearchTree( object ):
    """
    The 'implicit tree' of a grammar is the tree of possible derivation
    paths in that grammar. This 'search tree' is the portion of the implicit
    tree that is examined during the parse.
    """
    def __init__(self, root=None):
        self.root = root
    # TODO: expand class to fulfil its function within the parsers


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
