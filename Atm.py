class Atm(object):
    def __init__(self,atmcardnumber,pinnumber):
        self.atmcardnumber = atmcardnumber
        self.pinnumber=pinnumber
        

    def CashWithdrawal(self):
        print("cash is withdrawed")

    def BalanceEnquiry(self):
        print("balance enquired")



person1= Atm("1234567890123456", "6969")
person2= Atm("3456901256781234" ,"9696")


print(person1.atmcardnumber)
print(person2.pinnumber)