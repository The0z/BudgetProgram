class Category:

    def __init__(self, Category):
        self.categoryName = Category
        self.balance = 0
        self.ledger = list()

    # def create_spend_chart(categories):
    #    print("Hello World")

    def deposit(self, amount, description=""):
        self.balance = amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description="withdrawal"):
        # locate the item in the ledger
        for i in range(len(self.ledger)):
            if self.balance >= amount:
                self.ledger.append({"amount": -1*amount, "description":
                                    description})
                self.balance = self.balance - amount
                return True
            else:
                return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        # Enough funds Transfer return true
        dsc = "Transfer to " + category.categoryName
        if self.withdraw(amount, dsc):
            depDsc = "Transfer From " + self.categoryName
            category.deposit(amount, depDsc)
            return True
        # Not enough funds do not transfer return false
        else:
            return False

    def check_funds():
        return 0
