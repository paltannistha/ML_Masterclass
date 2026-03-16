# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Step 1: Dataset
# House size (in square feet)
X = np.array([[500], [800], [1000], [1200], [1500]])

# House price (in thousands)
y = np.array([50, 80, 100, 120, 150])

# Step 2: Train model
model = LinearRegression()
model.fit(X, y)

# Step 3: Predict price of 1100 sq ft house
predicted_price = model.predict([[1100]])
print("Predicted price for 1100 sq ft house:", predicted_price[0])

# Step 4: Predictions for regression line
y_pred = model.predict(X)

# Step 5: Model evaluation
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print("R2 Score:", r2)
print("MSE:", mse)
print("RMSE:", rmse)

# Step 6: Visualization
plt.scatter(X, y, label="Actual Prices")
plt.plot(X, y_pred, label="Regression Line")

plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (thousands)")
plt.title("Linear Regression: House Price Prediction")
plt.legend()

plt.show()