#Classes
class Expense:
    
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.catefory =category
    
    def summarize(self, totalAmount):
        totalAmount.amount += totalAmount