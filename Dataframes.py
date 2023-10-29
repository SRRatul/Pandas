import pandas as pd

'''Creating a data frame a dictionary'''
data = {'Subject':['Math','History','Science', 'English'],
        'marks':(100, 85, 95, 81),
        'CGPA':(5.0, 5.0, 5.0, 5.0)}
df = pd.DataFrame(data)
print(df)

'''TO create dataframe from series'''

Subject = pd.Series(['Math','History','Bangla','ICT'])
Marks = pd.Series([80,60,50,79])
Cgpa = pd.Series([5.0, 3.5, 3.0, 4.0])
print(pd.DataFrame([Subject,Marks,Cgpa], index=['Subject','Marks','Cgpa']))

'''However to want a vertical dataframe so we use .T
the 'T' stands for transpose. '''

print(pd.DataFrame([Subject,Marks,Cgpa], index=['Subject','Marks','Cgpa']).T)

'''TO read data from csv file. '''
datas = pd.read_csv("example.csv")
type(datas)
print(datas)

'''To print head of the data'''
data.head()
'''To know some information of the data'''
data.info()

