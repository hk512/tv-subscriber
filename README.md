# tv-subscriber

## Description
This is a script to trade on bybit by receiving alerts from TradingView.
## Usage
### 1. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install requests
pip install git+https://github.com/MtkN1/pybybit.git
pip install flask
```

### 3. Create a config file
```bash
cp config/config.sample.ini config/config.ini
```

### 4. Edit config.ini
example:
```ini
[bybit]
api_key = (your api key)
api_secret = (your api secret)

[trade]
symbol = BTCUSD
lot = 100
max_lot = 1000

[server]
host = 0.0.0.0
port = 80

[slack]
webhook_url = (your slack webhook url)
```
about each parameter:
- bybit
  - api_key: your bybit api key
  - api_secret: your bybit api secret
- trade
  - symbol: symbol to trade
  - lot: lot size
  - max_lot: max lot size
  - leverage: leverage
- server
  - host: host to run the server
  - port: port to run the server
- slack
  - webhook_url: your slack webhook url

### 5. Run the server
```bash
python app.py
```
