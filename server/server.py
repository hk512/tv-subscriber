import ipaddress
import logging

from flask import abort
from flask import Flask
from flask import jsonify
from flask import request

from controller.trader import Trader
from controller.notificator import Notificator
from config import config

app = Flask(__name__)
logger = logging.getLogger(__name__)

# allowed ip address
ALLOW_NETWORKS = ["52.89.214.238", "34.212.75.30", "54.218.53.128", "52.32.178.7"]


@app.before_request
def before_request():
    remote_address = ipaddress.ip_address(request.remote_addr)
    for allow_network in ALLOW_NETWORKS:
        ip_network = ipaddress.ip_network(allow_network)
        if remote_address in ip_network:
            return

    return abort(403, "access denied your IP address")


@app.route("/", methods=["POST"])
def run():
    signal = request.data.decode()

    logger.info({"action": "run", "signal": signal})

    trader = Trader(
        api_key=config.api_key,
        api_secret=config.api_secret,
        symbol=config.symbol,
        lot=config.lot,
        max_lot=config.max_lot,
    )

    notificator = Notificator(config.webhook_url)

    if signal == "Buy":
        close_position_result = trader.close_position("sell")

        if not close_position_result:
            msg = "Failed to close the sell position."
            notificator.notify(msg)
            return jsonify({"result": -1, "msg": msg}), 400

        create_position_result = trader.create_position("buy")

        if not create_position_result:
            msg = "Failed to create the sell position."
            notificator.notify(msg)
            return jsonify({"result": -1, "message": msg}), 400

    elif signal == "Sell":
        close_position_result = trader.close_position("buy")

        if not close_position_result:
            msg = "Failed to close the buy position."
            notificator.notify(msg)
            return jsonify({"result": -1, "msg": msg}), 400

        create_position_result = trader.create_position("sell")

        if not create_position_result:
            msg = "Failed to create the sell position."
            notificator.notify(msg)
            return jsonify({"result": -1, "msg": msg}), 400

    else:
        return jsonify({"result": -1}), 400

    return jsonify({"result": 0}), 200
