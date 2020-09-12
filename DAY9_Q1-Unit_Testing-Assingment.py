#Requirement already satisfied: pylint in /home/ravikiran/anaconda3/lib/python3.8/site-packages (2.5.3)
#Requirement already satisfied: mccabe<0.7,>=0.6 in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from pylint) (0.6.1)
#Requirement already satisfied: toml>=0.7.1 in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from pylint) (0.10.1)
#Requirement already satisfied: astroid<=2.5,>=2.4.0 in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from pylint) (2.4.2)
#Requirement already satisfied: isort<5,>=4.2.5 in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from pylint) (4.3.21)
#Requirement already satisfied: wrapt~=1.11 in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from astroid<=2.5,>=2.4.0->pylint) (1.11.2)
#Requirement already satisfied: lazy-object-proxy==1.4.* in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from astroid<=2.5,>=2.4.0->pylint) (1.4.3)
#Requirement already satisfied: six~=1.12 in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from astroid<=2.5,>=2.4.0->pylint) (1.15.0)

#Collecting unittest2
#  Downloading unittest2-1.1.0-py2.py3-none-any.whl (96 kB)
#     |████████████████████████████████| 96 kB 171 kB/s 
#Collecting argparse
#  Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)
#Requirement already satisfied: six>=1.4 in /home/ravikiran/anaconda3/lib/python3.8/site-packages (from unittest2) (1.15.0)
#Collecting traceback2
#  Downloading traceback2-1.4.0-py2.py3-none-any.whl (16 kB)
#Collecting linecache2
#  Downloading linecache2-1.0.0-py2.py3-none-any.whl (12 kB)
#Installing collected packages: argparse, linecache2, traceback2, unittest2
#Successfully installed argparse-1.4.0 linecache2-1.0.0 traceback2-1.4.0 unittest2-1.1.0

#ERROR: Could not find a version that satisfies the requirement unittest (from versions: none)
#ERROR: No matching distribution found for unittest


#PyLint

'''
This is a module to check weather the given number is even or odd.''
'''
def prime(num):
    '''
    This is the main function which check out the given number is even or odd.
    '''
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            return print("It is a Prime Number")
    return print("It is not a Prime Number")
n = int(input("enter the number :"))
prime(n)



#Unittest


def capText(string_To_Cap):
    return string_To_Cap.title()



#writefile test.py

'''
this is the test file in which we are going to check out the py file with the help of unittest
'''
import unittest
import capitalizeText

class testPrimeNumber(unittest.TestCase):
    def testOne(self):
        result = capitalizeText.capText("anmol noor")
        self.assertEqual(result,"Anmol Noor")
    def testSecond(self):
        result = capitalizeText.capText("this is a text string to test the unittest on a file")
        self.assertEqual(result,"This Is A Text String To Test The Unittest On A File")

if __name__ == "__main__":
    unittest.main()


