from api_client.bybit_client import BybitClient


class Trader(object):
    def __init__(self, api_key, api_secret, symbol, lot, max_lot):
        self.client = BybitClient(api_key=api_key, api_secret=api_secret)
        self.symbol = symbol
        self.lot = lot
        self.max_lot = max_lot

    def create_position(self, side, max_iteration=10):
        for _ in range(max_iteration):
            position_size = self.client.get_position_size(symbol=self.symbol)

            if position_size is None:
                continue

            if side == "buy":
                size = position_size["buy"]
            elif side == "sell":
                size = position_size["sell"]

            if size >= self.max_lot:
                return True

            if side == "buy":
                result = self.client.order_buy(
                    symbol=self.symbol, size=self.lot, reduce_only=False
                )
            elif side == "sell":
                result = self.client.order_sell(
                    symbol=self.symbol, size=self.lot, reduce_only=False
                )

            if result is not None:
                return True

        return False

    def close_position(self, side, max_iteration=10):
        for _ in range(max_iteration):
            position_size = self.client.get_position_size(symbol=self.symbol)

            if position_size is None:
                continue

            if side == "buy":
                size = position_size["buy"]
            elif side == "sell":
                size = position_size["sell"]

            if size == 0:
                return True

            if side == "buy":
                result = self.client.order_sell(symbol=self.symbol, size=size, reduce_only=True)
            elif side == "sell":
                result = self.client.order_buy(symbol=self.symbol, size=size, reduce_only=True)

            if result is not None:
                return True

        return False
