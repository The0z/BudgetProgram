class Category:

    def __init__(self, Category):
        self.categoryName = Category
        self.balance = 0
        self.ledger = list()

    def __str__(self):
        MAX_LEN = 30
        MAX_DSC = 23
        MAX_AMT = 7
        dsc = ""

        title = self.titleMaker(MAX_LEN)
        for i in range(len(self.ledger)):
            dsc = dsc + "\n" + self.descriptionMaker(MAX_DSC, MAX_AMT, i)
        return title + dsc

    def titleMaker(self, MAX_LEN):
        titleSize = len(self.categoryName)
        if(titleSize > MAX_LEN):
            title = self.categoryName[:MAX_LEN]
        else:
            stars = int((MAX_LEN - titleSize)/2)
            title = "*"*stars + self.categoryName + "*"*stars
            if(len(title) < MAX_LEN):
                title = title+"*"
        return title

    def descriptionMaker(self, MAX_DSC, MAX_AMT, i):
        dscSize = len(self.ledger[i].get("description"))
        if(dscSize > MAX_DSC):
            dsc = self.ledger[i].get("description")[:MAX_DSC]
        else:
            space = int(MAX_DSC - dscSize)
            dsc = self.ledger[i].get("description") + " "*space

        amtFormat = ("{:"+str(MAX_AMT)+".2f}").format(self.ledger[i].get(
                                                    "amount"))
        numSize = len(amtFormat)
        if(numSize > MAX_AMT):
            amt = amtFormat[0:MAX_AMT]
        else:
            space = int(MAX_AMT - numSize)
            amt = " "*space + amtFormat
        return dsc + amt

    def deposit(self, amount, description=""):
        self.balance = amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # locate the item in the ledger
        for i in range(len(self.ledger)):
            if self.check_funds(amount):
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
        if self.check_funds(amount):
            dsc = "Transfer to " + category.categoryName
            self.withdraw(amount, dsc)
            depDsc = "Transfer from " + self.categoryName
            category.deposit(amount, depDsc)
            return True
        # Not enough funds do not transfer return false
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    print("Hello World")
