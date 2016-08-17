import itertools

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
def constructRegExFromFiniteAutomaton( G ):
    q0 = G.initial()
    qt = list(G.final())[0] # should be only one final state in set
    while True:
        qi = [x for x in G.states.values() if x.name not in [q0.name, qt.name]][0]
        # delete the qi from G according to the following procedure
        for j,k in [(j,k) for j,k in list(itertools.product()) if qi.name not in [j.name, k.name])]:
            w_ji = [(a,t) for a in G.alphabet for t in nfa.events[a].transitions[j.name] if t.dest == qi.name]
            w_ik = [(a,t) for a in G.alphabet for t in nfa.events[a].transitions[qi.name] if t.dest == k.name]
            w_ii = [(a,t) for a in G.alphabet for t in nfa.events[a].transitions[qi.name] if t.dest == qi.name]
            if w_ji and w_ik and not w_ii:
                # add arc from j to k labeled w_ji-w_ik
            if w_ji and w_ik and w_ii:
                # add arc from j to k  labeled w_ji(w_ii)*w_ik
            jkArcs = [(a,t) for a in G.alphabet for t in nfa.events[a].transitions[j.name] if t.dest == k.name]
            if jkArcs:
                newSymbol = '_OR_'.join([a for a,_ in jkArcs]) # union of all symbols
                # remove all arcs
                for event in G.events.values():
                    for t in event.transitions.values():
                        if (t.source == j.name and t.dest == k.name): del event.transitions[t.source]
                # replace with new arc
                G.add_transition( newSymbol, j.name, k.name)
        # remove qi and all arcs incident to it in G
        for event in G.events.values():
            for t in event.transitions.values():
                if qi.name in [t.source,t.dest]: del event.transitions[t.source]
        del G.states[qi.name]
