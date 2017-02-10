from unrestricted import UnrestrictedGrammar
from grammar import Rule, STARTSYMBOL

def build_UG_one():
    g = UnrestrictedGrammar()
    rules = []
    rules.extend( Rule([STARTSYMBOL], ["a","A","b","c"]), Rule([STARTSYMBOL],[None]),
                  Rule(["A"], ["a","A","b","C"], Rule(["A"],[None])),
                  Rule(["C","b"], ["b","C"]), Rule(["C","c"], ["c","c"]))
    g.addRules(rules)
    
    return g
