from qttp.trading_apis import CoinoneApi
import schedule
import time

def long_investment(market, invest_money):
    access          = ""
    secret          = ""
    market          = market
    invest_money    = invest_money

    trading = CoinoneApi(access, secret, market)
    ask_price = trading.ask_price(0)
    amount = round(invest_money / ask_price, 4)
    buy = trading.limit_buy(amount=amount, price=ask_price)

def klay_long_investment():
    market          = "KLAY/KRW"
    invest_money    = 4000
    long_investment(market, invest_money)

def xrp_long_investment():
    market          = "XRP/KRW"
    invest_money    = 4000
    long_investment(market, invest_money)

def xlm_long_investment():
    market          = "XLM/KRW"
    invest_money    = 4000
    long_investment(market, invest_money)

def bch_long_investment():
    market          = "BCH/KRW"
    invest_money    = 4000
    long_investment(market, invest_money)

if __name__ == "__main__":
    schedule.every().day.at("09:05").do(klay_long_investment)
    schedule.every().day.at("09:06").do(xrp_long_investment)
    schedule.every().day.at("09:07").do(xlm_long_investment)
    schedule.every().day.at("09:08").do(bch_long_investment)

    while True:
        schedule.run_pending()
        time.sleep(1)
