from player import *
from market import *
import datetime

def sell_stock(charge):
    while True:
        print("\n--- [주식 매도] ---")
        name = input("팔 종목의 이름을 입력해주세요: ").strip()
        
        if name not in portfolio or portfolio[name]["quantity"] <= 0:
            print("X 해당 주식을 보유하고 있지 않습니다.")
            continue
        
        if name not in stocks:
            print("X 시장에서 거래되지 않는 종목입니다.")
            continue
        
        else:
            break
        
    while True:
        try:
            current_holdings = portfolio[name]["quantity"]
            count = int(input(f"판매할 수량을 입력하세요 (보유: {current_holdings}주): ").strip())
            
            if count <= 0:
                print("X 1주 이상 입력해주세요.")
            elif count <= current_holdings:
                current_price = stocks[name]["price"]
                sale_price = current_price * count
                
                player["cash"] += sale_price * (1 - charge) 
                portfolio[name]["quantity"] -= count
                
                if portfolio[name]["quantity"] == 0:
                    del portfolio[name]
                
                print(f"\n{name} {count}주 매도 완료! (+{sale_price:,}원)")
                break
            
            else:
                print("X 보유 수량이 부족합니다.")
                continue
                
        except ValueError:
            print("X 숫자만 입력해주세요.")
            continue
        
def buy_stock():
    while True:
        name = input("\n매수할 종목의 이름을 입력해주세요: ").strip()
        
        if name not in stocks:
            print("X 시장에서 거래되지 않는 종목입니다.")
            continue
        
        else:
            break
        
    while True:
        try:
            qty = int(input("매수 수량을 입력해주세요: ").strip())
            price = stocks[name]["price"]
            total_cost = price * qty
            
            if player["cash"] >= total_cost:
                player["cash"] -= total_cost
                
                if name in portfolio:
                    new_avg = int(((portfolio[name]["avg_price"] * portfolio[name]["quantity"]) + (price * qty)) / (portfolio[name]["quantity"] + qty))
                    portfolio[name]["avg_price"] = new_avg
                    portfolio[name]["quantity"] += qty
                    print(f"\n{name} {qty}주 매수 완료! (-{total_cost:,}원)")
                    break
                
                else:
                    portfolio[name] = {"quantity": qty, "avg_price": price}
                    print(f"\n{name} {qty}주 매수 완료! (-{total_cost:,}원)")
                    break
                    
            else:
                print("X 잔액이 부족합니다")
                continue
                    
        except ValueError:
            print("X 숫자만 입력해주세요.")
            continue
        
def run_game(charge, target_money):
    print(f"현재 수수료: {charge*100}%")
    print(f"현재 target money: {target_money:,}원")
    out = False
    current_date = datetime.date(2026,2,21)
    
    while True:
        if player["cash"] >= target_money:
            print("\n승리하셨습니다!")
            return
        
        if (player["cash"] <= 0) and (portfolio == {}):
            print("\n파산하셨습니다.")
            return
        
        print(f"\n--- {current_date} 국내 주식 ---")
        for key, value in stocks.items():
            print(f"{key}: {value}")
            
        print("\n--- 현재 보유 주식 ---")
        if portfolio:
            for key, value in portfolio.items():
                print(f"{key}: {value}")
        else:
            print("")
            
        print(f"\n현재 보유 현금: {player['cash']:,}원")
        
        if portfolio != {}:
            show_earnings_rate(portfolio, stocks)
            
        while True:
            select = input("=== 매도 / 매수 / 넘기기 / 게임 종료 === 중 택1: ").strip()
            
            if select == "매도":
                sell_stock(charge)
                print(f"현재 보유 현금: {int(player['cash']):,}원")
                print(f"현재 target money: {target_money:,}원")
                continue
            
            elif select == "매수":
                buy_stock()
                print(f"현재 보유 현금: {int(player['cash']):,}원")
                print(f"현재 target money: {target_money:,}원")
                continue
            
            elif select == "넘기기":
                save_stock_log(current_date, player['cash'], portfolio, stocks)
                break
            
            elif select == "게임 종료":
                out = True
                save_stock_log(current_date, player['cash'], portfolio, stocks)
                break
            
            else:
                print("Invalid input!")
                
        if out == True:
            total = 0
            print("\n게임이 종료되었습니다.")
            print("\n=== 게임 결과 ===")
            show_earnings_rate(portfolio, stocks)
            for name in portfolio:
                total += int((stocks[name]["price"] - portfolio[name]["avg_price"]) * portfolio[name]["quantity"])
            
            total += player["cash"]
            print(f"\n총 손익: {int(total-100000000):,}원")
            return
        
        target_news, target_impact = get_daily_news(stocks, news_data)
        updated_prices(stocks, target_news, target_impact)
        current_date += datetime.timedelta(days=1)
    
    
if __name__ == "__main__":
    charge = 0
    target_money = 0
    
    while True:
        difficulty = input("\n난이도를 선택하세요 (easy / normal / hard): ")
        if difficulty == "easy":
            charge = 0.001
            target_money = 150000000
            break
        elif difficulty == "normal":
            charge = 0.01
            target_money = 200000000
            break
        elif difficulty == "hard":
            charge = 0.03
            target_money = 250000000
            break
        else:
            print("Invalid Input!")
            
    print("=== 규칙 설명 ===")
    print("\n승리조건: 보유 '현금'이 target_money를 넘으면 승리")
    print("패배조건: 파산\n")
    
    run_game(charge, target_money)