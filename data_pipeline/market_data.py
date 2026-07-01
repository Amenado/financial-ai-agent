import yfinance as yf
import pandas as pd

def fetch_asset_data(ticker_symbol: str):
    """
    Belirtilen sembol (Örn: AAPL, BTC-USD) için finansal verileri çeker.
    """
    print(f"[{ticker_symbol}] verileri çekiliyor...")
    
    # yfinance üzerinden varlığı tanımla
    asset = yf.Ticker(ticker_symbol)
    
    # 1. Şirket / Varlık Temel Bilgileri
    info = asset.info
    current_price = info.get("currentPrice", info.get("regularMarketPrice", "Bilinmiyor"))
    short_name = info.get("shortName", ticker_symbol)
    
    # 2. Son 5 günlük fiyat geçmişi
    # AI ajanlarına trendi göstermek için geçmiş veriyi alıyoruz
    history = asset.history(period="5d")
    
    # Geçmiş veriyi daha temiz bir sözlük (dictionary) formatına çevirelim
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

# Eğer bu dosya doğrudan çalıştırılırsa test etmek için aşağıdaki bloğu kullan
if __name__ == "__main__":
    # Test için hem bir hisse hem de bir kripto sembolü deneyelim
    test_symbol = "BTC-USD" # İstersen "NVDA" veya "MSTR" olarak değiştirebilirsin
    
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