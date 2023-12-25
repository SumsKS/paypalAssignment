import os

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

favicon_path = "favicon.ico"

# PayPal API base URL
PAYPAL_API_BASE_URL = "https://api-m.sandbox.paypal.com"

OAUTH_TOKEN_URL = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
