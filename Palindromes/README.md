# Palindromes

1. Definition
	A palindrome is a string that reads the same from both ways.
	Ex: madam, bob, aa, level, abba

2. Iterative Method
	We iterate from the beginning of the string till the middle, and check if 
	the character that we are pointing to is the same on the other side of the string.

3. Recursive Method
	In the recursive method, we check both ends of the string, and then return 
	the same string but with both ends.
	The loop will end if the length of the string is equal to 0 or 1

4. Reverse the string
	In python, if st is a string, then st[::-1] if the reversed string
	Ex: st = abc
	    st[::-1] = cba
	Now, to check if st is a palindrome, we just check if the string and the 
	reversed string are equal.

Check out the video on https://www.youtube.com/channel/UCzw1_BkDtDeaaq9f8PJrJmA.
