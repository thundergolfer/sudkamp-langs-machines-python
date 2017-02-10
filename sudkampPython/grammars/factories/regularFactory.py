from regular import RegularGrammar
from grammar import Rule, STARTSYMBOL

def build_RG_one():
    g = RegularGrammar()
    rules = []
    rules.extend( Rule([STARTSYMBOL], ["a","B"]), Rule([STARTSYMBOL], [None]),
                  Rule(["B"], ["b","S"]), Rule(["B"], ["b","A"]),
                  Rule(["A"], ["a","A"]), Rule(["A"], [None]))
    g.addRules(rules)

    return g

def build_RG_two():
    """
    a*(a*ba*ba*)*
    """
    g = RegularGrammar()
    rules = []
    rules.extend( Rule([STARTSYMBOL], ["a","S"]), Rule([STARTSYMBOL], ["b","B"]),
                  Rule([STARTSYMBOL], [None]), Rule(["B"], ["a","B"]),
                  Rule(["B"], ["b","S"]), Rule(["B"], ["b","C"]),
                  Rule(["C"], ["a","C"]), Rule(["C"], [None])
    g.addRules(rules)

    return g

def build_RG_three():
    """
    Most basic Regular Grammar.
    """
    g = RegularGrammar()
    rules = []
    rules.extend( Rule(["A"], ["a"]), Rule(["A"], ["a","B"]), Rule(["A"], [None]))
    g.addRules(rules)

    return g
