from crewai import Crew, Process
from agents.financial_agents import FinancialAgents
from agents.financial_tasks import FinancialTasks

def run_financial_analysis(market_data):
    print(f"\n--- {market_data['symbol']} İÇİN YAPAY ZEKA ANALİZİ BAŞLIYOR ---")
    
    # 1. Sınıflarımızı başlatalım
    agents = FinancialAgents()
    tasks = FinancialTasks()

    # 2. Ajanları (Çalışanları) oluştur
    tech_analyst = agents.technical_analyst()
    fund_analyst = agents.fundamental_analyst()
    cio = agents.chief_investment_officer()

    # 3. Görevleri oluştur ve çektiğimiz canlı veriyi (market_data) içlerine gönder
    task1 = tasks.technical_analysis_task(tech_analyst, market_data)
    task2 = tasks.fundamental_analysis_task(fund_analyst, market_data)
    task3 = tasks.final_report_task(cio)

    # 4. Ekibi (Crew) kur
    crew = Crew(
        agents=[tech_analyst, fund_analyst, cio],
        tasks=[task1, task2, task3],
        verbose=True,
        process=Process.sequential # Görevleri sırayla yap (Teknik -> Temel -> CIO)
    )

    # 5. Başlama vuruşunu yap ve nihai raporu döndür
    result = crew.kickoff()
    return result