import random

stocks = {
    "SK하이닉스": {"price": 943000, "volatility": 0.055},
    "삼성전자": {"price": 190300, "volatility": 0.015},
    "두산에너빌리티": {"price": 103900, "volatility": 0.056},
    "한화오션": {"price": 149000, "volatility": 0.060},
    "SK이터닉스": {"price": 29950, "volatility": 0.055},
    "삼현": {"price": 53200, "volatility": 0.014},
    "삼성SDI": {"price": 402500, "volatility": 0.013},
    "S-OIL": {"price": 120600, "volatility": 0.087},
    "부국증권": {"price": 101300, "volatility": 0.201},
    "한화시스템": {"price": 116000, "volatility": 0.090}
}

news_data = {
    "good": [
        "꿈에서 할아버지가 이 종목을 사라고 말씀하셨다..",
        "주식 커뮤니티에서 이 종목이 핫하던데.."
    ],
    "bad": [
        "오늘은 뭔가 느낌이 좋다",
        "내 친구가 이 종목을 사라고 추천해줬는데.."
    ]
}

def get_daily_news(stocks, news_data):
    impact = 0.0
    
    if random.random() <= 0.3:
        target_stock = random.choice(list(stocks.keys()))
        
        if random.random() <= 0.2:
            impact = random.randint(15,30) / 100
        else:
            impact = random.randint(6,15) / 100
        
        sign = random.choice(list(news_data.keys()))
        print(f"\n{target_stock}에 관한 뉴스가 공개되었습니다.")
        
        if sign == "good":
            print(random.choice(news_data["good"]))
            print("\n호재 - 주가 상승 확률 UP!")
            return (target_stock, impact)
        
        else:
            print(random.choice(news_data["bad"]))
            print("\n악재 - 주가 하락 확률 UP!")
            return (target_stock, -impact)
        
    else:
        return None, 0.0
    
def updated_prices(stocks, target=None, impact=0.0):
    for name in stocks.keys():
        vol = stocks[name]["volatility"]
        change = random.uniform(-vol, vol)
        
        if name == target:
            stocks[name]["price"] = int(stocks[name]["price"] * (1 + change + impact))
        else:
            stocks[name]["price"] = int(stocks[name]["price"] * (1 + change))