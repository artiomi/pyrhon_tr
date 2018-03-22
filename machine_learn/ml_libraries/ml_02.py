#pandas
import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20 , 30]
arr = np.array(my_data)
d = {'a':10 , 'b': 20, 'c':30}
pd.Series(data = my_data, index = labels)
pd.Series(arr, labels)
pd.Series(d)

ser1= pd.Series([1,2,3,4],["USA","Japan","USSR","Germany"])

#dataframes
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C', 'D', 'E'],['W', 'X', 'Y', 'Z'])
df[['W','Z']]

df['new'] = df['W'] + df['Y']
df.drop('E')

df.drop('new', axis = 1, inplace =True)

df.loc['A']
df.iloc[0]

df.loc['B','Y']
df.loc[['A','B'],['W','Y']]
df.shape

booldf = df>0
df[df['W']<0][['Y','X']]

df.reset_index()

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
df.loc['G1'].loc[1]
df.index.names = ['Groups', 'Num']
df.xs(1, level = 'Num')

#Missing data

d = {'A':[1,2, np.nan],'B':[5, np.nan, np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
df.dropna(thresh=2)
df.fillna(value = 'Fill')
df['A'].fillna(value = df['A'].mean())

#Group By

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
byComp = df.groupby('Company')
byComp.describe().transpose()['FB']

#Operations

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df['col2'].unique()
df['col2'].value_counts()

def times2(x):
    return x*2

df['col1'].apply(times2)

df['col1'].apply(lambda x: x*3)
df.sort_values('col2')

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
df.pivot_table(values = 'D', index=['A','B'], columns ='C')

df = pd.read_csv('E:\AI\python_libs\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-for-Data-Analysis\Pandas\example')
df.to_csv('output', index =False)

