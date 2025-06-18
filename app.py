import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

#Loading the dataset
data = pd.read_csv("data/mumbaihouses.csv")

#Converting location column into one-hot encoded columns
data = pd.get_dummies(data, columns=['location'], drop_first=True)

#Spliting the dataset into features(X) and target(y)
X = data.drop('price', axis=1)
y = data['price']

#Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creating and training the model
model = LinearRegression()
model.fit(X_train, y_train)

#Predict on the test data
y_pred = model.predict(X_test)

#Calculate performance metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

#Streamlit Web App
st.set_page_config(page_title="Mumbai House Price Prediction", page_icon="🏠")
st.title("🏠 Mumbai House Price Prediction")
st.write("This app predicts house prices in Mumbai using simple Linear Regression.")

#User inputs
bhk = st.number_input("Enter number of BHK:", min_value=1, max_value=10, step=1)
sqft = st.number_input("Enter total square feet area:", min_value=100, max_value=10000, step=10)

#Extracting location list from dataset column names
locations = [col.replace('location_', '') for col in X.columns if 'location_' in col]
selected_location = st.selectbox("Choose location:", sorted(locations))

#on clicking the Predict button
if st.button("Predict Price"):
    input_data = {
        'sqft': [sqft],
        'bhk': [bhk]
    }
    for loc in locations:
        input_data[f'location_{loc}'] = [1 if loc == selected_location else 0]
    input_df = pd.DataFrame(input_data)
    predicted_price = model.predict(input_df)[0]
    st.success(f"Estimated House Price: ₹ {round(predicted_price, 2):,}")

    # Showing model performance
    st.markdown("### 📊 Model Performance")
    st.write(f"R² Score: {r2:.3f}")
    st.write(f"Mean Absolute Error: ₹ {round(mae, 2):,}")