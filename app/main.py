from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from fastapi.responses import FileResponse
import httpx
import json

from .constants import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)


templates = Jinja2Templates(
    directory=Path(__file__).parent.parent.absolute() / "templates"
)


def generate_access_token():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    response = httpx.post(
        OAUTH_TOKEN_URL, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET), data=data
    )
    return json.loads(response.text)["access_token"]


ACCESS_TOKEN = generate_access_token()


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


class CreateOrder(BaseModel):
    name: str
    description: str
    quantity: str
    perUnitPrice: str
    totalPrice: str


@app.post("/create_order")
async def create_order(create_order: CreateOrder):
    order_data = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "description": "Paypal Order",
                "amount": {
                    "currency_code": "USD",
                    "value": int(create_order.totalPrice),
                },
            }
        ],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API_BASE_URL}/v2/checkout/orders",
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
            json=order_data,
        )

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Failed to create order"
            )


class CaptureOrder(BaseModel):
    orderID: str


@app.post("/capture_order")
async def create_order(order_id: CaptureOrder):
    order_id = order_id.orderID
    print(order_id)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API_BASE_URL}/v2/checkout/orders/{order_id}/capture",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {ACCESS_TOKEN}",
            },
        )

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Failed to create order"
            )


# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
