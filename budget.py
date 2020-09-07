class Category:
    ledger = list()

    def __init__(self, Category):
        self.Category = Category
        self.balance = 0

    # def create_spend_chart(categories):
    #    print("Hello World")

    def deposit(self, amount, description=""):
        self.balance = amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description):
        # locate the item in the ledger
        for i in range(len(self.ledger)):
            if(self.ledger[i].get("amount") >= self.balance):
                print("amount > if")
                self.ledger.append({"amount": -1*amount, "description":
                                    "withdrawal"})
                self.balance = self.balance - amount
                return True
            else:
                return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        return 0

    def check_funds():
        return 0
