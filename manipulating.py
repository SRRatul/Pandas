import pandas as pd
import numpy as np
data={'Math':100,'English':88,'ICT':100, 'Bangla':89}
Subject={'Math','English','ICT','Religion','Bangla'}
print(pd.Series(data, index=Subject))
ms = pd.Series(data, index=Subject)
'''TO check for null values using .isnull'''
print(pd.isnull(ms))

'''To check for null values using .notnull'''
print(pd.notnull(ms))

'''To check the subjects in which marks score is more than 90'''
print(ms[ms >= 90])

'''To assign marks in Null element'''
ms["Religion"]=88
print(ms)

'''To check whether Maths marks are 100 or not'''
print(ms.Math == 100)
print(ms.Math == 90)

'''Sorting a numeric series'''
Series = np.arange(15)
values = pd.Series(Series)
print(values)

#sorting in ascending order
print(values.sort_values(ascending= True))
#sorting in descending order
print(values.sort_values(ascending = False))
 #Rank the series
print(ms.rank(ascending=True, pct=False))
