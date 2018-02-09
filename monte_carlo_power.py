# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:43:33 2018

@author: rbarnes
"""

from scipy.stats import *
import numpy as np
import matplotlib.pyplot as plt

def simulate(n1=10,n2=100,diff=0,sd1=0.01,sd2=0.01):
    x1 = halfcauchy.rvs(loc=0,scale=sd1,size=n1)
    x2 = halfcauchy.rvs(loc=diff,scale=sd2,size=n2)
    return ttest_ind(x1,x2)

def run(N=1000,n1=10,n2=10,diff=0,sd1=1,sd2=1):
    output = []
    for i in range(N):
        output.append(simulate(n1,n2,diff,sd1,sd2).pvalue)
    return output

def calculate_power(pvalues):
    success = [1 if value<=0.05 else 0 for value in pvalues]
    return(np.mean(success),np.std(success),success,pvalues)

def display_pvalues(N=1000,n1=10,n2=10,diff=0,sd1=1,sd2=1):
    power,std,success,pval = calculate_power(run(N=N,
                                                 n1=n1,
                                                 n2=n2,
                                                 diff=diff,
                                                 sd1=sd1,
                                                 sd2=sd2))
    plt.hist(pval,bins=100,range=(0,1))
    plt.xlabel('P-value')
    plt.ylabel('Number of Simulations')
    plt.title('Probability of Finding Statistically\n'\
              'Significant Result: {0}%'.format(round(power*100,2)))
    plt.show()

if __name__=='__main__':
    display_pvalues(diff=0.5,n1=100,n2=100)