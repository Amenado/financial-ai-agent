import os
import requests
from crewai.tools import tool

@tool("search")
def search_tool(query: str) -> str:
    """İnternette güncel finans haberlerini, kripto gelişmelerini ve piyasa gündemini aramak için kullanılır."""
    url = "https://google.serper.dev/search"
    payload = {
        "q": query,
        "num": 3 # En taze 3 haberi getir
    }
    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        # Gelen JSON verisinden sadece 'organic' (doğal arama) sonuçlarını alıyoruz
        results = response.json().get("organic", [])
        
        if not results:
            return "Aratılan konuyla ilgili güncel bir haber bulunamadı."
        
        formatted_results = []
        for r in results:
            title = r.get('title', 'Başlıksız')
            snippet = r.get('snippet', 'İçerik yok')
            formatted_results.append(f"Haber Başlığı: {title}\nÖzet: {snippet}\n---")
            
        return "\n".join(formatted_results)
        
    except Exception as e:
        return f"Arama motoru çalışırken bir hata oluştu: {str(e)}"