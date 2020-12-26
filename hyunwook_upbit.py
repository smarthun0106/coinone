from qttp.trading_apis import UpbitApi
import schedule
import time

def long_investment(market, invest_money):
    access          = ""
    secret          = ""
    market          = market
    invest_money    = invest_money

    trading = UpbitApi(access, secret, market)
    ask_price = trading.ask_price(0)
    amount = round(invest_money / ask_price, 4)
    buy = trading.limit_buy(amount=amount, price=ask_price)

def xrp_long_investment():
    market          = "KRW-XRP"
    invest_money    = 1000
    long_investment(market, invest_money)

def xlm_long_investment():
    market          = "KRW-XLM"
    invest_money    = 1000
    long_investment(market, invest_money)

def bch_long_investment():
    market          = "KRW-BCH"
    invest_money    = 1000
    long_investment(market, invest_money)

if __name__ == "__main__":
    schedule.every().day.at("19:26").do(xrp_long_investment)
    schedule.every().day.at("19:26").do(xlm_long_investment)
    schedule.every().day.at("19:26").do(bch_long_investment)

    while True:
        schedule.run_pending()
        time.sleep(1)
