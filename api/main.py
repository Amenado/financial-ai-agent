from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Veri boru hattımızdaki fonksiyonu içeri aktarıyoruz
from data_pipeline.market_data import fetch_asset_data

app = FastAPI(title="FAA (Financial AI Agent) API")

# Next.js arayüzünün erişebilmesi için CORS izinleri
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "success", "message": "FAA Backend is running!"}

# Yeni Endpoint: Kullanıcının girdiği sembole göre canlı veriyi döner
@app.get("/api/market/{symbol}")
def get_market_data(symbol: str):
    try:
        # data_pipeline klasöründeki yazdığımız fonksiyonu çağırıyoruz
        data = fetch_asset_data(symbol)
        return {"status": "success", "data": data}
    except Exception as e:
        # Eğer yfinance veriyi bulamazsa veya hata olursa 404 döneceğiz
        raise HTTPException(status_code=404, detail=f"Veri çekilemedi. Sembol hatalı olabilir: {e}")