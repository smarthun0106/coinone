from qttp.trading_apis import CoinoneApi
import schedule
import time

def long_investment(market, invest_money):
    access          = "9130a983-8590-4beb-8a30-9b59d5b17e23"
    secret          = "f846bc98-5a74-4394-ba36-3c71b3f7b20f"
    market          = market
    invest_money    = invest_money

    trading = CoinoneApi(access, secret, market)
    ask_price = trading.ask_price(0)
    amount = round(invest_money / ask_price, 4)
    buy = trading.limit_buy(amount=amount, price=ask_price)

def btc_long_investment():
    market          = "BTC/KRW"
    invest_money    = 3000
    long_investment(market, invest_money)

def eth_long_investment():
    market          = "ETH/KRW"
    invest_money    = 3000
    long_investment(market, invest_money)

def xrp_long_investment():
    market          = "XRP/KRW"
    invest_money    = 1000
    long_investment(market, invest_money)

def xlm_long_investment():
    market          = "XLM/KRW"
    invest_money    = 1000
    long_investment(market, invest_money)

def bch_long_investment():
    market          = "BCH/KRW"
    invest_money    = 3000
    long_investment(market, invest_money)

def ltc_long_investment():
    market          = "LTC/KRW"
    invest_money    = 3000
    long_investment(market, invest_money)

def klay_long_investment():
    market          = "KLAY/KRW"
    invest_money    = 2000
    long_investment(market, invest_money)



if __name__ == "__main__":
    schedule.every().day.at("09:01").do(btc_long_investment)
    schedule.every().day.at("09:02").do(eth_long_investment)
    schedule.every().day.at("09:03").do(xrp_long_investment)
    schedule.every().day.at("09:04").do(xlm_long_investment)
    schedule.every().day.at("09:05").do(bch_long_investment)
    schedule.every().day.at("09:06").do(ltc_long_investment)
    schedule.every().day.at("09:07").do(klay_long_investment)


    while True:
        schedule.run_pending()
        time.sleep(1)
