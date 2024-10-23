class Category:

    def __init__(self,name):
        self.name = name 
        self.ledger = []
    
    def get_balance(self):
       
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def check_funds(self,amount):
        if amount <= self.get_balance():
            return True
        return False
    def __str__(self):
       
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


    

    def deposit(self,amount,description=""):
        self.ledger.append({'amount':amount,'description': description})


    def withdraw (self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    def transfer(self, amount, category):
        # Проверяем, достаточно ли средств для перевода
        if self.check_funds(amount):
            # Если достаточно, выполняем перевод
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
   

    
   
        
def create_spend_chart(categories):
    # Chart header
    chart = "Percentage spent by category\n"

    # Calculate total spending for each category
    total_spent = 0
    category_spent = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])  # Summing up only withdrawals
        category_spent.append(spent)
        total_spent += spent

    # Calculate percentages
    percentages = [(spent / total_spent) * 100 for spent in category_spent]

    # Build vertical chart
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Separator line
    chart += "    -" + "---" * len(categories) + "\n"

    # Print category names horizontally
    max_len = max([len(category.name) for category in categories])
    for i in range(max_len):
        chart += "     "  # Padding to align with the chart bars
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "  # Add spaces if the category name is shorter
        chart += "\n"

    # Ensure there are no trailing spaces after the last character
    chart = chart.rstrip("\n")

    return chart





food = Category("food")
clothing = Category("clothing")

food.deposit(1000, "deposit")
food.withdraw(150, "dinner")
print(food)

clothing.deposit(500, "buy clothing")
food.transfer(200, clothing)
print(clothing)
print(create_spend_chart([food]))
