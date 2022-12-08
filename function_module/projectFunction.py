#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Data ##

import numpy as np
import matplotlib.pyplot as plt

"""
Function Name: readFile
input: fileName - path to file
output: data_list - a list of all the data except the header
"""
def readFile(fileName):
    
    '''reads the data file from the named state'''
    
    data = np.loadtxt(fileName,delimiter=',',dtype=str)
    data_list = []
    for i in range(1, len(data)):
        item = data[i]
        data_list.append(item)
    return data_list


"""
Function Name: simplifyData
input: data - country data with no header
output: reduced_data - simplified with only date, deaths
"""
def simplifyData(data):

    reduced_data = []
    for item in data:
        reduced_data.append([item[0],item[2]])
    return reduced_data


"""
Function Name: sortData
input: data - reduced data with Dates, deaths, deathsIncrease
output: sorted_data - data sorted from 2020 to 2021
"""
def sortData(data):
    
    sorted_data = []
    for i in range(len(data)-1, -1, -1):
        sorted_data.append(data[i])
    return sorted_data


# In[ ]:


##Graphs##

import matplotlib.pyplot as plt

"""
Function Name: createMonthlyAverage
input: data - sorted data with just data, deaths
output: monthly_data - data reduced to deaths per month
"""
def createMonthlyAverage(data):
    
    months = ["March","April","May","June","July","August","September","October","November","December","January","Febuary"]
    monthly_data = []
    current = 0
    current_death = data[0][1]
    oldMonth = data[0][0][6:8]
    
    for i in range(len(data)):
        item = data[i]
        currentMonth = item[0][6:8]
        
        if oldMonth == currentMonth:
            current_death = item[1]
        else:
            monthly_data.append([months[current],current_death])
            current += 1
            current_death = item[1]
            oldMonth = currentMonth
            
    return monthly_data
            
    
"""
Function Name: graphState
input: fileName - data path to file
       state - the name of state to show on graph
output: montlyAverages is returned which is deaths for each month times 1000
        the function also plots the graph of each state
"""
def graphState(fileName, state, pop):
    months = ["Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec","Jan","Feb"]
    data = readFile(fileName)
    data = simplifyData(data)
    data = sortData(data)
    data = createMonthlyAverage(data)
    monthlyAverages = []
    
    for i in data:
        num = i[1]
        if num == '':
            num = '0'
        monthlyAverages.append(int(num)/pop)

    plt.plot(monthlyAverages)
    plt.xlabel('Month')
    plt.ylabel('Deaths Per 100,000 People')
    plt.title(state + " Covid Deaths Per 100,000 People")
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11], months)
    plt.yticks([0,25,50,75,100,125,150,175,200])
    plt.show()
    
    return monthlyAverages

"""
Function: calculateAverageOfStates
input: stateList - list of all red/blue states
output: avgList - average of all deaths for each month
"""
def calculateAverageOfStates(stateList):
    avgList = []
    total = len(stateList)
    
    for i in range(len(stateList[0])):
        
        current = 0
        for state in stateList:
            current += state[i]
        avgList.append(current / total)
        
    return avgList
        
        
"""
Function: graphRBStates
input: stateAvgList - list of all the states average deaths
       stateColor - title for plot red or blue states
output: nothing returned, plots graph
"""     

def graphRBStates(stateAvgList, stateColor):

    months = ["Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec","Jan","Feb"]
    plt.scatter(months, stateAvgList)
    
    plt.xlabel('Month')
    plt.ylabel('Deaths x 1000')
    plt.title(stateColor + " Covid Deaths")
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11], months)
    plt.yticks([0,25,50,75,100,125,150,175,200])
    plt.show()

