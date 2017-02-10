from contextSensitive import ContextSensitiveGrammar
from grammar import Rule, STARTSYMBOL

def build_CSG_one():
    """
    Generates {a^ib^ic^i | i > 0}.
    """
    g = ContextSensitiveGrammar()
    rules = []
    rules.extend( Rule([STARTSYMBOL], ["a","A","b","c"]), Rule([STARTSYMBOL], ["a","b","c"]),
                  Rule(["A"], ["a","A","b","C"]), Rule(["A"], ["a","b","C"]))
    g.addRules(rules)

    return g

def build_CSG_two():
    raise NotImplementedError
