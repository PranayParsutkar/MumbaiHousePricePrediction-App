# 🏠 Mumbai House Price Prediction App
This is a machine learning capstone project that predicts house prices in Mumbai based on input features like square feet, BHK, and location. The app uses Linear Regression and is built using Python and Streamlit.

## Dataset
The dataset contains real-estate listings from Mumbai with the following columns:
- price: Price of the property (in ₹)
- sqft: Total area in square feet
- location: Locality in Mumbai
- bhk: Number of bedrooms
- Location: data/mumbaihouses.csv

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

## How to Run the App
1. download the files or clone repository.
2. Make sure you have Python installed.
3. Install required libraries using:
   pip install pandas scikit-learn streamlit
4. Run the app using:
   streamlit run app.py
5. A new tab will open in your browser: Enter values
6. Click Predict Price 

## Sample Input and Output
User Inputs :
- BHK: 3  
- Sqft: 1000  
- Location: Kharghar
Predicted Output:
- Estimated House Price: ₹ 66,80,385.36  
- R² Score: 0.82  
- Mean Absolute Error: ₹ 20,500

I have attached a screenshot of the web app showing the predicted house price output for the given inputs.
