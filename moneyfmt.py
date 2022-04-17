class Moneyfmt:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        if self.amount >= 0:
            return '${:,.2f}'.format(self.amount)
        else:
            return '-${:,.2f}'.format(self.amount)

    def update(self, new):
        self.amount = new
        return new

    def repr(self):
        return float(self.amount)

