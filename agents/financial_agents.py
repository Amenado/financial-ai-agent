import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from agents.tools import search_tool

# .env dosyasındaki şifreleri sisteme yüklüyoruz
load_dotenv()

# CrewAI'ın kendi LLM sınıfını kullanarak Gemini modelini tanımlıyoruz
# Bu yöntem, CrewAI ile tam uyumludur ve validation hatalarını engeller
llm = LLM(
    model="gemini/gemini-3.1-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY")
)

class FinancialAgents:
    def technical_analyst(self):
        return Agent(
            role='Kıdemli Teknik Analist',
            goal='Finansal varlıkların fiyat hareketlerini analiz etmek.',
            backstory='Sen 15 yıllık deneyime sahip, algoritmik ticaret ve grafik okuma uzmanı bir teknik analistsin.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def fundamental_analyst(self):
        return Agent(
            role='Makroekonomi Uzmanı',
            goal='İnternetteki en güncel piyasa haberlerini taramak ve temel metrikleri yorumlamak.',
            backstory='Küresel piyasaları takip eden, son dakika haberlerini analiz edip fiyatlara etkisini yorumlayan deneyimli bir ekonomistsin.',
            verbose=True,
            allow_delegation=False,
            tools=[search_tool], # 2. YENİ EKLENEN SATIR: Ajanın eline arama motorunu verdik!
            llm=llm
        )

    def chief_investment_officer(self):
        return Agent(
            role='Baş Yatırım Sorumlusu (CIO)',
            goal='Analizleri birleştirip profesyonel bir yatırım raporu yazmak.',
            backstory='Bir hedge fonunun yöneticisisin, net ve kararlı yatırım tavsiyeleri verirsin.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )