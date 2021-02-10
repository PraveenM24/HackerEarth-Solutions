"""
PROBLEM STATEMENT
You are given a string S. Find the number of different substrings in S.
Input
One line containing a string S consisting of lowercase Latin letters.
Output
Output one integer - answer to the question.
Constraints
1 <= length of S <= 1200
Sample Input
abc
Sample Output
6
Explanation
substrings of abc =['ab','bc','ac','a','b','c']
"""
if __name__ == '__main__': 
    string = str(input())
    result = set() 
    for i in range(len(string)+1): 
        for j in range( i + 1, len(string)+1): 
            result.add(string[i:j])
    print(len(result))
