# simple-ecommerce-site

### Specifications of the Simple PayPal based ECommerce website

1. Single Web Page for purchasing a bike using PayPal Smart Button

2. Maximum quantity is 3 and minimum is 1

3. After successful payment, success message is displayed on the product page

4. Language used Python with fastAPI framework

5. Sandbox user credentials - `sb-436hyn28908491@personal.example.com/lI>Z9!)+`

### Installation Steps for setting up the project

1. `pip3 install -r requirements.txt --user` has to be run from the root of the repo

2. `uvicorn app.main:app --port 8000` to run the app


### Paypal Documentation helpful links

* Dummy Cards on Paypal: https://developer.paypal.com/tools/sandbox/card-testing/

* JS SDK: https://developer.paypal.com/sdk/js/reference/#buttons

* Orders API: https://developer.paypal.com/docs/api/orders/v2/#orders_create

* Developer Dashboard: https://developer.paypal.com/dashboard/

* Integration Code and Logic: https://developer.paypal.com/docs/checkout/standard/integrate/

### Steps to generate access_token:
 curl -v -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token"\
 -u "AUHYUhlxVeI3L8v5fpKOIAja_8gmmQJQsukxOGPNjXXXXXXXXdpPhWp_zzMj:ENmHpiuN-ev8WrXXXXXJ"\
 -H "Content-Type: application/x-www-form-urlencoded"\
 -d "grant_type=client_credentials"

### Steps to test capture order:
curl -X POST "https://api-m.sandbox.paypal.com/v2/checkout/orders/55P657475A479652N/capture" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer A21AAKwC96Ystp98x1z4yU-d9rS8JPVTIAqBIEaj1jiQeAP5PAG1XXXXXXX2APAfKQx8Q9Sf4w"


