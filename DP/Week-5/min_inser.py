# The problem is simple , to make any string as palindromic string , we can add the reverse of the sting to it ,for 
# example , to make abc as palindromic subtring , we can add cba to it and this would make it abccba which is a palindromic
# substring . This is the maximum length insertion to make any string palindromic . But , in order to find the minimum insertions
# required to make a string palindromic , we can ignore counting subsequence which is already a palindromic . for example 
# to make abaac , aaa is a subsequence which is already palindromic , we can make use of it to find the minimum insertions
# minimum insertions = length of given string - length of longest subsequence


# Problem statement - minimum insertions and minimum deletions required to convert string 1 to string 2

# in general , if we want to convert string 1 to string 2 , we can delete all the characters from string1 (n deletions)
# operations) and add all the characters of string2 (m addition operations) , making total of n + m operations where
# n is the length of string1 and m is the length of string2 , in order to find the minimum operations , we can ignore
# deleting all the characters of string1 which are present in string 2 , in other words finding longest common subsequence
# and then deleting the remaining characters and adding the characters of strning 2 
# final conclusion =( n - length of common subsequence ) + (m - length of common subsequence)

# problem statement - shortest common supersequence 
# shortest common supersequence is a string from which both string1 and string 2 can generated .
# in general we can make this by adding both the strings , string1 + string2  . in order to make it minimum 
# we can avoid adding those characters which are common in both the strings . in other words find the longest common 
# subsequence and add them only once 
#final solutions : (n+m - k ) where k is the length of the longest common superseuqnce
