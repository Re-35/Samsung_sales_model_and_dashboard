# import libraries:
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# define scalar:
scalar = StandardScaler()

# load the models:
xgb = joblib.load(r'C:\Users\R1alm\Desktop\sam_model\xgb_model.joblib')
rf = joblib.load(r'C:\Users\R1alm\Desktop\sam_model\rf_model.joblib')

models = [xgb, rf]

# define the method of prediction:
def pred_1_month(model, scalar, arr):
    result = 0
    pred = 0

    for i in range(1,31):
        arr[0, 9] = i
        arr_scaled = scalar.fit_transform(arr)
        pred = model.predict(arr_scaled)
        result = result + pred[0]

    return result

# define the main method:

def main_app(scalar, models):
    print('==========   Samsung Sales Model Prediction   ==========')
    print(f'Please choose the below 9 values for each:\n- Year.\n- Month.\n- Country.\n- Category.\n- Discount %.\n- Maen of units sold per day.\n- Price of product in USD.\n- Sale channel.\n- Payment method.')
    
    year = int(input('Enter the year (ex:2026): '))
    month = int(input('Enter the month (1-12): '))
    country = int(input(f'(0- Austria. | 1- Canada. | 2- France. | 3- Greece. | 4- Norway. | 5- Saudi Arabia. | 6- South Korea. | 7- Sri Lanka. | 8- Taiwan. | 9- UAE. | 10- Vietnam.)\nEnter the number of country: '))
    category = int(input(f'(0- Accessories. | 1- Galaxy A. | 2- Monitor. | 3- Appliances. | 4- Galaxy S. | 5- Galaxy Tab. | 6- Galaxy Watch. | 7- Galaxy M. | 8- Galazy Z. | 9- Galaxy Buds. | 10- Smart TV.)\nEnter the number of category: '))
    disc = float(input(f'Enter the discount (ex: 20 = %20, 0 = %0): '))
    units_sold = int(input('Enter th AVG units sold per each transaction (ex: 2 - each transaction had sold 2 pices of same category): '))
    price = float(input('Enter the price of the product in USD (discount will applied automatically): '))
    channel = int(input(f'(0- E-commerce Platform. | 1- Third-Party Retailer. | 2- Samsung Store. | 3- Authorized Reseller. | 4- Carrier Store. | 5- Corporate / B2B. | 6- Online (Samsung.com).)\nEnter the number of channel: '))
    payment = int(input(f'(0- Credit Card. | 1- Gift Card. | 2- Cash. | 3- EMI / Installment. | 4- Debit Card. | 5- Net Banking. | 6- BNPL (Buy Now Pay Later). | 7- Samsung Pay.)\nEnter the number of payment method: '))


    # apply discount:
    dis = (price * disc) / 100
    price = price - dis
    202
    # gather data into 2D array:
    # 0 at end of the array locate day place:
    arr = np.array([[year, month, country, category, disc, units_sold, price, channel, payment, 0]])

    xgb_result = pred_1_month(model=models[0], scalar=scalar, arr=arr)
    rf_result = pred_1_month(model=models[1], scalar=scalar, arr=arr)

    pred_arr = np.array([xgb_result, rf_result])

    print(f'The expected result of sales at ({year} / {month}) around: {pred_arr.min()} - {pred_arr.max()}')


main_app(models=models, scalar=scalar)