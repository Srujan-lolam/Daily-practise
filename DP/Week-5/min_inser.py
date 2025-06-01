# The problem is simple , to make any string as palindromic string , we can add the reverse of the sting to it ,for 
# example , to make abc as palindromic subtring , we can add cba to it and this would make it abccba which is a palindromic
# substring . This is the maximum length insertion to make any string palindromic . But , in order to find the minimum insertions
# required to make a string palindromic , we can ignore counting subsequence which is already a palindromic . for example 
# to make abaac , aaa is a subsequence which is already palindromic , we can make use of it to find the minimum insertions
# minimum insertions = length of given string - length of longest subsequence
