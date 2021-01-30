#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα στον αντίστοιχο αριθμό ASCII και κρατάει τους μονούς. Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με “μπάρες” χρησιμοποιώντας το χαρακτήρα '*', όπου κάθε  αντιστοιχεί σε 1%. Η στρογγυλοποίηση θα γίνει προς τα πάνω.

import math
#----------------------------------
def printStars(chr, total, fr, show):
  times = (fr/total) * 100
  if (show):
    print(f'\n( {times:.5} ) --> {math.ceil(times)} stars')
  print(chr, ': ', end='')
  for i in range(math.ceil(times)):
    print ('*',end='') 
  print ()
#----------------------------------
frequency = {}
document_text = open('two_cities.txt', 'r')
text_string = document_text.read()

letters = 'abcdefhigklmnopqrstuwxyzABCDEFHIGKLMNOPQRSTUWXYZ'

for ch in text_string:
    # γράμματα με μονούς ascii κωδικούς
    if (((ord(ch) % 2) != 0) and (ch in letters)):
      count = frequency.get(ch,0)
      frequency[ch] = count + 1
     
frequency_list = frequency.keys()

show = False;

  

sumchars = sum(frequency.values())
if(show):
  print('\nΠλήθος:', sumchars)

for chr in frequency:
  printStars(chr, sumchars, frequency.get(chr), show)
