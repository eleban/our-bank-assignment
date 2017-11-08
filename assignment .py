class Bank(object):
    def __init__(self, BankId, Bankname, Location):
        self.BankId = BankId
        self.Bankname = Bankname
        self.Location = Location


class Customer(Bank):
    def __init__(self,BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Customer, self).__init__(BankId, Bankname, Location)
        self.accounts = {}
        self.CustomerId = CustomerId
        self.AcctNo = AccountNo
        self.Name = Name
        self.Address = Address
        self.PhoneNo = PhoneNo

    def GeneralInquiry(self):
        try:
            a = self.accounts[self.CustomerId]['CustomerId']
            b = self.accounts[self.CustomerId]['Name']
            c = self.accounts[self.CustomerId]['Address']
            d = self.accounts[self.CustomerId]['PhoneNo']
            e = self.accounts[self.CustomerId][self.AcctNo]['accountNumber']
            f = self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']
            print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
            print('CustomerId: %s\nCustomer_Name: %s\nAddress: %s\nPhoneNo.: %s \n' % (a, b, c, d))
            print('AccountNo: %s\nAccountBalance: %s\n' % (e, f))
            try:
                x = self.accounts[self.CustomerId]['loan']['loanbalance']
                y = self.accounts[self.CustomerId]['loan']['loanType']
                print('Active_Loan: %s\n' % x)
                print('loan Type: %s\n' % y)
            except:
                print('Loan account not activated')
        except:
            print('no account activated!')

    def OpenAccount(self):
                self.accounts[self.CustomerId] = {}
                self.accounts[self.CustomerId]['Name'] = self.Name
                self.accounts[self.CustomerId]['CustomerId'] = self.CustomerId
                self.accounts[self.CustomerId]['Address'] = self.Address
                self.accounts[self.CustomerId]['PhoneNo'] = self.PhoneNo
                self.accounts[self.CustomerId][self.AcctNo] = {}
                self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
                self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] = 0
                return self.accounts

    def DepositMoney(self, amount):
        self.amount = amount
        if self.amount >= 0:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.amount

    def WithdrawMoney(self, value):
        self.value = value
        if 0 < self.value < self.accounts[self.CustomerId][self.AcctNo]['AccountBalance']:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] -= self.value
        else:
            print('INSUFFICIENT BALANCE')


    def CloseAccount(self):
        del self.accounts[self.CustomerId]

    def ApplyForLoan(self, loanamount):
        self.loanamount = loanamount
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('application not accepted')
        if self.loanamount > (1.8 * (self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('you are not eligible')
        else:
            print('your Request has been Successful')

    def RequestCard(self):
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Your are not eligible for Card please create an account first!')


class Teller(Customer, Bank):
    def __init__(self,TellerName, TellerId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Teller, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.TellerName = TellerName
        self.TellerId = TellerId

    def CollectMoney(self):
        if self.amount > 0:
            self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'] += self.amount
        else:
            print('INPUT AMOUNT GREATER THAN ZERO')

    def LoanRequest(self, loanId ,Type):
        self.loanType = Type
        self.loanId = loanId
        try:
            self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] = self.AcctNo
        except:
            print('Your are not eligible for a loan')
        if self.loanamount > (1.8*(self.accounts[self.CustomerId][self.AcctNo]['AccountBalance'])):
            print('Your not eligible')
        else:
            self.accounts[self.CustomerId]['loan'] = {}
            self.accounts[self.CustomerId]['loan']['loanId'] = self.loanId
            self.accounts[self.CustomerId]['loan']['loanType'] = self.loanType
            self.accounts[self.CustomerId]['loan']['loanbalance'] = -self.loanamount
            print('LOAN ACCOUNT  ACCEPTED!')

    def ProvideInfo(self):
        print('Bank ID:%s\nBank Name: %s\nBank Location: %s\n' % (self.BankId, self.Bankname, self.Location))
        print('Teller Id: %s\nTeller Name: %s\n' % (self.TellerId, self.TellerName))

    def IssueCard(self):
        if self.accounts[self.CustomerId][self.AcctNo]['accountNumber'] == self.AcctNo:
            print('Your request  for card was received and your Card is ready')
        else:
            print('Not eligible for card issuing')


class Account(Customer):
    pass


class Loan(Customer):
    def __init__(self, LoanId, Type, AccountId, BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo):
        super(Loan, self).__init__(BankId, Bankname, Location, CustomerId, AccountNo, Name, Address, PhoneNo)
        self.LoanId = LoanId
        self.Type = Type
        self.AcctNo = AccountId


BANK_one = Bank(1, 'BRIEF BANK', 'MASAKA')
BANK_two = Bank(2, 'HALK BANK', 'MBARARA')

p = int(input('Enter the Id of the Bank:\n'))
q = input('Enter the Bank Name: \n')
r = input('Enter the bank location:\n')
s = input('if your a customer enter C or if a teller enter T:\n')
if s == 'C':
    j = 1
    while j < 11:
        j += 1
        L, M, N, O = input('Enter Customer Name:\n'), input('Enter your Address:\n'), \
                     int(input('Enter your phone Number')), input('Enter Your Account Number:\n')
        Cus_1 = Customer(p, q, r, s, L, M, N, O)
        while True:
            E = int(input('Enter: 1 for General inquiry ,2 Open Account ,3 for Depositing , 4 for withdrawing, 5 for Requesting,'
                          ' 6 for Loan Application, , 7 Close Account, 8 Quit'))
            if E == 1:
                Cus_1.GeneralInquiry()
            elif E == 2:
                F = int(input('Please enter the amount you want to deposit in figure\n'))
                Cus_1.DepositMoney(F)
            elif E == 3:
                G = int('Please enter the amount you want to withdraw\n')
                Cus_1.WithdrawMoney(G)
            elif E == 4:
                Cus_1.RequestCard()
            elif E == 5:
                H = input('Enter the amount of loan you need in figures\n')
                Cus_1.ApplyForLoan(H)
            elif E == 6:
                Cus_1.OpenAccount()
            elif E == 7:
                Cus_1.CloseAccount()
            elif E == 8:
                break
elif s =='T':
    a, b, c, d, e, f, g = input('Teller Name:\n'), input('TellerID:\n'), input('Enter Customer Name:\n'),\
                          input('Enter your Address:\n'), int(input('Enter your phone Number')),\
                        input('Enter Your Account Number:\n'), input('Enter CustomerId:')
    Teller = Teller(a, b, p, q, r, g, f, c, d, e)

    while True:
        while True:
            h = int(input('Enter: 1 for General inquiry\n , 2 for Depositing\n , 3 for withdrawing\n, 4 for Requesting\n,'
                          ' 5 for Loan Application\n, 6 Open Account\n, 7 Close Account\n, 8 Quit\n, 9 Provide Info\n, '
                          '10  Work on loan Request\n, 11 IssueCard\n,'))
            if h == 1:
                Teller.GeneralInquiry()
            elif h == 2:
                F = int(input('Please enter the amount you want to deposit in figure\n'))
                Teller.DepositMoney(F)
            elif h == 3:
                G = int('Please enter the amount you want to withdraw\n')
                Teller.WithdrawMoney(G)
            elif h == 4:
                Teller.RequestCard()
            elif h == 5:
                H = input('Enter the amount of loan you need in figures\n')
                Teller.ApplyForLoan(H)
            elif h == 6:
                Teller.OpenAccount()
            elif h == 7:
                Teller.CloseAccount()
            elif h == 8:
                break
            elif h == 9:
                Teller.ProvideInfo()
            elif h == 10:
                U = int(input('Please Enter loanId for the  Customer:'))
                t = input('Enter loan type requested by Customer:')
                Teller.LoanRequest(U, t)
            elif h == 11:
                Teller.IssueCard()
































