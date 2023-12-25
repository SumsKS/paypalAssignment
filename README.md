# simple-ecommerce-site

### Specifications of the Simple PayPal based ECommerce website

1. Single Web Page for purchasing a bike using PayPal Smart Button

2. Maximum quantity is 3 and minimum is 1

3. After successful payment, success message is displayed on the product page

4. Language used Python with fastAPI framework

### Installation Steps for setting up the project

1. `pip3 install -r requirements.txt --user` has to be run from the root of the repo

2. `uvicorn app.main:app --port 8000` to run the app


### Paypal Documentation helpful links

* Dummy Cards on Paypal: https://developer.paypal.com/tools/sandbox/card-testing/

* JS SDK: https://developer.paypal.com/sdk/js/reference/#buttons

* Orders API: https://developer.paypal.com/docs/api/orders/v2/#orders_create

* Developer Dashboard: https://developer.paypal.com/dashboard/

* Integration Code and Logic: https://developer.paypal.com/docs/checkout/standard/integrate/

