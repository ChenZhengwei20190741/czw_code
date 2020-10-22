#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import sys
import pprint

def find_key(n):
    if n.find('.a')!=-1:
        return 1
    else:
        return 0
def find_value(n):
    if n.find('\n')!=-1:
        return 1
    else:
        return 0
dict1= {}
dict2= {}
def get_value(string, dict_string):
    list1 = string.split(" ")
    tmplist_key = filter(find_key, list1)
    newlist_key = list(tmplist_key)
    tmplist_value = filter(find_value, list1)
    newlist_value = list(tmplist_value)
    listvalue = list(map(int,newlist_value))
    # print(listvalue)
    
    dict_string[newlist_key[0]] = listvalue[0]
    # print (dict_string)
    # print (newlist_key[0], listvalue[0])
    # print (list1.index('\n'))
    # list1.index(' ')
    # print(string.split(" "))


####################
# main
####################

# file_name = '/bluf_41.txt'
# open(file_name, mode = 'r', buffering = -1, encoding_ = None, errors = None, newline = None, closefd = True, opener = None)
# os.mknod("hh.txt")
# fp = open("bluf_41.txt", "r")

file1 = sys.argv[1]
file2 = sys.argv[2]
fp1 = open(file1, "r")
fp2 = open(file2,"r")

while 1:
 fileline = fp1.readline()
 if not fileline:
     break
 if fileline.find('.a') != -1:
    get_value(fileline, dict1)
    # print (fileline)


while 1:
 fileline = fp2.readline()
 if not fileline:
     break
 if fileline.find('.a') != -1:
    get_value(fileline, dict2)
    # print (fileline)
 if fileline.find('idf.py -p (PORT) app-flash') != -1:
    break

dict3 = {}

for key in dict1:
    if dict2.get(key):
        dict3[key] = dict1[key] - dict2[key]
    else:
        dict3[key] = dict1[key]

for key in dict2:
    if not dict1.get(key):
        dict3[key] = -dict2[key]

list_cmp = sorted(dict3.items(),key=lambda x:x[1],reverse=True)
pprint.pprint(list_cmp)
# print(list_cmp)
