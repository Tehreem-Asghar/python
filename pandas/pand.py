import pandas as pd
import pandera as pa


# pandas core component 
# Series type
# DataFrame  type


# create series

# list
a = pd.Series([1, 2, 3])
print(a)


c = pd.Series([12, 23, 34], index=['a', 'b', 'c'])
print(c)

# tuple
b = pd.Series((1, 2, 3))
print(b)


# d = pd.Series({1, 2, 3})
# print(d) # Error set data type not allow


# dic we can use for creating series


# dict ma ham jo bhi key rakhta hai wo indexing ki replacement ho jati hai
e = pd.Series({'a': 1, 'b': 2, 'c': 3 , 'd': 4 , 'e': 5})
print("dic",e)

values : list[int] = [1, 2, 3]
index : list[str] = ['a', 'b', 'c']

f = pd.Series(values, index=index)
print("index" ,f)

# multiple indexing

values : list[int] = [1,2,3,4,5,6,7,8,9]
index  = ['a','a', 'a','b' ,'b', 'b','c', 'c', 'c']

f = pd.Series(values, index=index) 
print("multiple indexing" ,f)

# we can also pass extra parameter like name

values : list[int] = [1,2,3,4,5,6,7,8,9]
index  = ['a','a', 'a','b' ,'b', 'b','c', 'c', 'c']

f = pd.Series(values, index=index  , name='Tehreem') 
print("Extra parameter",f)

# # multiple indexing

values : list[int] = [1,2,3,4,5,6,7,8,9]
index  = [['a','a', 'a','b' ,'b', 'b','c', 'c', 'c'],  [1,2,3,4,5,6,7,8,9]]

f = pd.Series(values, index=index) 
print("-----------------------\n",f)




















import pandas as pd
import pandera as pa

# data to validate
df = pd.DataFrame({
    "column1": [1, 4, 0, 10, 9],
    "column2": [-1.3, -1.4, -2.9, -10.1, -20.4],
    "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"],
})

# define schema
schema = pa.DataFrameSchema({
    "column1": pa.Column(int, checks=pa.Check.le(10)),
    "column2": pa.Column(float, checks=pa.Check.lt(-1.2)),
    "column3": pa.Column(str, checks=[
        pa.Check.str_startswith("value_"),
        # define custom checks as functions that take a series as input and
        # outputs a boolean or boolean Series
        pa.Check(lambda s: s.str.split("_", expand=True).shape[1] == 2)
    ]),
})

validated_df = schema(df)
print(validated_df)