#Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος της ακολουθίας Fibonacci είναι πρώτος ή όχι. Για να απαντήσετε αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες επιλογές του a να ισχύει ότι a^p=a mod p. Ο κώδικάς σας παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.
#Για παράδειγμα:
#5ος όρος είναι ο 5 και είναι πρώτος.
#11ος όρος είναι ο 89 και είναι πρώτος.
#15ος όρος είναι ο 610 και δεν είναι πρώτος
import random

def fibonaci(number):

    if (number == 1 or number == 2 or number==3 or number==4):
      if number==1 or number==2:
        p = 1
      elif number==3:
        p=2
      else:
        p=3
     # print (p)

    else:
      previous = 1
      current = 2

      for i in range (2, number-1, 1):
        t = current
        current = previous + current
        previous = t
        p = current
       # print (p)


    return p

number = int(input("Doste ton oro: "))
p = fibonaci(number)

flag = True
i = 0

#-----------------------------
while (i < 20 and flag == True):
  a = random.randrange(0,100)
  #print(" tyxaios---", a)

  if ((a**p)%p != a % p):
   # print("a ^ p ---", a ** p)
   # print("a % p ---", a % p)
    #print(a ** p != a % p)
    flag = False
  
  i = i + 1
#-------------------------------
if (flag == True):
  print("ο", number,"ος όρος ειναί ο",p, "και  είναι πρώτος")
else:
  print("ο", number,"ος όρος ειναί ο",p, "και δεν είναι πρώτος")





