import pytest
from finite_state_machines import buildDfaWithEquivelantStates
import finiteAutomaton

class TestFiniteAutomatonAlgorithms(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDetermineEquivStates(self):
        dfa = buildDfaWithEquivelantStates()
        equivStates = finiteAutomaton.determineEquivelantStatesOfDFA( dfa )
        self.assertTrue( all(x in equivStates for x in ['q4','q5']))
