# Simple application: Text List
"""
How the app works
The user enters the text and the app creates a list of characters and displays the number of characters
"""
# How to use application:
"""
Take a copy of the following text, run the application, paste into the console, and then run the program
will showing Table Data in console and Draw in plots
"""
## Take following Text For example
d='Machine learning is a muhammad.mahmoud@gmail.com  form of AI that enables a system to learn from data rather than through explicit programming. However, machine learning is not a simple process. As the algorithms ingest training data, it is then possible to produce more precise models based on that data. A machine-learning model is the output generated when you train your machine-learning algorithm with data. After training, when you provide a model with an input, you will be given an output. For example, a predictive algorithm will create a predictive model. Then, when you provide the predictive model with data, you will receive a prediction based on the data that trained the model.Machine learning is a muhammad.mahmoud@gmail.com  muhammad.mahmoud@gmail.com programmer.muhammad@gmail.com'

# d='DataFrame هو: هيكل بيانات جدولي ثنائي الأبعاد قابل للتغيير ، يحتمل أن يكون غير متجانس مع محاور مسماة (صفوف وأعمدة). تتم محاذاة العمليات الحسابية على تسميات الصفوف والأعمدة. يمكن اعتباره بمثابة حاوية شبيهة بالديكت لكائنات السلسلة. هيكل بيانات الباندا الأولية.'

import pandas as pd
import matplotlib.pyplot as plt
import re


# a='This, is. A test!'.
# print(a)

class TextDisplay:
    def __init__(self):
        # self.__Text=input("Enter Text :") ## input text from user 
        self.__Text=d
        self.__colData=''
        self.__colCount='Count'
        self.__Data=[]
        self.__Dot='-----------------------------------------'
        print(self.__Dot)

    def CharsCount(self):
        self.__colData='Chars'
        textlower=self.__Text
        textlower=textlower.lower()#Convert all Chars to lower Case
        lstChars=[]#Create list empty to append Chars

        ##loop on text lower to Get Chars and Count for each Chars
        for i in textlower:
            ##Add  tuple(Chars,Count) in lstChars list.
            lstChars.append((i,textlower.count(i)))

        #Use function 'set' to  remove duplicates from list[(Chars,Count)]
        setChars=set(lstChars)

        ## to show all rwos in DataFrame
        pd.set_option('display.max_rows', None)
        #show data as a table
        dChars=pd.DataFrame(setChars,columns=[self.__colData,self.__colCount])
        #Cheange index by colChars column
        dChars=dChars.set_index(self.__colData)
        ##### d.set_index=np.arange(1, len(d)+1)

        #assighn to public list and sort data by count columns at Decs
        self.__Data=dChars.sort_values([self.__colCount],ascending=False)
        pd.set_option('colheader_justify', 'center')
        print(self.__Data)
        print(self.__Dot)

    def ShowMials(self):
        self.__colData='Emails'
        email=re.compile('\w+.\w+@\w+\.[a-z]{3}')
        emailFind=email.findall(self.__Text)
        setemail=set(emailFind)

        lenEmail=len(setemail)+1
        index=[]
        for i in range(1,lenEmail):
            index.append(i)

        if  setemail:
            self.__Data =pd.DataFrame(setemail,index=index,columns=[self.__colData])
            pd.set_option('colheader_justify', 'center')

            print(self.__Data)
            print(self.__Dot)
        else : 
            print ('Not Found Emails or No Text')
            print(self.__Dot)


    def WordCount(self):
        self.__colData='Words'
        textlower=self.__Text
        textlower=textlower.lower()#Convert all Chars to lower Case
        ##Replace each character in the string using the given translation table.

        # textlower= textlower.translate(str.maketrans('', '', string.punctuation))
        email=re.compile('\w+')
        emailFind=email.findall(textlower)
        # emailFind=list(emailFind)
        # setemail=set(emailFind)

        # splitWord=setemail.split()
        # print(emailFind)
        lstWord=[]#Create list empty to append Chars

        ##loop on text lower to Get Chars and Count for each Chars
        for i in emailFind:
            ##Add  tuple(Chars,Count) in lstChars list.
            lstWord.append((i,emailFind.count(i)))

        #Use function 'set' to  remove duplicates from list[(Chars,Count)]
        setChars=set(lstWord)
        # lenChars=len(setChars) +1
        # index=[]
        # for i in range(1,lenChars):
        #      index.append(i)
        ## to show all rwos in DataFrame
        pd.set_option('display.max_rows', None)
        #show data as a table
        dChars=pd.DataFrame(setChars,columns=[self.__colData,self.__colCount])
        #Cheange index by colChars column
        dChars=dChars.set_index(self.__colData)
        ##### d.set_index=np.arange(1, len(d)+1)

        #assighn to public list and sort data by count columns at Decs
        self.__Data=dChars.sort_values([self.__colCount],ascending=False)
        pd.set_option('colheader_justify', 'center')
        print(self.__Data)
        print(self.__Dot)

    def DataDraw(self):
        ## Draw data in plot 
        ax=plt.axes()
        ax.set_xlabel(self.__colData)#Set Chars to x label 
        ax.set_ylabel(self.__colCount)#Set Count to y label 
        #Add title in plot with format string
        title='Text Drawing:{0}{1}{2}'.format(self.__colCount,"|",self.__colData)
        ax.set_title(title)
        ## Draw plot with line and color blue  
        plt.plot(self.__Data,'b-')
        plt.legend([self.__colData])
        ## Save Image in hard disc
        plt.savefig(self.__colData+self.__colData+'Imge')
        plt.show()

    ##Function to Export data in Excel sheet to hard disc
    def ExportToExcel(self):
        self.__Data.to_excel(self.__colCount + self.__colData +'.xls',sheet_name=self.__colData)
        fileName='File Name Export: {0}{1}'.format(self.__colCount,self.__colData+'.xls')
        print(fileName)## print fileName on pyhton screen



a=TextDisplay()
a.WordCount()

# a.ShowMials()
# a.CharsCount()

a.ExportToExcel()
# a.DataDraw()