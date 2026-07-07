import yfinance as yf
import pandas as pd

def fetch_asset_data(ticker_symbol: str):
    """
    Yahoo Finance'den veri çekmek için en güncel ve güvenli yöntem.
    """
    print(f"[{ticker_symbol}] verileri çekiliyor...")
    
    # yfinance'ın kendi içinde otomatik cookie/crumb yönetimi var.
    # Ona müdahale etmiyoruz, sadece Ticker'ı oluşturuyoruz.
    asset = yf.Ticker(ticker_symbol)
    
    # info bilgisini çekerken bir 'timeout' (zaman aşımı) ekliyoruz
    # Bulut sunucularında bazen bağlantı yavaş olabilir.
    info = asset.info
    
    current_price = info.get("currentPrice", info.get("regularMarketPrice", "Bilinmiyor"))
    short_name = info.get("shortName", ticker_symbol)
    
    # Geçmiş veri
    history = asset.history(period="5d")
    
    historical_prices = []
    if not history.empty:
        for date, row in history.iterrows():
            historical_prices.append({
                "date": date.strftime("%Y-%m-%d"),
                "close": round(row["Close"], 2),
                "volume": int(row["Volume"])
            })

    return {
        "symbol": ticker_symbol,
        "name": short_name,
        "current_price": current_price,
        "recent_history": historical_prices
    }