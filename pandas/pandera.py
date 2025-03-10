# DataFram

# more than two coloumns
import pandas as pd
from nptyping import NDArray, Shape
import numpy as np
from typing import Any



# Key
# Value : iterable
# length should be same as length of others Series

a : pd.Series = pd.Series([1,2,3,4,5,6,7,8,9] , name="student_id")
b : pd.Series= pd.Series([10,20,30,40,50,60,70,80,90] , name="Marks")
c : pd.Series= pd.Series(["taha","arfa", "sarim" , "aysha" , "tehreem" , "aina" , "arham", "afaq" , "hadi"], name="Name")

dt : pd.DataFrame = pd.DataFrame({"Student_id" : a , "Marks" : b , "Name" : c})
print(dt)



# second Example 

dt : pd.DataFrame = pd.concat([ a , b , c] , axis=1)
print("--------------------------------------------------------\n",dt)


# another example 

e : pd.DataFrame = pd.concat([a,b,c])
print("--------------------------------------------------------\n",e)



list = [[1,2,3] , [4,5,6] , [7,8,9]]
l : pd.DataFrame = pd.DataFrame(list)
print("--------------------------------------------------------\n",l)
l : pd.DataFrame = pd.DataFrame(list , columns=["a" , "b" , "c"])
print("--------------------------------------------------------\n",l)
 
print(l.columns)
print(l.index)
print(l.dtypes)



m = pd.read_html("https://www.w3schools.com/python/python_operators.asp")
print(m)