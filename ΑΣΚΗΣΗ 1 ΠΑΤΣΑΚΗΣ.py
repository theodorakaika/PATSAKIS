#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση ενός τετραγώνου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα. Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και θα γεμίζει στην τύχη τις μισές με μονάδες (στρογγυλοποίηση προς τα πάνω). Σκοπός είναι να μετρήσετε πόσες τετράδες από μονάδες υπάρχουν οριζόντια, κάθετα, και διαγώνια. Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για την ίδια διάσταση) και επιστρέφει τον μέσο όρο των τετράδων.
import random

#------------------------------------- Συναρτήσεις
def printit(list):

  v = len(list[0]) # βάση v
  y = len(list) # ύψος y

  for j in range(y): 
    for i in range(v): 
      print(list[j][i], " ", end = '')
    print()

#------------------
def count1(list):
  counter = i = j = 0
  
  # έλεγχος στις γραμμές
  for row in range (i + 4):
    if list[row][j] == 1 and list[row][j + 1] == 1 and list[row][j + 2] == 1 and list[row][j+3]==1:
      counter = counter + 1

  # cέλεγχος στις στήλες
  for row in range (j + 4):
      if list[i][row] == 1 and list[i + 1][row]==1 and list[i + 2][row] == 1 and list[i+3][row]:
        counter = counter + 1

  # έλεγχος αριστερής διαγωνίου
  if list[i][j]==1 and list[i + 1][j + 1]==1 and list[i + 2][j + 2] == 1 and list[i+3][j+3]:
    counter = counter + 1

  # έλεγχος δεξιάς διαγωνίου
  if list[i + 3][j]==1 and list[i + 2][j + 1]==1 and list[i+1][j + 2] == 1 and list[i][j+3]==1:
    counter = counter + 1

  return counter

#------------------

def fillMe(list):

  v = len(list[0]) # βάση v
  y = len(list) # ύψος y
  found = 0 #τετραδες 1 που βρέθηκαν
  half = int ((v * y) / 2) # μισά στοιχεία

  for time in range(half):
    j = random.randrange(y)
    i = random.randrange(v)
    if list[j][i] == 1:
      list[j][i] = 0
      found += 1
    else:
      while list[j][i] == 1:
        i = random.randrange(v)
        j = random.randrange(y)
      list[j][i] = 1
      found += 1

  return found

#------------------
def getUserInput():
  
  wrongInput = True

  while wrongInput: # έλεγχος εισόδου χρήστη
    v = int(input("Δώστε βάση ορθογωνίου (v) >= 4: ")) # στήλες
    y = int(input("Δώστε ύψος ορθογωνίου (y) >= 4: ")) # γραμμές
    if (v >= 4 and y >= 4 ):
      wrongInput = False
    else: 
      print ("Δοκιμάστε ξανά..")
  
  show = False
  askForShow = input("Εκτύπωση ενδιάμεσων βημάτων; (y/n) ")
  if (askForShow == 'y'):
    show = True
  
  return (v, y, show)

#------------------------------------------------ Αλγόριθμος

v, y, show = getUserInput() # παραλαβή τιμών από τον χρήστη
total = v * y # total - πλήθος στοιχείων
theList = square = [] # square λίστα 
total1 = 0 # πόσες τετράδες 1 βρέθηκαν συνολικά
columns, rows = (v - 3, y - 3) #αρχικές τιμές για τα όρια
loops = 100

for repeat in range(loops):
  
  # αρχικοποίηση του πίνακα με 0
  theList = [[0 for i in range(v)] for j in range(y)]    
  found = fillMe(theList) 
  
  if show:
    if(repeat > 0):
      print("\n**** Νέος πίνακας ****")
    print('\nΠλήθος στοιχείων: ', total, " - κάθε θέση με 0.")
    print(found, " 1 τοποθετήθηκαν σε τυχαίες θέσεις.\n")
    print("Πίνακας (", repeat + 1, "):")
    printit(theList)
    print("στήλες = ", columns + 2, "\nγραμμές = ", rows + 2)

  g = s = loops1 = times = 0 # g γραμμή / s στήλη

  for j in range(rows):
    for i in range(columns): 
      square = [[theList[j + g][i + s] for s in range(s + 4)] for g in range(g + 4)]
      current1 = count1(square)
      total1 = total1 + current1
      if show:
        loops1 = loops1 + current1
        print("\n------- ", times + 1)
        print(square)
        printit(square)
        print("( ", current1, " ) τετράδες από 1 βρέθηκαν. ",)
      times = times + 1

  if show:
    print("\nΈγινε τελικός υπολογισμός για τον πίνακα No.", repeat + 1)
    print("Βρέθηκαν συνολικά:", loops1,"τετράδες 1 σε αυτόν.")

  loops1 = 0

print("\n\nΑποτέλεσμα υπολογισμών:")
print("Μετά από", repeat + 1, "επαναλήψεις βρέθηκαν", total1, " τετράδες 1 συνολικά .")
print("Ο μέσος όρος των τετραδών 1 στις", loops, "φορές είναι", total1 / loops)


  
  
    
    


  
