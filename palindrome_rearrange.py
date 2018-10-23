'''
Author: Anitha Kiron Vedantam
Description: This is a simple program to check whether the strings given in the
list can be re-arranged to form a palindrome or not.

'''

# Importing counter from collections
from collections import Counter

def palindromeRearranging(tests):
    oddCount = 0
    for k,v in Counter(tests).items():
        if v%2!=0:
            oddCount+=1
    if oddCount>1:
        return False
    return True

if __name__ == '__main__':
        tests = ["aabb", "acab", "dkfhakc", "odkirteikrtod", "ccddd", "ccdddd", "cd", "eeeeeee", "tacocat", "-a--a"]
        solutions = [True, False, False, True, True, True, False]
        for t, s in zip(tests, solutions):
                if palindromeRearranging(t) != s:
                        print('Error in test %s' % t)
                        break
        else:
                print('All tests passed.')
