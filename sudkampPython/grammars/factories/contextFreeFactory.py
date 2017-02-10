from contextFree import ContextFreeGrammar
from grammar import Rule

def buildCFGWithChainRules():
    g = ContextFreeGrammar()
    rules = []
    rules.extend( Rule(["A"],["a"]), Rule(["A"],["a","A"]), Rule(["A"],["B"]),
                  Rule(["B"],["b","B"]), Rule(["B"],["b"]), Rule(["B"],["C"]))
    g.addRules(rules)
    return g

def buildCFGWtihNullableVars():
    g = ContextFreeGrammar()
    rules = []
    rules.extend( Rule(["S"],["A","C","A"]), Rule(["A"],["a","A","a"]),
                  Rule(["A"],["B"]), Rule(["A"],["C"]), Rule(["B"],["b","B"],
                  Rule(["B"],["b"]), Rule(["C"],["c","C"]), Rule(["C"],[]))
    g.addRules(rules)
    return g

def buildCFGWithRecursiveStartSymbol():
    g = ContextFreeGrammar()
    rules = []
    rules.extend( Rule(["S"],["a","S"]), Rule(["S"],["A","B"]), Rule(["S"],["A","C"]),
                  Rule(["A"],["a","A"]), Rule(["A"],[]), Rule(["B"],["b","B"]),
                  Rule(["B"],["b","S"]), Rule(["C"],["c","C"]), Rule(["C"],[]))
    g.addRules(rules)
    return g

def buildCFGWithVarsThatDontDeriveTerminalStrings():
    g = ContextFreeGrammar()
    rules = []
    rules.extend( Rule(["S"],["A","C"]), Rule(["S"],["B","S"]), Rule(["S"],["B"]),
                  Rule(["A"],["a","A"]), Rule(["A"],["a","F"]), Rule(["B"],["C","F"]),
                  Rule(["B"],["b"]), Rule(["C"],["c","C"]), Rule(["C"],["D"]),
                  Rule(["D"],["a","D"]), Rule(["D"],["B","D"]), Rule(["D"],["C"]),
                  Rule(["E"],["a","A"]), Rule(["E"],["B","S","A"]), Rule(["F"],["b","B"]),
                  Rule(["F"],["b"]))
    g.addRules(rules)
    return g

def buildCFGForReachableVars:
    g = ContextFreeGrammar()
    rules = []
    rules.extend( Rule(["S"],["B","S"]), Rule(["S"],["B"]), Rule(["A"],["a","A"]),
                  Rule(["A"],["a","F"]), Rule(["B"],["b"]), Rule(["E"],["a","A"]),
                  Rule(["E"],["B","S","A"]), Rule(["F"],["b","B"]), Rule(["F"],["b"]))
    g.addRules(rules)
    return g
