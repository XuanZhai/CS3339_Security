import hashlib
from multiprocessing import Manager,Pool
import string

Find = ""

def SetFind(newFind):
    global Find
    Find = newFind
    
def GetFind():
    return Find


def checkhash(salt,nhash,newline):                  # Check whether it's the right answer
    salted_word = (salt + newline).encode('utf-8')
    hash_value = hashlib.sha256(salted_word).hexdigest()
    if hash_value == nhash:
        return True
    else:
        return False
    

def ReCalculation(arr,length,start,result,nhash,salt):      # Use Brute Force method to find the answer
    if length == 0 or GetFind() != "":
        return
    for i in range(len(arr)):
        result[len(result)-length] = arr[i]
        newline = ''.join(result)
        nsign=0
        for a in range(0,len(result)):
            if str(result[a]).isalnum() == False:
                nsign = nsign + 1   
                
        if nsign <=3:
            if checkhash(salt,nhash,newline) is True:
                print("Find " + nhash + " is " + newline)
                SetFind(newline)
                return
                    
            stringup = newline.upper()
            if checkhash(salt,nhash,stringup) is True:
                print("Find " + nhash + " is " + newline)
                SetFind(newline)
                return
                    
            if newline[0].isalpha():
                stringcap = newline.capitalize()
                if checkhash(salt,nhash,stringup) is True:
                    print("Find " + nhash + " is " + newline)
                    SetFind(newline)
                    return
        ReCalculation(arr, length-1, i+1, result,nhash,salt)        # It is a recursive function
    return
    

if __name__=="__main__":
    saltf = open("salt.txt",'r')
    cracked = open("cracked.txt",'w')
    salt = saltf.read().strip()
    charlist = list(string.ascii_lowercase) + ['0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','-','+','=','<','>','?']
    
    hashf = open("hashes.txt")
    for line in hashf.readlines():
        SetFind("")
        print("Finding ", line)
        line = line.strip('\n')
        result = ""
        for i in range(31):
            newline = ['a']*(i+1)
            ReCalculation(charlist,i+1,0,newline,line,salt)
            result = GetFind()
            if result != "":
                break
        cracked.write(line+": "+ str(result))    
    print("Program Finished")
        
