import itertools
import string
from itertools import permutations
import re

#Creating random number using Brute Force Generator

def left_right():
    file = open("file/CommonWords_small.txt", 'r')
    w = file.readlines()
    file.close()
    write = open("file/CommonWordsll.txt", 'w')
    word_list = []
    for word in w:
        word = word.strip()
        word_list.append(word)
    for subset in itertools.permutations(word_list, 2):
        write.write(''.join(subset))
        write.write('\n')
    write.close()

def Left_right():
    file = open("file/CommonWordsll.txt", 'r')
    w = file.readlines()
    file.close()
    write = open("file/CommonWordsul.txt", 'w')
    for word in w:
        word = word.strip()
        write.write(word.capitalize() + '\n')
    write.close()

def Left_Right():
    file = open("file/CommonWords_small.txt", 'r')
    w = file.readlines()
    file.close()
    write = open("file/CommonWordsuu.txt", 'w')
    word_list = []
    for word in w:
        word = word.strip()
        word = word.capitalize()
        word_list.append(word)
    for subset in itertools.permutations(word_list, 2):
        write.write(''.join(subset))
        write.write('\n')
    write.close()
    
def left_Right():
    file = open("file/CommonWordsuu.txt", 'r')
    w = file.readlines()
    file.close()
    write = open("file/CommonWordslu.txt", 'w')
    for word in w:
        word = word.strip()
        word = word[0].lower() + word[1:]
        write.write(word + '\n')
    write.close()

def cap_dict():
    file = open('file/CommonWords.txt', 'r')
    w = file.readlines()
    file.close()
    write = open('file/CommonWords_cap.txt', 'w')
    for word in w:
        word = word.strip()
        write.write(word.capitalize()+'\n')

def upper_dict():
    file = open('file/CommonWords.txt', 'r')
    w = file.readlines()
    file.close()
    write = open('file/CommonWords_upper.txt', 'w')
    for word in w:
        word = word.strip()
        write.write(word.upper()+'\n')

def add_trailing():
    add = list('!@#$%^&*-+=<>?' + string.digits)
    result = []
    write = open("file/CommonWords_trailing.txt", 'w')
    with open("file/CommonWords.txt") as d:
        for line in d:
            for a in add:
                write.write(''.join(line.strip() + a) + '\n')
    for i in range(1,4):
        for r in result:
            for a in add:        
                write.write(''.join(r+a)+ '\n')
    write.close()

def replace_letter():
    result = []
    write = open("file/CommonWords_replace.txt", 'w')
    with open("file/CommonWords.txt") as d:
        for line in d:
            line = line.strip()
            t1 = re.subn('a','@',line)
            t2 = re.subn('o','0',line)
            
            if t1[1] == 0 and t2[1] == 0:
                pass
            elif t1[1] > 0 and t2[1] > 0:
                write.write(''.join(t1[0])+'\n')
                write.write(''.join(t2[0])+'\n')
                t3 = re.sub('o','0',t1[0])
                write.write(''.join(t3)+'\n')
            elif t1[1] > 0:
                write.write(''.join(t1[0])+'\n')
            elif t2[1] > 0:
                write.write(''.join(t2[0])+'\n')
            else:
                pass
    write.close()
 

if __name__ == "__main__":
    left_right()
    Left_right()
    Left_Right()
    left_Right()
    cap_dict()
    upper_dict()
    add_trailing()
    replace_letter()