import logging

import pybybit

logger = logging.getLogger(__name__)


class BybitClient(object):
    def __init__(self, api_key, api_secret, testnet=False):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet

    def order_buy(self, symbol, size, reduce_only=False):
        logger.info(
            {
                "action": "order_buy",
                "symbol": symbol,
                "size": size,
                "reduce_only": reduce_only,
            }
        )
        return self.order(symbol=symbol, side="Buy", size=size, reduce_only=reduce_only)

    def order_sell(self, symbol, size, reduce_only=False):
        logger.info(
            {
                "action": "order_sell",
                "symbol": symbol,
                "size": size,
                "reduce_only": reduce_only,
            }
        )
        return self.order(
            symbol=symbol, side="Sell", size=size, reduce_only=reduce_only
        )

    def order(self, symbol, side, size, reduce_only=False):
        logger.info(
            {
                "action": "order",
                "symbol": symbol,
                "side": side,
                "size": size,
                "reduce_only": reduce_only,
            }
        )

        client = pybybit.API(
            key=self.api_key, secret=self.api_secret, testnet=self.testnet
        )

        if symbol[-4:] == "USDT":
            res = client.rest.linear.private_order_create(
                side=side,
                symbol=symbol,
                order_type="Market",
                qty=size,
                reduce_only=reduce_only,
                time_in_force="GoodTillCancel",
                close_on_trigger=False,
            )

        elif symbol[-3:] == "USD":
            res = client.rest.inverse.private_order_create(
                side=side,
                symbol=symbol,
                order_type="Market",
                qty=int(size),
                time_in_force="GoodTillCancel",
                close_on_trigger=False,
            )
        else:
            return None

        logger.info({"action": "order", "status_code": res.status_code})

        if res.status_code == 200:
            response_data = res.json()
            logger.info({"action": "order", "response_data": response_data})
            if response_data["ret_code"] == 0:
                return response_data

    def get_positions(self, symbol):
        logger.info({"action": "get_positions", "symbol": symbol})
        client = pybybit.API(
            key=self.api_key, secret=self.api_secret, testnet=self.testnet
        )

        if symbol[-4:] == "USDT":
            res = client.rest.linear.private_position_list(symbol=symbol)
        elif symbol[-3:] == "USD":
            res = client.rest.inverse.private_position_list(symbol=symbol)
        else:
            return None

        logger.info({"action": "get_positions", "status_code": res.status_code})

        if res.status_code == 200:
            response_data = res.json()
            logger.info({"action": "get_positions", "response_data": response_data})
            if response_data["ret_code"] == 0:
                return response_data

    def get_position_size(self, symbol) -> {str: float}:
        response_data = self.get_positions(symbol=symbol)

        if response_data is None:
            return None

        result = response_data["result"]

        if symbol[-4:] == "USDT":
            position_size = {"buy": result[0]["size"], "sell": result[1]["size"]}
        elif symbol[-3:] == "USD":
            if result["side"] == "Buy":
                position_size = {"buy": result["size"], "sell": 0}
            else:
                position_size = {"buy": 0, "sell": result["size"]}
        else:
            return None

        logger.info({"action": "get_position_size", "position_size": position_size})

        return position_size
