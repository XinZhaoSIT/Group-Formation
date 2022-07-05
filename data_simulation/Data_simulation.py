#!/usr/bin/env python
# coding: utf-8

# In[101]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
import scipy.stats as ss


# In[102]:


def simu_gender(size, pct=0.5): # 50% of male students by default
    sex_dic = {0:'female',1:'male'}
    sex_p = [1-pct,pct]
    nums = np.random.choice((0,1),size=size,p=sex_p)
    gender = []
    for i in nums:
        gender.append(sex_dic.get(i))
    return gender


# In[103]:


def simu_temperament(size):
    tmp_dic = {0:'ISFJ',1:'ESFJ',2:'ISTJ',3:'ISFP',4:'ESTJ',5:'ESFP',6:'ENFP',7:'ISTP',8:'INFP',\
               9:'ESTP',10:'INTP',11:'ENTP',12:'ENFJ',13:'INTJ',14:'ENTJ',15:'INFJ'}
    
    tmp_p = [0.138, 0.123, 0.116, 0.088, 0.087, 0.085, 0.081, 0.054, 0.044,\
             0.043, 0.033, 0.032, 0.025, 0.021, 0.018, 0.015]
    # personality type distribution in the general population
    # data source: "MBTI Manual" published by CPP
    
    tmp_p /= np.sum(tmp_p)
    # normalize the probability to 1
    
    x = np.arange(0,16)
    nums = np.random.choice(x,size=size,p=tmp_p)
    tmp = []
    for i in nums:
        tmp.append(tmp_dic.get(i))
    return tmp


# In[104]:


def simu_race(size):
    x = np.arange(1,6)
    race_dic = {1:'white',2:'Hispanic and Latino',3:'black',4:'asian',5:'others'}
    
    race_p =[0.603, 0.185, 0.134, 0.059, 0.043]
    # data from wiki: percent of population in U.S. https://en.wikipedia.org/wiki/Race_and_ethnicity_in_the_United_States
    race_p /= np.sum(race_p)
    # normalize the probability to 1
    
    nums = np.random.choice(x, size= size, p=race_p)

    race = []
    for i in nums:
        race.append(race_dic.get(i))
    return race    


# In[105]:


# international student or U.S. demoestic student
def simu_international(size, pct=0.06): 
    #default percentage is from https://www.migrationpolicy.org/article/international-students-united-states-2020
    
    int_dic = {0:'domestic',1:'international'}
    int_p = [1-pct,pct]
    nums = np.random.choice((0,1),size = size, p = int_p)
    
    s_int = []
    for i in nums:
        s_int.append(int_dic.get(i))
        
    return s_int


# In[106]:


# target skills; default by 20% of students qualified 
def simu_tgt_skill(size, pct=0.2):
    
    tgt_dic = {0:'no',1:'yes'}
    tgt_p = [1-pct,pct]
    nums = np.random.choice((0,1),size = size, p = tgt_p)
    
    tgt_skill = []
    for i in nums:
        tgt_skill.append(tgt_dic.get(i))
        
    return tgt_skill    


# In[107]:


# team work score: 1 to 5
def simu_team_work_score(size):
    x = np.arange(1,6,1)
    
    # assume most of students has a score of 3 or 4
    prob = [0.1, 0.15, 0.33, 0.32, 0.1]
    
    nums = np.random.choice(x,size=size, p = prob)
    
    return nums


# In[108]:


# reading score: 1 to 5
def simu_reading_score(size):
    x = np.arange(1,6,1)
    
    # assume most of students has a score of 3 or 4
    prob = [0.1, 0.15, 0.33, 0.32, 0.1]
    
    nums = np.random.choice(x,size=size, p = prob)
    
    return nums    


# In[132]:


def get_interpersonal(size):
    
    nums = np.around(np.random.normal(80,9,size=(size,11)).T,0).astype(int)

        
    columns = ['Teamwork','Empathy_skills','Self-control','Ability_to_compromise',\
               'Ability_to_teach','Respect_for_others','Openness_to_Criticism','Sensitivity_and_Tact',\
               'Gaining_trust','Comfort_with_Differences','Listening_Skills']
    
    tmw = nums[0]
    ems = nums[1]
    sc = nums[2]
    atc = nums[3]
    att = nums[4]
    rfo = nums[5]
    otc = nums[6]
    sat = nums[7]
    gt = nums[8]
    cwd = nums[9]
    ls = nums[10]
    
    return tmw, ems, sc, atc, att, rfo, otc, sat, gt, cwd, ls


# In[133]:


if __name__ == "__main__":
    
    np.random.seed(42)
    
    size = 1000000
    
    gender = simu_gender(size)
    #tmp = simu_temperament(size)
    race = simu_race(size)
    intn = simu_international(size)
    tgt = simu_tgt_skill(size)
    rds = simu_reading_score(size)
    tmw, ems, sc, atc, att, rfo, otc, sat, gt, cwd, ls = get_interpersonal(size)
    
    data_dic = {'gender':gender,'race':race,'international_stu':intn,'technical_skill':tgt,\
                'reading_score':rds, 'Teamwork':tmw,'Empathy_skills':ems,'Self-control':sc,'Ability_to_compromise':atc,\
                'Ability_to_teach':att,'Respect_for_others':rfo,'Openness_to_Criticism':otc,'Sensitivity_and_Tact':sat,\
                'Gaining_trust':gt,'Comfort_with_Differences':cwd,'Listening_Skills':ls}
    
    df = pd.DataFrame(data_dic)
    print(df.head())

    compression_opts = dict(method='zip', archive_name='student_simulation.csv')  
    
    df.to_csv('student.zip', index=False, compression=compression_opts)



