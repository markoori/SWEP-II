import pandas as pd
import numpy as np

csv-file = pd.read('DatascienceTest.csv')

count,airtelCount,mtnCount,gloCount,etisalatCount,othersCount = 0

mtnNumber = ['0803','0806','0814','0810','08013','0814','0816','0703','0706','0903','0906']
airtelNumber = ['0802','0808','0812','0708','0701','0902','0901','0907']
etisalatNumber = ['0809','0817','0818','0909','0908']
gloNumber = ['0805','0807','0811','0815','0705','0905']

for i in csv-file:
    if i['PHONE NUMBER'].split(:4) ==  mtnNumber[count]:
        mtnCount += 1;
    elif i['PHONE NUMBER'].split(:4) ==  airtelNumber[count]:
        airtelCount += 1;
    elif i['PHONE NUMBER'].split(:4) ==  etisalatNumber[count]:
        etisalatCount += 1;
    elif i['PHONE NUMBER'].split(:4) ==  gloNumber[count]:
        gloCount += 1;
    else:
        othersCount += 1;
        
# sorting algorithm for the scores
scoreArray = []
for score in csv-file:
   scoreArray =  score["SCORE"] 

updatedScores = []
for i in range(len(scoreArray)):
    updatedScores.append(max(scoreArray)) 
    scoreArray.remove(max(scoreArray))

# displaying the updated score in the DataFrame

    