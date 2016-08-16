from grammar import isVariable, isTerminal, STARTSYMBOL, ALT_STARTSYMBOL

class UnrestrictedGrammar(object):

    def __init__(self):
        self.rules = []
        self.vars = set()
        self.terminals = set()

    def __str__(self):
        output = ""
        output += "VARIABLES: " + ",".join(self.vars) + '\n'
        output += "TERMINALS: " + ",".join(self.terminals) + '\n'
        output += "RULES: " + '\n' + [(str(rule) + '\n') for rule in self.rules]
        return output

    def addRules( rules ):
        if all(validRule(r) for r in rules):
            self.rules.extend(rules)
            return True
        else:
            return False

    def addRule( self, r ):
        if validRule(r):
            self.rules.append(r)
            return True
        else: return False

    def validRule( self, r ):
        if r.lhs: return True
        else: return False

    def updateVarsAndTerminals(self, rule=None):
        if rule:
            self.vars.update([x for x in (rule.lhs + rule.rhs) if isVariable(x)])
            self.terminals.update([x for x in (rule.lhs + rule.rhs) if isTerminal(x)])
        else:
            self.vars = set()
            self.terminals = set()
            for r in self.rules:
                updateVarsAndTerminals(self, rule=r)

    def getStartSymbol(self):
        return ALT_STARTSYMBOL if ALT_STARTSYMBOL in self.vars else STARTSYMBOL
