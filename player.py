player = {
    "cash": 10000000
}

portfolio = {
    "name": {"quantity": 1, "avg_price": 100}
}

def show_earnings_rate(portfolio, stocks):
    for name in portfolio:
        result = ((stocks[name]["price"] - portfolio[name]["avg_price"]) / portfolio[name]["avg_price"]) * 100
        print(f"\n평가 금액: {stocks[name]["price"] * portfolio[name]["quantity"]:.2f}")
        print(f"수익 금액: {(stocks[name]["price"] - portfolio[name]["avg_price"]) * portfolio[name]["quantity"]:.2f}")
        print(f"수익률: {result:.2f}%")