import pandas as pd

#SMA AND STOCKASTIC RSI:
Numbers=pd.Series([1, 25, 3, 11, 24, 6,4,2,5,23,5,27,12,19,15,18,33,51,21,40])
lowestlow = pd.Series.rolling(Numbers,window=14,center=False).min()
print(lowestlow)
highesthigh = pd.Series.rolling(Numbers, window=14, center=False).max()
print(highesthigh)
#Creating the Series
result = pd.Series.rolling(Numbers,window=2).mean()
StoRSI=100*((Numbers-lowestlow)/(highesthigh-lowestlow))
print(StoRSI)
K=pd.Series.rolling(StoRSI,window=3).mean()
print(K)
D=pd.Series.rolling(K,window=3).mean()
print(D)

'''
# Create the Index
#index = ['Zam Zam', 'Sprite', 'Coke', 'Fanta', 'Dew', 'ThumbsUp']
# set the index
sr.index = index #what is different index and index_
# Print the series
# Find sum over a window size of 2
#result = sr.rolling(window=2).mean()
'''
'''
#result
Zam Zam      NaN
Sprite      17.5
Coke        14.0
Fanta        7.0
Dew         17.5
ThumbsUp    15.0
dtype: float64
'''
#there was no element previous to it so the sum could not be performed.

