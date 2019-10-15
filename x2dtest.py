import random
import sys
import pickle
import os

import matplotlib.pyplot as plt


randomInputs = False
tally = []
rolls = 0
dye = 0
filename = ""

x = 1
for x in range(1, len(sys.argv)):
    if 'rand' in sys.argv[x]:
        randomInputs = True
        print( "Randomizing inputs!" )
    elif os.path.exists(sys.argv[x]) and os.path.isfile(sys.argv[x]):
        filename = sys.argv[x]
        print( "Unpickling "+filename)
        with open(filename, "rb") as fp:   # Unpickling
            tally = pickle.load(fp)
        print( "Load tally from " + filename)
        # deriving previous data points
        dye = len(tally)
        rolls = sum(tally)
        print( "Concluded data is regarding a d"+str(dye)+", which has been rolled "+str(rolls)+" already.")

if dye == 0:
    while True:
        try:
            dye = int(input("How many sides does your dye have: d"))
            break
        except ValueError:
            print("Invalid dye side. Try again. \n.")
            #better try again... Return to the start of the loop
            continue

while True:
    try:
        rolls = rolls + int(input("How many times do you want to roll? (recommended 5 * the dye size, ie 200 for a d20): "))
        break
    except ValueError:
        print(("Invalid dye side. Try again. \n."))
        #better try again... Return to the start of the loop
        continue


if(len(tally) == 0):
    tally = [0] * (dye)

print( "Rolling a "+str(dye)+"-sided dye "+ str(rolls-sum(tally))+" times. \n")

for i in range(sum(tally), rolls):
    print( str(i)+"/"+str(rolls))
    while True:
        try:
            if randomInputs:
                val = random.randint(1,dye)
            else:
                val = int(input("Enter your value: "))
        except ValueError:
            print(("Invalid dye side. Try again. \n."))
            #better try again... Return to the start of the loop
            continue
        
        if val > 0 and val <= (dye):
            break
        else:
            print("Value must be between "+str(1)+" and "+str(dye) + " (inclusive)")
            continue

    tally[val-1] = tally[val-1]+1

    i+=1

print( "Results for each side hit:")

N = sum(tally)
Nexp = float(rolls) / float(dye)
X2 = 0.0

print( "Nexp " + str(Nexp))
print( "X2 " + str(X2))

print( "---------------")
print( "|  si  |  hi  |")
print( "---------------")
for i in range(len(tally)):
    hits = tally[i]

    side = i+1

    if(hits >= 100):
        hi = str(hits) + "  |"
    elif(hits >= 10):
        hi = str(hits) + "   |"
    else:
        hi = str(hits) + "    |"

    if(side >= 100):
        si = str(side) + " | "
    if(side >= 10):
        si = str(side) + " | "
    else:
        si = str(side) + "  | "

    print( "| "+ si + hi)

    X2 = X2 + ((tally[i] - Nexp)**2.0) / Nexp

print( "---------------")

print( "v = "+str(dye-1))
print( "X2 = "+str(X2))
print( "https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm")

plt.bar([x for x in range(dye)], tally)
plt.show()

while True:
    try:
        saveTally = input("Save tally? [y/n/o]: ")
        if(saveTally == "n"):
            saveTally = False
            break
        elif(saveTally == "y"):
            saveTally = True
            filename = ""
            break
        elif(saveTally == "o"):
            saveTally = True
            break
        else:
            print( "Invalid input")
            continue

    except ValueError:
        print( "Invalid dye side. Try again. \n.")
        #better try again... Return to the start of the loop
        continue

while True and saveTally:
    try:
        if( filename == ""):
            filename = input("filename: ")
        
        
        with open(filename, "wb") as fp:   #Pickling
            pickle.dump(tally, fp)
        
        print( filename + " saved successfully.")

        break

    except ValueError:
        print( "Invalid filename... or some such. Try again. \n.")
        #better try again... Return to the start of the loop
        continue


