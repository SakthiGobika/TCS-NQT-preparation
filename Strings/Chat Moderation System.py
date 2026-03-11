'''Q - Chat Moderation System

Problem Statement:
A chat platform wants to detect spam. If a message contains three consecutive identical characters, it is
considered spam.
Given a message string, determine whether it is spam or safe.

Input Format:
. A single string S

Output Format:
. Print Spam or Safe'''
s=input()
for i in range(len(s)-2):
    if s[i]==s[i+1]==s[i+2]:
        print("Spam")
        break
else:
        print("Safe")