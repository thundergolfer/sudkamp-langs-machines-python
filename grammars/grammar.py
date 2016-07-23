
STARTSYMBOL = "S"
ALT_STARTSYMBOL = "S`"

def isVariable( elem ):
    return True if elem.isupper() else (True if elem == ALT_STARTSYMBOL else False)

def isTerminal( elem ):
    return True if elem.isLower() else False

class Rule(object):

    def __init__(self, lhs, rhs=None):
        self.lhs = lhs.split(",")
        self.rhs = rhs.split(",")

    def __str__(self):
        if(self.rhs):
            return " ".join(self.lhs) + " -> " + " ".join(self.rhs)
        else:
            return " ".join(self.lhs) + " -> null"
