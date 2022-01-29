
# Problem statement
With the given 9 features(categorical and continuous) build a model to predict the price of houses.

# Description
This Model/WebApp predicts real estate price. Many times we have come across websites like "Magicbricks.com" where they sell and estimate the price of the property in many part of the country, so this model is also inspired by the concept of predicting property prices based on the area, bedrooms, bathrooms and location. Firstly I built the model using sklearn and machine learning algorithm using home prices dataset. Second step was to write a python code using Streamlit that uses the saved model to serve http requests. Third component was to deploy the model on heroku that allows user to enter home square ft area, bedrooms etc and it will call the model to retrieve the predicted price. During model building I came across all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering etc.

## Data:
- The train and test data will consist of various features that describe that property.
- Each row contains fixed size object of features. There are 9 features and each feature can be accessed by its name.

### Features:
1. Area_type – describes the area
2. Availability – when it can be possessed or when it is ready(categorical and time-series)
3. Location – where it is located in Bengaluru (Area name)
4. Size – in BHK or Bedroom (1-10 or more)
5. Society – to which society it belongs
6. Total_sqft – size of the property in sq.ft
7. Bath – No. of bathrooms
8. Balcony – No. of the balcony

## Technologies used

1.  Python
2.  Numpy and Pandas for data cleaning
3.  Matplotlib and Seaborn for data visualization
4.  Sklearn for model building
5.  Jupyter notebook, visual studio code as IDE
6.  Streamlit for Deployment
7. 
## Deployment
This Web App is deployed to cloud (AWS EC2) where it can be accesssed. Running last command above will prompt that server is running on port 5000. 8. Now just load your cloud url in browser (for me it was ), website will open but it will not work unless I run this app's server in virtual OS Ubuntu.

Web App Link(Heroku) -  [Visit here](https://www.house-price-demo.herokuapp.com/)


## Screenshot

