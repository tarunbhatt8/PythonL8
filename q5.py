'''Q.5- Create a class Expenditure and initialize it with salary,savings, category , total expenditure.Make the following methods.
1. Add expenditure according to category .
2. Calculate total expenditure.
3. Calculate per day and monthly expenditure.
'''

class Expenditure:
    ''' class to add and calculate expenditure'''

    def __init__(self):
        self.salary=120000.0
        self.savings=18000.0
        self.category='m'
        self.totalexp=18000.0

    def AddExpenditure(self,category):
        '''method to add expenditure according to category'''
        if category=='f':
            self.category=category
            self.expenditure=36000.0
        elif category=='m':
            self.category=category
            self.expenditure=18000.0

    def CalcTotalExp(self):
        '''method to calculate total expenditure'''
        self.totalexp+=self.expenditure

    def CalcPerDayAndMonthlyExp(self):
        ''''method to calculate per day and monthly expenditure'''
        self.perDayExp=self.totalexp/365
        self.monthlyExp=self.totalexp/12


    def Display(self):
        '''method to display expenditure information'''
        print("Salary",self.salary,"\n")
        print("Savings",self.savings,"\n")
        print("Category",self.category,"\n")
        print("Expenditure",self.expenditure,"\n")
        print("Total Expenditure",self.totalexp,"\n")
        print("Per Month Expenditur",self.monthlyExp,"\n")
        print("Daily Expenditure",self.perDayExp,"\n")


ch='y'
while ch=='y':
    cat=input("Enter category: ")
    e1=Expenditure()
    e1.AddExpenditure(cat)
    e1.CalcTotalExp()
    e1.CalcPerDayAndMonthlyExp()
    e1.Display()

    ch=input("Do you want to enter more cases?? y\\n: ")

print("Program Ended")
