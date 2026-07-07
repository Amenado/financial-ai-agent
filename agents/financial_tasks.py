from crewai import Task
from datetime import datetime

class FinancialTasks:
    def technical_analysis_task(self, agent, market_data):
        return Task(
            description=f'''
            Aşağıda {market_data['name']} ({market_data['symbol']}) için güncel piyasa verileri bulunmaktadır:
            - Anlık Fiyat: {market_data['current_price']}
            - Son 5 Günlük Kapanışlar: {market_data['recent_history']}
            
            Görev: Bu 5 günlük fiyat hareketine ve hacim değişimlerine bakarak kısa vadeli bir teknik analiz yap. 
            Trend yukarı mı aşağı mı? Hacim fiyatı destekliyor mu? 
            Raporunu net paragraflarla yaz.
            ''',
            expected_output='Varlığın fiyat hareketlerine dayanan detaylı bir teknik analiz raporu.',
            agent=agent
        )

    def fundamental_analysis_task(self, agent, market_data):
        simdi = datetime.now()
        # Arama motoru global olduğu için ay ismini İngilizce alıyoruz (Örn: "July 2026")
        guncel_ay_yil = simdi.strftime("%B %Y") 

        return Task(
            description=f'''
            {market_data['name']} ({market_data['symbol']}) varlığı için güncel makro durumu değerlendir.
            
            GÖREVİN: 
            1. "search" adlı arama aracını kullanarak küresel piyasa durumunu tarat.
            2. Arama motorunun tam olarak bu aya ait analizleri bulması için sorguları şu formatta gönder:
               - "{market_data['symbol']} news {guncel_ay_yil}"
               - "crypto market analysis {guncel_ay_yil}"
               - "Bitcoin updates {guncel_ay_yil}"
            3. ÖNEMLİ ZAMAN ALGISI: Şu an {guncel_ay_yil} dönemindeyiz. Gelen haberlerin bu döneme ait taze gelişmeler olduğunu bilerek yorumla.
            4. Gelecek olan İngilizce haber özetlerini oku, analiz et ve nihai raporunu TÜRKÇE olarak tamamla.
            ''',
            expected_output=f'{guncel_ay_yil} dönemine ait taze küresel haberlerin Türkçe makro analizi.',
            agent=agent
        )

    def final_report_task(self, agent):
        # Sistemden bugünün tarihini dinamik olarak çekiyoruz
        bugunun_tarihi = datetime.now().strftime("%d %B %Y")
        
        return Task(
            description=f'''
            Teknik analist ve Temel analistin yazdığı raporları dikkatlice oku. 
            Bu iki raporu birleştirerek profesyonel bir "Yatırımcı Yönetici Özeti" (Executive Summary) oluştur.
            
            ÖNEMLİ: Raporun en üstüne kesinlikle bugünün tarihini ekle. Bugünün tarihi: {bugunun_tarihi}.
            
            Raporun Markdown formatında şık, başlıkları olan ve net bir "Sonuç/Tavsiye" bölümü içeren bir yapıya sahip olmalı.
            ''',
            expected_output='Markdown formatında birleştirilmiş, güncel tarihli ve profesyonel nihai yatırım raporu.',
            agent=agent
        )