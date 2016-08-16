"""
Algorithm 6.2.2
Construction of a Regular Expression from a Finite Automaton

input: state diagram G of a finite automaton with one accepting state

Let q0 be the start state and qt the accepting state of G.
1. repeat
    1.1 choose a node qi that is neither q0 not qt
    1.2 delete the node qi from G according to the following procedure:
        1.2.1 for every j,k not equal to i (this includes j=k) do
                i) if w_ji != ∅, w_ik != ∅ and w_ii != ∅, then add an arc
                    from node j to node k labeled w_jiw_ik
                ii) if w_ji != ∅, w_ik != ∅ and w_ii != ∅, then add an arc from
                    node qj to node qk labeled w_ji(w_ii)*w_ik
                iii) if nodes qj and qk have arcs labeled w1, w2,..., ws
                     connecting them, then replace the arcs by a single arc
                     labeled w1 ∪ w2 ∪ ... ∪ ws
        1.2.2 remove the node qi and all arcs incident to it in G
   until the only nodes in G are q0 and qt
2. determine the expression accepted by G
"""
def constructRegExFromFiniteAutomaton( finiteAutomaton ):
    raise NotImplementedError
