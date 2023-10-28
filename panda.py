import pandas as pd
'''Pandas has two data structures as follows:
1) A series is 1D labeled array that can hold data of any 
type(int, str, bool, float, python objects and so on).
it's axis labels are collectively called an index
2) A DataFrame is 2D labeled data structure with columns. It 
supports multiple datatypes'''

'''Pandas Series:
Pandas Series is a 1D labeled array capable of holding
any data type. However, a series is a sequence of 
homogeneous data types. similar to an array, list or
coloumn in a table

It will assign a labeled index to each item in the series.
By default, each item will receive an indes label from 0 to N,
where N is the length of the Series minus one'''

#create a numeric series
numbers = range(1, 100, 5)
pd.Series(numbers)
#print(pd.Series(numbers))
# create a object series
objects = "hello", "how", "are", "you","?"
print(pd.Series(objects))
 #create a Series with an arbitary list
s = pd.Series([.014, 'Dhaka', 40, -20, 'Bangladesh'])
print(s)

#To set index values for a series 
marks = [100, 84, 94, 100]
subject = ["Maths", "Science", "English", "Social Science"]
print(pd.Series(marks, index = subject))

#To Create a series from a dictionary
data = {"Maths":100, "Science":85, "English":92, "Social Science":85}
print(pd.Series(data))
