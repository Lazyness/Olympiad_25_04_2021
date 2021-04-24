from constants import message

def outputf(message):
    # -*- coding: utf-8 -*-
    my_file = open('D:\\Olimp_24_05_2021\\Olympiad_25_04_2021\\test.txt', 'w')
       
    my_file.write(message)
    
    my_file.close()

outputf(message)