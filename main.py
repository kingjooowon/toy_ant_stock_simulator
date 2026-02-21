from player import player, portfolio
from market import stocks

def sell_stock():
    print("--- [주식 매도] ---")
    name = input("팔 종목의 이름을 입력해주세요: ")
    
    if name not in portfolio or portfolio[name]["quantity"] <= 0:
        print("X 해당 주식을 보유하고 있지 않습니다.")
        return
    
    if name not in stocks:
        print("X 시장에서 거래되지 않는 종목입니다.")
        return
    
    try:
        current_holdings = portfolio[name]["quantity"]
        count = int(input(f"판매할 수량을 입력하세요 (보유: {current_holdings}주): "))
        
        if count <= 0:
            print("X 1주 이상 입력해주세요.")
        elif count <= current_holdings:
            current_price = stocks[name]["price"]
            sale_price = current_price * count
            
            player["cash"] += sale_price
            portfolio[name]["quantity"] -= count
            
            if portfolio[name]["quantity"] == 0:
                del portfolio[name]
            
            print(f"{name} {count}주 매도 완료! (+{sale_price:,}원)")
        else:
            print("X 보유 수량이 부족합니다.")
            
    except ValueError:
        print("X 숫자만 입력해주세요.")
        
def buy_stock():
    name = input("매수할 종목의 이름을 입력해주세요: ")
    
    if name not in stocks:
        print("X 시장에서 거래되지 않는 종목입니다.")
        return
    
    try:
        qty = int(input("매수 수량을 입력해주세요: "))
        price = stocks[name]["price"]
        total_cost = price * qty
        
        if player["cash"] >= total_cost:
            player["cash"] -= total_cost
            
            if name in portfolio:
                new_avg = int(((portfolio[name]["avg_price"] * portfolio[name]["quantity"]) + (price * qty)) / (portfolio[name]["quantity"] + qty))
                portfolio[name]["avg_price"] = new_avg
                portfolio[name]["quantity"] += qty
            
            else:
                portfolio[name] = {"quantity": qty, "avg_price": price}
                
        else:
            print("X 잔액이 부족합니다")
            return
                
    except ValueError:
        print("X 숫자만 입력해주세요.")