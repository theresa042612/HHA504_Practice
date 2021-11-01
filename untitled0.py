#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:50:01 2021

@author: theresaoriental
"""

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import norm

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')


timeinhospital = diabetes['time_in_hospital']
labprocedures = diabetes['num_lab_procedures'] 
gender = diabetes['gender']

from scipy.stats import shapiro
import scipy.stats as stats
from matplotlib import pyplot
from scipy.stats import ttest_ind

diabetes_small = diabetes.sample(100)
 
#generate list of vars name 
list(diabetes_small)

timeinhospital = diabetes['time_in_hospital']
labprocedures = diabetes['num_lab_procedures'] 

diabetes['totalCountProcedures'] = diabetes['num_procedures'] + diabetes['num_lab_procedures']
diabetes['totalCountProcedures'].describe()
totalCountProcedures = diabetes['totalCountProcedures'].array


#T-Test
#difference 1
#Is there a difference between sex (M:F) and the number of days in hospital?

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

Female['totalCountProcedures'] = Female['num_procedures'] + Female['num_lab_procedures']
Male['totalCountProcedures'] = Male['num_procedures'] + Male['num_lab_procedures']
ttest_ind(Female['totalCountProcedures'], Male['totalCountProcedures'])
####statistic=-0.6747218803792331, pvalue=0.4998540133474586


##There is no difference in average number of procedures between males and females 
##because the p-value is greater than 0.05, which means that we fail to reject the null hypothesis 

#### difference between gender (M:F) and the number of days in hospital

ttest_ind (Female['time_in_hospital'], Male['time_in_hospital'])
###statistic=9.542637042242887, pvalue=1.4217299655114968e-21

#There is a significant difference in time in hospital between males and females 
#because the p-value is less than 0.05, which is allowing us to reject the null hypothesis 
#Difference 2
#Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?

Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])
####statistic=-5.0610017032095325, pvalue=4.178330085585203e-07

##There is a significant difference in time in hospital between males and females 
#because the p-value is less than 0.05, which is allowing us to reject the null hypothesis 


#Difference 3
#Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?
Asian = diabetes[diabetes['race']=='Asian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Asian['totalCountProcedures'], AfricanAmerican['totalCountProcedures'])
###statistic=-3.7897663070631253, pvalue=0.00015123463923369748

##There is a significant difference in time in hospital between males and females 
because the p-value is less than 0.05, which is allowing us to reject the null hypothesis 