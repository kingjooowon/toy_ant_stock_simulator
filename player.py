import csv, os
 
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
        
def save_stock_log(date, cash, portfolio, stocks):
    stock_value = 0
    for name, info in portfolio.items():
        stock_value += stocks[name]["price"] * info["quantity"]
        
    total_assets = int(cash + stock_value)
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    file_path = 'data/stock_log.csv'
    file_exists = os.path.isfile(file_path)
    
    with open(file_path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        if not file_exists:
            writer.writerow(["Data", "Cash", "StockValue", "TotalAssets"])
        writer.writerow([date, int(cash), int(stock_value), total_assets])