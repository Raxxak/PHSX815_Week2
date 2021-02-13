#analyzes the dieroll results and plots em

import numpy as np
import matplotlib.pyplot as plt

#choosing a result to plot the probability of 
result_num=5

#opens the data
result =open("diceroll_result.txt","r")

line = result.readlines()




i=0
x=[]
for i in range(0,len(line)):
    x.append(int(line[i]))
    

    
result.close()


#plots the histogram
plt.hist(x,bins= 25, density=True)    
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Diceroll')
plt.grid(True)
plt.show()






        
