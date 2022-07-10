import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

import math

N = 10000 # 10.000 tıklama
d = 10  # toplam 10 ilan var

toplam = 0 # toplam odul
secilenler = []

birler = [0]*d
sıfırlar =[0]*d

for n in range(1,N):
    ad = 0 #seçilen ilan
    max_th = 0
    for i in range(0,d):
        ranbeta = random.betavariate (birler[i] +1, sıfırlar[i] +1 )
        
        if ranbeta > max_th:
            max_th = ranbeta
            ad = i          
    secilenler.append(ad)
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    if odul == 1:
        birler[ad] = birler[ad]+1
    else:
        sıfırlar[ad] = sıfırlar[ad]+1
    toplam = toplam + odul
print('Toplam Odul:')   
print(toplam)

plt.hist(secilenler)
plt.show()
