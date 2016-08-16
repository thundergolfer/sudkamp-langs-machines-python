from sudkampPython.transitions import Machine

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
             delta(q<sub>j</sub>m, a) = q<sub>n</sub>
                 if m < n and [i,j] != [m,n], then add [i,j] to S[m,n]
             else if m > n and [i,j] != [n,m], then add [i,j] to S[n,m]
    end for

DIST(i,j);
begin
    D[i,j] := 1
    for all [m,n] that are elements of S[i,j], DIST(m,n)
end
"""
def determineEquivelantStatesOfDFA( dfa ): # TODO: Improve algorithmic efficiency
    states = list(dfa.states.items())
    equivStates = set()
    D, S = [], []
    # initialization
    for i in range(len(states)):
        D.append([])
        S.append([])
        for j in range(len(states)):
            D[-1].append(False) if i < j else D[-1].append(None)
            S[-1].append(set()) if i < j else S[-1].append(None)
    # Step 2
    for i in range(len(states)):
        for j in range(len(states)):
            if (i < j and any(s.is_final() for s in states[i:j+1])
                     and not all(s.is_final() for s in states[i:j+1])):
                # one is final and other isn't
                D[i][j] = 1
    # Step 3
    for i in range(len(states)):
        for j in range(len(states)):
            if i < j and D[i][j] == 0: # Do
                # if there is an "a" for which both qi and qj have a transition and the
                # resulting state m,n are not equal (m!=n) and D[m][n] or D[n][m] == 1 then
                # DIST(i,j)
                # 3.1
                for symbol in dfa.alphabet.keys():
                    qi_transition = getTransitionWithSymbol( symbol, states[i].name )
                    qj_transition = getTransitionWithSymbol( symbol, states[j].name )
                    m_state_name, n_state_name = qi_transition.dest, qj_transition.dest
                    # get indexes
                    m = [s.name for s in states].index(m_state_name)
                    n = [s.name for s in states].index(n_state_name)
                    if D[m][n] == 1 or D[n][m] == 1: # if n = m, D[n,m] will never equal 1
                        DIST(i, j, D, S)
                # 3.2
                for symbol in dfa.alphabet.key():
                    qi_transition = getTransitionWithSymbol( symbol, states[i].name )
                    qj_transition = getTransitionWithSymbol( symbol, states[j].name )
                    m_state_name, n_state_name = qi_transition.dest, qj_transition.dest
                    # get indexes
                    m = [s.name for s in states].index(m_state_name)
                    n = [s.name for s in states].index(n_state_name)
                    if m < n and (i,j) != (m,n):
                        S[m][n].add((i,j))
                    elif m > n and (i,j) != (n,m):
                        S[n][m].add((i,j))

    # Now determine the set of equiv states. If D[i][j] = 0 then i and j are equiv
    for i in range(len(states)):
        for j in  range(len(states)):
            if D[i][j] == 0:
                equivStates.add(states[i])
                equivStates.add(states[j])
    return equivStates

def DIST(i, j, D, S):
    """ Helper function for our main algorithm """
    D[i][j] = 1
    for m,n in S[i][j]:
        DIST(m, n, D, S)

def getTransitionWithSymbol( dfa, symbol, source ):
    """
    Find a transition, if one exists, that involves the named
    symbol and source
    """
    for event in dfa.events.keys():
        for transition in event.transitions.values():
            if event == symbol and transition.source == source:
                return transition

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
3. the set of accepting states of DM is F' = {X, where X is element of Q' | X contains
                                                 an element q<sub>i</sub> that is element of F}
"""
def constructEquivelantDFAFromNFA( nfa ):
    dfa = Machine( model=None, states=nfa.initial.name, initial=nfa.initial.name, transitions=None)
    Q_ = nullClosure(nfa, nfa.initial) # state q0
    while  True:
        for X in Q_:
            validSymbols = [sym for sym in nfa.alphabet if not nfa.events[sym].transitions[X.name]]
            if validSymbols:
                a = validSymbols[0]
                destinations = [t.dest for qi in X for t in nfa.events[a].transitions[qi.name]]
                Y = set([nfa.states[x] for x in destinations])
                if Y != Q_:
                    Q_ |= Y
                dfa.add_transition(a, str(X), str(Y))
            else: # done = true
                break
    # the set of final states in F'
    F_ = [X for X in Q_ if any(q in X for q in nfa.final_states)]


def nullClosure( machine, state ):
    """ Calculate the set of states that can be reached without processing a symbol """
    closureSet = set()
    closureSet.add(state)
    # TODO: If "*" trigger doesn't exist then we can just return the set with just the named state?
    while True: # do
        prev = set(closureSet) # update previous states set
        # add all states that can be reached by null
        for state in closureSet:
            reachableWithNull = [t.dest for t in machine.events['*'].transitions[state.name]]
            closureSet |= set(reachableWithNull)
        if prev == closureSet: # has closureSet changed?
            break
    return closureSet
