import yfinance as yf
import pandas as pd
import requests_cache

# 1. Adım: Yahoo Finance'in bizi bot olarak algılamasını engellemek için bir 'session' oluşturuyoruz.
# Bu session, her isteği sanki bir Chrome tarayıcısıymış gibi gösterir.
session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

def fetch_asset_data(ticker_symbol: str):
    """
    Belirtilen sembol için finansal verileri, ban yememek için özelleştirilmiş session ile çeker.
    """
    print(f"[{ticker_symbol}] verileri çekiliyor...")
    
    # 2. Adım: Ticker tanımlarken oluşturduğumuz 'session'ı parametre olarak veriyoruz.
    asset = yf.Ticker(ticker_symbol, session=session)
    
    # 1. Şirket / Varlık Temel Bilgileri
    info = asset.info
    current_price = info.get("currentPrice", info.get("regularMarketPrice", "Bilinmiyor"))
    short_name = info.get("shortName", ticker_symbol)
    
    # 2. Son 5 günlük fiyat geçmişi
    history = asset.history(period="5d")
    
    historical_prices = []
    if not history.empty:
        for date, row in history.iterrows():
            historical_prices.append({
                "date": date.strftime("%Y-%m-%d"),
                "close": round(row["Close"], 2),
                "volume": int(row["Volume"])
            })

    # Analiz için paketlenmiş nihai veri
    market_data = {
        "symbol": ticker_symbol,
        "name": short_name,
        "current_price": current_price,
        "recent_history": historical_prices
    }
    
    return market_data

if __name__ == "__main__":
    test_symbol = "BTC-USD"
    try:
        data = fetch_asset_data(test_symbol)
        print("\n--- ÇEKİLEN VERİ ÖZETİ ---")
        print(f"Varlık: {data['name']} ({data['symbol']})")
        print(f"Anlık Fiyat: {data['current_price']}")
        print("Son 5 Günlük Kapanışlar:")
        for day in data["recent_history"]:
            print(f" - {day['date']}: {day['close']} (Hacim: {day['volume']})")
    except Exception as e:
        print(f"Hata oluştu: {e}")