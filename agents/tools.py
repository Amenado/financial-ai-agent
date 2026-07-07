from crewai.tools import tool
from duckduckgo_search import DDGS

@tool("search") # İsmi tamamen İngilizce ve tek kelime yaptık
def search_tool(query: str) -> str:
    """İnternette güncel finans haberlerini, kripto gelişmelerini ve piyasa gündemini aramak için kullanılır."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            if not results:
                return "Aratılan konuyla ilgili güncel bir haber bulunamadı."
            
            formatted_results = []
            for r in results:
                title = r.get('title', 'Başlıksız')
                body = r.get('body', 'İçerik yok')
                formatted_results.append(f"Haber Başlığı: {title}\nÖzet: {body}\n---")
                
            return "\n".join(formatted_results)
            
    except Exception as e:
        return f"Arama motoru çalışırken bir hata oluştu: {str(e)}"