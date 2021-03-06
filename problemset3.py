#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def loadAndCleanData(filename):
	df = pd.read_csv(filename) 
	df = df.fillna(0)
	return df
	


a = loadAndCleanData('creditData.csv')


#def computePDF(targetFeature, dataset):


	#x = dataset.plot.kde()
	#plt.show()

#computePDF(a['age'],a)
#computePDF(a['SeriousDlqin2yrs'],a)
#computePDF(a['RevolvingUtilizationOfUnsecuredLines'],a)
#computePDF(a['NumberOfTime30-59DaysPastDueNotWorse'],a)
#computePDF(a['DebtRatio'],a)
#computePDF(a['MonthlyIncome'],a)
#computePDF(a['NumberOfOpenCreditLinesAndLoans'],a)
#computePDF(a['NumberOfTimes90DaysLate'],a)
#computePDF(a['NumberRealEstateLoansOrLines'],a)
#computePDF(a['NumberOfTime60-89DaysPastDueNotWorse'],a)
#computePDF(a['NumberOfDependents'],a)

#5

def viewDistribution(colum, dataframe):
	dataframe.hist(column = colum)
	plt.show()
#viewDistribution('age', a)

#viewDistribution('SeriousDlqin2yrs',a)
#viewDistribution('RevolvingUtilizationOfUnsecuredLines',a)
#viewDistribution(a['NumberOfTime30-59DaysPastDueNotWorse'],a)
#viewDistribution('DebtRatio',a)
#viewDistribution('MonthlyIncome',a)
#viewDistribution('NumberOfOpenCreditLinesAndLoans',a)
#viewDistribution('NumberOfTimes90DaysLate',a)
#viewDistribution('NumberRealEstateLoansOrLines',a)
#viewDistribution('NumberOfTime60-89DaysPastDueNotWorse',a)
#viewDistribution('NumberOfDependents',a)


def viewLogDistribution(colum, dataframe):
	dataframe.hist(column = math.log(colum))
	plt.show()

#viewDistribution('age', a)

#viewDistribution('SeriousDlqin2yrs',a)
#viewDistribution('RevolvingUtilizationOfUnsecuredLines',a)
#viewDistribution(a['NumberOfTime30-59DaysPastDueNotWorse'],a)
#viewDistribution('DebtRatio',a)
#viewDistribution('MonthlyIncome',a)
#viewDistribution('NumberOfOpenCreditLinesAndLoans',a)
#viewDistribution('NumberOfTimes90DaysLate',a)
#viewDistribution('NumberRealEstateLoansOrLines',a)
#viewDistribution('NumberOfTime60-89DaysPastDueNotWorse',a)
#viewDistribution('NumberOfDependents',a)

#probability of a given b = probability of a and b, divided by probability of b
def computeDefaultRisk(colum,bin,targetFeature,dataframe):
	#column is name of column being looked at
	#bin is the start and end of the range of values you are looking at
	#target feature is the delinquincy

	seriesObj = dataframe.apply(lambda x: True if (x[colum] > 50) & (x[targetFeature] == 1) else False , axis=1)
 
	# Count number of True in series
	ab = float(len(seriesObj[seriesObj == True].index))

	seriesObj2 = dataframe.apply(lambda x: True if x[targetFeature] == 1 else False , axis=1)
 
	# Count number of True in series
	b = float(len(seriesObj2[seriesObj2 == True].index))
	

	print (ab)/b


array = [50,120]
#computeDefaultRisk('age',array,'SeriousDlqin2yrs',a)




c = loadAndCleanData('newLoans.csv')





























