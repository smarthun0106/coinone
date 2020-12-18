from qttp.trading_apis import CoinoneApi
import schedule
import time

def coinone_long_investment():
    access          = "9130a983-8590-4beb-8a30-9b59d5b17e23"
    secret          = "f846bc98-5a74-4394-ba36-3c71b3f7b20f"
    market          = "KLAY/KRW"
    invest_money    = 7000

    trading = CoinoneApi(access, secret, market)
    ask_price = trading.ask_price(0)
    amount = round(invest_money / ask_price, 4)
    buy = trading.limit_buy(amount=amount, price=ask_price)

if __name__ == "__main__":
    schedule.every().day.at("14:01").do(coinone_long_investment)

    while True:
        schedule.run_pending()
        time.sleep(1)
