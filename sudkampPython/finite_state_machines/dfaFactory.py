from  transitions import Machine

def buildDfaWithEquivelantStates():
    """
    This DFA contains equivelant states and can be used to test the
    'determination of equivelant states' algorithm.
    """

    states = ['q0','q1','q2','q3','q4','q5']
    transitions = [['a', 'q0','q1'],['b', 'q0', 'q2'],['b', 'q1', 'q4'],
                    ['a', 'q1', 'q3'],['a', 'q2', 'q3'],['b', 'q2', 'q5'],
                    ['a', 'q3', 'q3'],['b', 'q3', 'q3'],['a', 'q4', 'q4'],
                    ['b', 'q4', 'q4'],['a', 'q5', 'q5'],['b', 'q5', 'q5']]
    dfa = Machine(model=None, states=states, transitions=transitions, initial='q0')
    dfa.add_transition(trigger='a', source='q0', dest='q1')
    dfa.set_final('q4')
    dfa.set_final('q5')
