import hashlib
import string


def fileChecking(hashCode, listName):           # Check hashcode with word
    sf = open("salt.txt", "r")
    salt = sf.read().strip()
    for word in listName:
        word = word.strip()
        if(len(word) != 0):
            salted_word = (salt + word).encode('utf-8')
            hash_value = hashlib.sha256(salted_word).hexdigest()
            if(hash_value == hashCode):
                print("Find ", hashCode, " is ", word)
                return word
    return "" 


if __name__ == "__main__":
    hashes = open('hashes.txt','r')
    lines = hashes.readlines()
    hashes.close()
    answer = open('cracked.txt', 'w')   # The order of files in the checklist could be important because it will minimize the waiting time
    check_file_list = ['file/commonPasswords', 'file/CommonWords', 'file/100k-passwords',  'file/CommonWords_replace', 'file/CommonWords_trailing', 'file/commonWords_cap', 'file/commonWords_upper', 'file/rockyou',  'file/CommonWordsll', 'file/CommonWordsuu', 'file/CommonWordslu','file/CommonWordsul']
    for hashcode in lines: 
        hashcode = hashcode.strip()
        print("Code is ", hashcode)
        if(len(hashcode) != 0):
            answer.write('{}: '.format(hashcode))
            for file in check_file_list:
                fileName = file + '.txt'
                print("File Name is",fileName)
                f = open(fileName, 'r', encoding='gb18030', errors='ignore')
                words = f.readlines()
                f.close()
                word = fileChecking(hashcode, words)
                if(len(word) != 0):
                    answer.write(word)
                    break
            answer.write('\n')
    answer.close()