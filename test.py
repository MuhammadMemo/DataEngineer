print("hdddd")
import os 

SR=os.environ.get('SRC_BASE_DIR')
name=os.environ.get('DB_HOST')
print(name)
n=int(input("Enter number"))

if n%2 ==0 :
    print("even")
else :
    print ("odd")

