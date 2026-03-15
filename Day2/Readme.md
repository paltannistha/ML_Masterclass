# Day 2: Linear Regression Example

In this example, we build a simple **Linear Regression** model to predict student marks based on hours studied.

## Dataset

| Hours Studied | Marks |
|---------------|------|
| 1 | 35 |
| 2 | 40 |
| 3 | 50 |
| 4 | 60 |
| 5 | 70 |

## Python Code

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# dataset
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([35,40,50,60,70])

# model
model = LinearRegression()
model.fit(X, y)

# prediction
print(model.predict([[6]]))