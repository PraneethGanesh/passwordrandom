# passwordrandom
import random
alphabet_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list=[0,1,2,3,4,5,6,7,8,9]
symbol_list=["!","@","#","$","%","^","&","*",":","~"]
password_list=[]
alpha=int(input("how many alphabet you want?"))
num=int(input("how many number you want?"))
sym=int(input("how many symbols you want?"))
for i in range(alpha):
 password_list.append(random.choice(alphabet_list))
for i in range(num):
 password_list.append(str(random.choice(number_list)))
for i in range(sym):
 password_list.append(random.choice(symbol_list)) 
random.shuffle(password_list)
password="".join(password_list)
print(password)