# tv-subscriber

## Description

## Usage
### 1. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install requests
pip install pybibit
pip install flask
```

### 3. Create a config file
```bash
cp config.sample.ini config.ini
```

### 4. Edit config.ini
example:
```ini
[bybit]
api_key = (your api key)
api_secret = (your api secret)

[trade]
symbol = BTCUSD
derivative_type = 'inverse'
lot = 100
max_lot = 1000
leverage = 10

[slack]
webhook_url = (your slack webhook url)
```
about each parameter:
- api_key: your bybit api key
- api_secret: your bybit api secret
- symbol: symbol to trade
- derivative_type: 'inverse' or 'linear'
- lot: lot size
- max_lot: max lot size
- leverage: leverage
- webhook_url: your slack webhook url

### 5. Run the server
```bash
python app.py
```
