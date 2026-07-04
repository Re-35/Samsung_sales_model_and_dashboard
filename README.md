# Samsung Sales Analysis Project

<br>

## Introduction:
The progject concern about analyzing the sales data of Samsung company between 2021-2024, explore trends and what customers want and who intrest in Samsung products. Also, develop a prediction model using XGBOOST + RandomForest models after different tests with dashboard for explore the insights of Samsung's customers.

<br>

---

## Strategy of Project:

<br>

The project progress based on: explore the data, available tools, logic of work, test the results, then modify if needed. <br>
The strategy similar to search to learn and improve than create the best available models to get best results.

<br>

---

## Problems Occurred During the Project:

<br>

**The main problem happend during the develop predict model stage:** <br>
I tried to fit model with small features are: (category, month, year, country), but the results were bad, all models have resutls near to: -0.02 at R2 score. <br>
Then tried to feed model with more numeric data, so tried to adding: (category, month, year, country, day, units sold, payment method, channel of sale, and the price per unit), which made the result much better near to: 0.98 at R2 score. <br>
Also used at first `train_test_split` which didn't gave me better control to what I want, then tried to split them by my self that I choosed only December 2024 which didn't gave me better results (The main problem was the features), then make it more by all 2024.



<br>

---

## The Data Used:

<br>

The dataset got from [Kaggle](https://www.kaggle.com/datasets/ashyou09/samsung-global-product-sales-dataset)

<br>

---

## The Tools Used:

<br>

- **Google Colab**: For EDA process, clean data, and develop and test the best models for predict future data.
- **Visual Code**: To create simple program for prediction.
- **Power BI**: For Dashboard.

<br>

`Note: ` The project focus on the valueable result of exploring the data and learn how to create best model for predict the result based on different features.
