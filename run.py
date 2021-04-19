#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:37:24 2021

@author: syu
"""
import pandas as pd 
import os
from preprocess import Preprocess 

checkings = pd.read_csv("bank-records/checking.csv")
savings = pd.read_csv("bank-records/savings.csv")
credit = pd.read_csv("bank-records/credit_card.csv", header=None)

preprocess = Preprocess() 
report = preprocess.create_report(checkings, savings, credit)


# Create a histogram of money in my possession vs money owed
money_in = input("Please enter the total amount of money in your checkings and savings account: ")
money_owed = input("Please enter the total amount of money owed in your credit account: ") 
all_money = [float(money_in), float(money_owed), float(money_in) - float(money_owed)]
labels = ["Money in bank", "Money owed to credit card", "Money adjusted for credit"]

# Write info to file        
with open("balance.dat", "w") as file_object: 
    for i in range(len(labels)): 
        file_object.write(labels[i] + "," + str(all_money[i]) + "\n")
    
# Generate a simple barplot within the terminal using termgraph
os.system("termgraph balance.dat")