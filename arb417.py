import requests
import smtplib
from email.mime.text import MIMEText
import pandas as pd

# Function to fetch crypto prices from different DEXs
def get_crypto_prices():
    dex_urls = {
        'DEX1': 'https://dydx.trade/',  
        'DEX2': 'https://app.uniswap.org/#/swap',
        
        'DEX3': 'https://vertexprotocol.io/',
        
        'DEX4': 'https://app.uniswap.org/#/swap',
        
        
       
    }

    crypto_prices = {}
    for dex, url in dex_urls.items():
        response = requests.get(url)
        data = response.json()
        crypto_prices[dex] = data

    return crypto_prices

# Function to find arbitrage opportunities
def find_arbitrage_opportunities(prices):
    opportunities = []

    for crypto, values in prices.items():
        max_price = max(values.values())
        min_price = min(values.values())

        if max_price > min_price:
            profit_percentage = ((max_price - min_price) / min_price) * 100
            opportunities.append(f"Arbitrage opportunity for {crypto}: {profit_percentage:.2f}%")

    return opportunities

# Function to send email notification
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'Ikesamuel888@gmail.com'  
    msg['To'] = 'ikesamuel888@gmail.com' 

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('ikesamuel888@gmail.com', 'difiti9900example') 
        server.sendmail('ikesamuel888@gmail.com', 'ikesamuel888@gmail.com', msg.as_string())

# Fetch crypto prices from DEXs
crypto_prices = get_crypto_prices()

# Find arbitrage opportunities
arbitrage_opportunities = find_arbitrage_opportunities(crypto_prices)

# Send email notification with arbitrage opportunities
if arbitrage_opportunities:
    subject = 'Crypto Arbitrage Opportunities'
    body = '\n'.join(arbitrage_opportunities)
    send_email(subject, body)
else:
    print('No arbitrage opportunities found.')
