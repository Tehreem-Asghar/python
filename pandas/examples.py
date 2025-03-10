from nptyping import NDArray, Shape
import numpy as np
from typing import Any
import pandas as pd
a: NDArray[Shape["3, 3"], Any] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



df = pd.DataFrame(a)
print(df)