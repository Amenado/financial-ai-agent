from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Kendi yazdığımız modülleri içeri aktarıyoruz
from data_pipeline.market_data import fetch_asset_data
from agents.crew_runner import run_financial_analysis

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

# Sadece ham veriyi getiren eski endpoint
@app.get("/api/market/{symbol}")
def get_market_data(symbol: str):
    try:
        data = fetch_asset_data(symbol)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# YENİ EKLENEN: Yapay Zeka Analiz Endpoint'i
@app.get("/api/analyze/{symbol}")
def analyze_asset(symbol: str):
    try:
        # 1. Adım: Veriyi çek
        market_data = fetch_asset_data(symbol)
        
        # 2. Adım: Veriyi yapay zeka ekibine yolla ve raporu al
        ai_report = run_financial_analysis(market_data)
        
        # CrewAI'nin sonucunu string'e (metne) çevirip gönderiyoruz
        return {"status": "success", "symbol": symbol, "report": str(ai_report)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Yapay zeka analizi sırasında hata oluştu: {e}")