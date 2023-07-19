# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:52:37 2020

"""

import pandas as pd
import datetime as dt

class CreditCard:
   def __init__(self,name,no):
      self.__FullName=name
      self.__AccountNo=no
      self.__Information='Account Name: {0} --> Account No:  {1}'.format(self.__FullName,self.__AccountNo) +'\n'

      self.__DateTrans=dt.datetime.now()
      self.__DateTrans=self.__DateTrans.strftime("%x")
      self.__Transeaction=[]
      self.__DataTranseaction=[]
      self.__Dot='----------------------------------------'
      print(self.__Dot)

   def AddBalance(self,initial_balance):
      checkNumber=isinstance(initial_balance,int) or isinstance(initial_balance,float)
      if checkNumber:
         if  float(initial_balance) >= 1000:
             self.__Balance=initial_balance
             print('The amount has been new balance {0} :   '.format(self.__Balance))
         else :
            raise Exception("Initial balance is must be greater than 1000 EGP... ") 
      else:
         raise Exception("Initial balance is not digit ") 
      # self.__Balance=initial_balance
      self.__DateBalance=dt.datetime.now()
      self.__DateBalance=self.__DateBalance.strftime("%x")
      self.__InitialBalance=[(self.__DateBalance,'Balance',initial_balance)]

   def deposit(self,amount):
      checkNumber=isinstance(amount,int) or isinstance(amount,float)
      if checkNumber:
         Amount=float(amount)
         if Amount >0 :
            self.__Balance += Amount
            self.__Transeaction.append((self.__DateTrans,'deposit',Amount))
            print('The amount has been deposited {0}: '.format(Amount))
            print(self.__Dot)
         else:
               raise Exception("deposit amount is must be greater than 0 EGP... ") 
      else :
        raise Exception("Initial balance is not digit ") 

   def Withdrawal(self,amount):
      checkNumber=isinstance(amount,int) or isinstance(amount,float)
      if checkNumber:
         Amount=float(amount)
         if Amount > 0:
            if self.__Balance >= Amount:
               self.__Balance -= Amount
               self.__Transeaction.append((self.__DateTrans,'Withdrawal',0-Amount))
               print('The amount has been Withdrawal {0}: '.format(Amount))
            else:print('The Balance is not enough')
         else:
            raise Exception("Withdrawal amount is must be greater than 0 EGP... ") 
         print(self.__Dot)
      else : 
         raise Exception("Initial balance is not digit ") 

   def CurrentBalance(self):
      self.__BalanceMove=[(self.__DateBalance,'Balance',self.__Balance)]
      self.__DataTranseaction =pd.DataFrame(self.__BalanceMove,columns=['Trans Date ','Type','Amount'])
      print(self.__Information,self.__DataTranseaction)
      print(self.__Dot)

   def Transeaction(self):
      print(self.__Information)
      t=pd.DataFrame(self.__Transeaction,columns=['Trans Date ','Type','Amount'])
      b=pd.DataFrame(self.__InitialBalance,columns=['Trans Date ','Type','Amount'])
      self.__DataTranseaction=pd.merge(b,t,how='outer')
      print(self.__DataTranseaction) 
      print(self.__Dot)


act=CreditCard('muhammad mahmoud',1234567)
act.AddBalance(5000)
act.deposit(2000)
act.CurrentBalance()
act.Withdrawal(500)
act.Transeaction()

