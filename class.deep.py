class Account():
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    def get_balance(self):
        print(f"{self.__owner} has {self.__amount}")

    def deposit(self, amount):
        print("Deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("Withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder setter running")
        self.__owner = new_owner


my_account = Account("John", 5000)
my_account.get_balance()

print("===")
my_account.deposit(600)
my_account.withdraw(300)
my_account.get_balance()
print("===")

try:
    result = my_account.__amount
    print(result)
except Exception as err:
    print(err)

print("Owner before:", my_account.holder)  # state
my_account.holder = "Nade"
print("Owner after:", my_account.holder)  # state
