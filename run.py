import smtplib
from email.message import EmailMessage


## get the postions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import requests

API_KEY = "your-API-Key"

request = requests.get("https://paper-trading.lemon.markets/v1/positions/", 
                       headers={"Authorization": "Bearer " + API_KEY})


r = request.json()
results = r["results"]

class Stocks():
    def __init__(self, isin, isin_title, quantity, buy_price_avg, estimated_price, estimated_price_total):
        self.isin = isin
        self.isin_title = isin_title
        self.quantity = quantity
        self.buy_price_avg = buy_price_avg
        self.estimated_price = estimated_price
        self.estimated_price_total = estimated_price_total


stocks = []

total_investment = 0

for result in results: 
    isin = result["isin"]
    isin_title = result["isin_title"]
    quantity = result["quantity"]
    buy_price_avg = result["buy_price_avg"]
    estimated_price = result["estimated_price"]
    estimated_price_total = result["estimated_price_total"]

    total_investment += estimated_price_total

    stock = Stocks(isin, isin_title, quantity, buy_price_avg, estimated_price, estimated_price_total) 
    stocks.append(stock)


total_investment = str(total_investment)
total_investment = total_investment[:3] + "." + total_investment[3:]
# print(total_investment)
total_investment = float(total_investment)
total_investment = "€ " + str(total_investment)
# print(total_investment)



## send Email ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


EMAIL_ADDRESS = "david.korn@code.berlin"
EMAIL_PASSWORD = "your-pasword"

msg = EmailMessage()
msg["Subject"] = "Your daily portfolio update"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "dkorn941@gmail.com"


html = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dispatch</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>

"""


for stock in stocks:
    isin = stock.isin
    isin_title = stock.isin_title
    quantity = stock.quantity
    buy_price_avg =  stock.buy_price_avg
    estimated_price = stock.estimated_price
    estimated_price_total = stock.estimated_price_total

    buy_price_avg = str(buy_price_avg)
    buy_price_avg = "€" + buy_price_avg[:3] + "," + buy_price_avg[3:]

    estimated_price = str(estimated_price)
    estimated_price = "€" + estimated_price[:3] + "," + estimated_price[3:]

    estimated_price_total = str(estimated_price_total)
    estimated_price_total = "€" + estimated_price_total[:3] + "," + estimated_price_total[3:]

    html += f"""\
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Dispatch</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    </head>
    <body style="font-family: 'Space Grotesk'; sans-serif;">
        <h1 style="color:#FDDC35;">&#127819; {isin_title}</h1>
        <h2 style="color:black;">{isin}</h2>
        <p style="color:black;">quantity: {quantity}</p>
        <p style="color:black;">buy price average: {buy_price_avg}</p>
        <p style="color:black;">estimated price: {estimated_price}</p>
        <p style="color:black;">estimated price total: {estimated_price_total}</p>
        <hr width="40%" color="black" align="left" />
    </body>
    </html>
    """

lemon_url = f"https://dashboard.lemon.markets/"

html += f"""
<h1>total portfolio worth: {total_investment}</h1>

<a href="{lemon_url}"
          ><button
            style="
              margin-top: 1em;
              margin-left: 50px;
              width: 50%;
              height: 40px;
              cursor: pointer;
              font-size: 20px;
              outline: none;
              background: none;
              border: none;
              border-radius: 15px;
              color: white;
              text-align: center;
              background: linear-gradient(
                to right,
                rgb(23, 158, 136),
                rgb(20, 102, 98),
                rgb(23, 158, 136)
              );
            "
          >
            lemon markets
          </button></a
        >
"""

msg.add_alternative(html, subtype="html")

def send_mail():
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


if __name__ == "__main__":
    send_mail()
