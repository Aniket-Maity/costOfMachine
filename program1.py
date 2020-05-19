# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:06:53 2020

@author: Aniket Maity
"""


'''
def main():
    pass

if __name__== '__main__':
    try:
        main()
    except:
        pass
'''


machineAndParts=list(map(int,input().split()))

machines  = list(map(int,input().split()))

allMachine = [0]*machineAndParts[0]


for i in range(machineAndParts[1]):
    
    a = list(map(int,input().split()))
    index = a[0]
    for i in range(index):
        curIndex = a[i+1]
        allMachine[curIndex-1]+=a[-1]
print(allMachine.index(max(allMachine))+1)


