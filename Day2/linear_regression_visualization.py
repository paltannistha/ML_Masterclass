# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create dataset
# Hours studied (feature)
X = np.array([[1], [2], [3], [4], [5]])

# Marks obtained (label)
y = np.array([35, 40, 50, 60, 70])

# Step 2: Create and train the model
model = LinearRegression()
model.fit(X, y)

predicted_marks = model.predict([[6]])
print("Predicted marks for 6 hours of study:", predicted_marks[0])

# Step 4: Predict values for the regression line
y_pred = model.predict(X)

# Step 5: Visualization
plt.scatter(X, y, label="Actual Data")     # data points
plt.plot(X, y_pred, label="Regression Line")  # predicted line

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Linear Regression Example")
plt.legend()

plt.show()