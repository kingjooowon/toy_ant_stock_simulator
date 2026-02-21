player = {
    "cash": 100000000
}

portfolio = {
    
}

def show_earnings_rate(portfolio, stocks):
    for name in portfolio:
        result = ((stocks[name]["price"] - portfolio[name]["avg_price"]) / portfolio[name]["avg_price"]) * 100
        print(f"\n이름: {name}")
        print(f"평가 금액: {int(stocks[name]["price"] * portfolio[name]["quantity"]):,}원")
        print(f"수익 금액: {int((stocks[name]["price"] - portfolio[name]["avg_price"]) * portfolio[name]["quantity"]):,}원")
        print(f"수익률: {result:.2f}%")