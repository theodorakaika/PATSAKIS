#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει τις διαστάσεις ενός ορθογωνίου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα. Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και γεμίζει στην τύχη τις μισές με S και τις μισές με O. Σκοπός είναι να μετρήσετε πόσες φορές εμφανίζεται το SOS οριζόντια, κάθετα, και διαγώνια. Το πρόγραμμα επαναλαμβάνεται 100 φορές (για τις ίδιες διαστάσεις) και επιστρέφει τον μέσο όρο των τριάδων SOS.
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
def countSOS(list):
  counter = i = j = 0
  
  # έλεγχος στις γραμμές
  for row in range (i + 3):
    if list[row][j] == "S" and list[row][j + 1] == "O" and list[row][j + 2] == "S" :
      counter = counter + 1

  # έλεγχος στις στήλες
  for row in range (j + 3):
      if list[i][row] == "S" and list[i + 1][row]=="O" and list[i + 2][row] == "S" :
        counter = counter + 1

  # έλεγχος αριστερής διαγωνίου
  if list[i][j]=="S" and list[i + 1][j + 1]=="O" and list[i + 2][j + 2] == "S" :
    counter = counter + 1

  # έλεγχος δεξιάς διαγωνίου
  if list[i + 2][j]=="S" and list[i + 1][j + 1]=="O" and list[i][j + 2] == "S" :
    counter = counter + 1

  return counter

#------------------

def fillMe(list):

  v = len(list[0]) # βάση v
  y = len(list) # ύψος y
  found = 0 #SOS που βρέθηκαν
  half = int ((v * y) / 2) # μισά στοιχεία

  for time in range(half):
    j = random.randrange(y)
    i = random.randrange(v)
    if list[j][i] == "O":
      list[j][i] = "S"
      found += 1
    else:
      while list[j][i] == "S":
        i = random.randrange(v)
        j = random.randrange(y)
      list[j][i] = "S"
      found += 1

  return found

#------------------
def getUserInput():
  
  wrongInput = True

  while wrongInput: # έλεγχος εισόδου χρήστη
    v = int(input("Δώστε βάση ορθογωνίου (v) >= 3: ")) # στήλες
    y = int(input("Δώστε ύψος ορθογωνίου (y) >= 3: ")) # γραμμές
    if (v >= 3 and y >= 3 ):
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
totalSOS = 0 # πόσα SOS βρέθηκαν συνολικά
columns, rows = (v - 2, y - 2) #αρχικές τιμές για τα όρια
loops = 100

for repeat in range(loops):
  
  # αρχικοποίηση του πίνακα με O
  theList = [["O" for i in range(v)] for j in range(y)]    
  found = fillMe(theList) # τοποθέτηση τυχαίων 'S'
  
  if show:
    if(repeat > 0):
      print("\n**** Νέος πίνακας ****")
    print('\nΠλήθος στοιχείων: ', total, " - κάθε θέση με 'O'.")
    print(found, " 'S' τοποθετήθηκαν σε τυχαίες θέσεις.\n")
    print("Πίνακας (", repeat + 1, "):")
    printit(theList)
    print("στήλες = ", columns + 2, "\nγραμμές = ", rows + 2)

  g = s = loopsSOS = times = 0 # g γραμμή / s στήλη

  for j in range(rows):
    for i in range(columns): 
      square = [[theList[j + g][i + s] for s in range(s + 3)] for g in range(g + 3)]
      currentSOS = countSOS(square)
      totalSOS = totalSOS + currentSOS
      if show:
        loopsSOS = loopsSOS+ currentSOS
        print("\n------- ", times + 1)
        print(square)
        printit(square)
        print("( ", currentSOS, " ) SOS που βρέθηκαν. ",)
      times = times + 1

  if show:
    print("\nΈγινε τελικός υπολογισμός για τον πίνακα No.", repeat + 1)
    print("Βρέθηκαν συνολικά:", loopsSOS,"SOS σε αυτόν.")

  loopsSOS = 0

print("\n\nΑποτέλεσμα υπολογισμών:")
print("Μετά από", repeat + 1, "επαναλήψεις βρέθηκαν", totalSOS, " SOS συνολικά .")
print("Ο μέσος όρος των SOS στις", loops, "φορές είναι", totalSOS / loops)


  
  
    
    


  
