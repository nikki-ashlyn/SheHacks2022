# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:28:52 2022

@author: Indigo
"""

from csv import reader

def main():
    # parse the mentee and mentor data by putting into a list of lists
    mentors = open("/Users/Indigo/Documents/mentors.csv","r") 
    mentees = open("/Users/Indigo/Documents/mentees.csv","r")
    mentor_reader = reader(mentors)
    mentor_list = list(mentor_reader)
    mentor_list = mentor_list[1:]
    mentee_reader= reader(mentees)
    mentee_list = list(mentee_reader)
    mentee_list = mentee_list[1:]
    
    # close mentor and mentee files
    mentors.close()
    mentees.close()
        
    # create dictionary of mentors by subject
    '''CS = 6 DS = 7 phys = 8 bio = 9 chem = 10 math = 11 engi = 12 gen = 13'''
    subjects = {6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: []}
    for mentor in mentor_list: 
        for i in range(6, 14):
            if mentor[i] == '1':
                subjects[i].append(mentor[0])
                
    # create dictionary of mentor sets for each mentee       
    mentor_sets_dict = {}
    for mentee in mentee_list: 
        mentor_sets_dict[mentee[0]] = []
        for i in range(6, 14):
            if mentee[i] == '1':
                for name in subjects[i]:
                    mentor_sets_dict[mentee[0]].append(name)
                    
    # sort mentees so we can start with mentee with the smallest mentor set
    sorted_mentor_sets = sorted(mentor_sets_dict, key=len)
        
    # create mentee dictionary for faster lookup
    mentee_dict = {}
    for mentee in mentee_list:
        mentee_dict[mentee[0]] = mentee[1:]  
    
    # create mentor dictionary for faster lookup
    mentor_dict = {}
    for mentor in mentor_list:
        mentor_dict[mentor[0]] = mentor[1:]  
        
    # create an output file
    matches = open("/Users/Indigo/Documents/matches.txt","w")
    
    # find matches starting with mentee with smallest mentor set
    for mentee in sorted_mentor_sets: 
        mentor_set = mentor_sets_dict[mentee]
        mentee_values = mentee_dict[mentee]
        maxNum = 0
        maxMatch = ""
        for mentor in mentor_set:
            # check if mentor has already been taken
            if mentor in mentor_dict:
                mentor_values = mentor_dict[mentor]
                temp = 0
                # find best match based on most compatible answers
                for j in range(0, len(mentee_values)):
                    if mentor_values[j] == mentee_values[j]:
                        temp += 1
                    if temp > maxNum: 
                        maxNum = temp
                        maxMatch = mentor
            # if mentor has already been taken, try next mentor
            else: 
                continue
        # if no mentor has been found, find closest compatible mentor
        if maxMatch == "":
            for mentor, mentor_values in mentor_dict.items(): 
                temp = 0
                # find best match based on most compatible answers
                for j in range(0, len(mentee_values)):
                    if mentor_values[j] == mentee_values[j]:
                        temp += 1
                    if temp >= maxNum: # equal to in case there are zero similarities
                        maxNum = temp
                        maxMatch = mentor   
        # print pairing to terminal/file and remove mentor
        output = "Mentor: {m1}, Mentee: {m2}\n".format(m1 = maxMatch, m2 = mentee)
        print(output, end='')
        matches.write(output)
        del mentor_dict[maxMatch]
    
    # close file containing the new matches
    matches.close()
                       
    
    
if __name__ == "__main__":
    main()