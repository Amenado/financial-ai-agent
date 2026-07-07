import yfinance as yf
import pandas as pd

# Yahoo'nun botları engellememesi için kütüphanenin kendi içindeki ayarı kullanıyoruz
yf.set_enforce_proxy(False)

def fetch_asset_data(ticker_symbol: str):
    print(f"[{ticker_symbol}] verileri çekiliyor...")
    
    # Session yerine yfinance'ın kendi 'proxy' ve 'user-agent' mantığını tetikliyoruz
    # Ticker'ı doğrudan çağırıyoruz ama arka planda yfinance 
    # artık yeni güncellemeleriyle kendi cookie mekanizmasını daha iyi yönetiyor
    asset = yf.Ticker(ticker_symbol)
    
    # 1. Şirket / Varlık Temel Bilgileri
    # Hata almamak için burayı biraz daha "korumalı" hale getiriyoruz
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

    market_data = {
        "symbol": ticker_symbol,
        "name": short_name,
        "current_price": current_price,
        "recent_history": historical_prices
    }
    
    return market_data