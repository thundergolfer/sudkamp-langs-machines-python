from unrestricted import UnrestrictedGrammar


class ContextSensitiveGrammar(UnrestrictedGrammar):

    def validRule(self, r ):
        if not super(ContextFreeGrammar, self).validRule(r):
            return False
        elif len(r.rhs) < len(r.lhs):
            return False
        return True
