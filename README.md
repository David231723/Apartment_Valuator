# Apartment_Valuator

## 1. Intro

This machine learning project aims to create an apartment price valuator using a Kaggle dataset consisting of information on 20,000 apartments. The goal is to develop a machine learning model that accurately predicts the price of an apartment based on its features, such as the number of rooms, location, and amenities. To achieve this goal, we have used Python libraries such as Plotly and Streamlit for data visualization and interactive web applications. This project is aimed at providing a valuable tool for real estate agents, investors, and homeowners to accurately price apartments based on their features and location.

## 2. Data Cleaning

This project involves cleaning and transforming data in Python for a machine learning project. The process begins with importing libraries, followed by exploring the data using custom functions to identify any issues that need to be addressed.

The data cleaning process involves removing unwanted columns, dropping columns with 100% null values, dropping columns with irrelevant values, and dropping duplicates. This helps to eliminate data that is not useful for the machine learning model and makes the dataset more efficient.

The final step involves transforming the columns to prepare the data for machine learning modeling. This includes transforming variables with null values into false to create bool columns, splitting columns that contain several pieces of information, and grouping column variables for different numeric columns such as the number of rooms or bathrooms.

Overall, this project demonstrates the importance of data cleaning in machine learning projects and how to prepare the data for modeling. By using Python libraries and custom functions, we can efficiently clean and transform the data to ensure accurate and reliable machine learning results.

## 3. Linear Regression Model

The goal of the project was to create a machine learning model that predicts the price of apartments based on their features using a linear regression algorithm. The project was implemented using Python, and the resulting model had an R2 score of 0.77, indicating a reasonably good fit.The first step in the process was to clean the dataset and prepare it for analysis. This involved removing any missing or incorrect data, transforming categorical variables into numerical ones, and normalizing the data to ensure that all variables had equal weight in the analysis.Next, the dataset was split into training and testing sets to evaluate the performance of the model. The training set was used to train the model on a subset of the data, and the testing set was used to evaluate the performance of the model on new, unseen data.

Once the data was cleaned and split, a linear regression model was created using the training data. This model was then evaluated using the testing data to determine how well it would perform on new data. The R2 score of 0.77 indicates that the model was able to explain 77% of the variance in the data, which is a reasonably good fit.

In summary, the linear regression model was developed using standard data preparation and machine learning techniques in Python, and achieved a reasonably good fit with an R2 score of 0.77. The resulting model can be used to predict the price of apartments based on their features, providing a valuable tool for real estate agents, investors, and homeowners.

## 4. Visualization & Interface in Streamlit

In addition to data cleaning and building a linear regression model to predict apartment prices, this project also incorporated data visualization and a user interface. With a dataset of 20,000 rows, visualization was crucial to gain insights into the relationships between different variables and identify patterns that could help improve the model's accuracy. By using Python libraries like Plotly and Seaborn, we were able to create interactive visualizations that allowed us to explore the data in new ways.

To make the project more accessible to users, we also created an interface where users could input the features of their apartment and get an estimate of its price. The interface was built using Streamlit, a Python library for creating interactive web applications. With the interface, users can select from a range of features such as the number of rooms, location, and amenities, and get an estimate of their apartment's price based on the linear regression model. This tool can be valuable for real estate agents, investors, and homeowners looking to accurately price their apartments.

Overall, this project demonstrates the power of combining data analysis, machine learning, and user interface design to create a valuable tool that can help users make informed decisions about apartment pricing. By incorporating data visualization and an interface for user input, we were able to create a project that is not only accurate but also user-friendly and accessible.




