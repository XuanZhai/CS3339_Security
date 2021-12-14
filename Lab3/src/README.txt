Xuan(James) Zhai - CS3339 LAB3
47607746


Crack Hash Passwords
================================================================
There are two methods that in the project, brute-force and dictionary attack. 
You may need to use both two methods to find all the words.

1. BruteForce
1.1 How to run it
You don't need to use any input dataset for this method.
When you run BruteForce.py, it will analyze all the hashes in hashes.txt.
It will simplely find all the combinations of characters, from length 1 to 31.
For each combination, it will hash it with salt and compare it with the original hash.
It will return the result into cracked.txt

1.2 Advantage and Disadvantage
It does not need any dataset.
It will eventually find all the result.
However, its time consumption could be exponential, especially when length is greater than 4.

1.3 How it's used in this Lab Assignment
Since one type of passwords is random string (length < 5) in this assignment, 
I use this method to find all the passwords with random string.


2. Dictionary attack
2.1 How to run it
There are some datasets that are already existed in the "file" folder, but you will need more.
To create more datasets, you will need to run DictMethod_File.py.
It will create datasets with combinational words, words with uppercase, and words with special characters replaced.
Creating datasets may take a few minutes.
After all the datasets are created, you can run DictMethod.py to crack the password.

2.2 Advantage and Disadvantage
It will take shorter time to run compared to BruteForce
It can find words with larger length
However, it does not gurantee to find all the password, everything will depend on the dataset you have.

2.3 How it's used in this Lab Assignment
For words that have length greater than 4, it's hard to use BruteForce to find it.
Therefore, I use Dictionary Attack to try to figure out all the words. 