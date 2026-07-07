# 1. Aşama: Olabildiğince hafif, resmi bir Python işletim sistemi (imajı) indiriyoruz
FROM python:3.11-slim

# 2. Aşama: Konteynerin içindeki çalışma klasörümüzü belirliyoruz
WORKDIR /app

# 3. Aşama: Sadece requirements.txt dosyasını kopyalıyoruz (Hızlı kurulum için önbellek taktiği)
COPY requirements.txt .

# 4. Aşama: Projenin ihtiyaç duyduğu kütüphaneleri konteynerin içine kuruyoruz
RUN pip install --no-cache-dir -r requirements.txt

# 5. Aşama: Kalan tüm proje dosyalarımızı (agents klasörü vb.) içeri kopyalıyoruz
COPY . .

# 6. Aşama: Uygulamanın dış dünyayla haberleşeceği portu açıyoruz
EXPOSE 8000

# 7. Aşama: Konteyner ayağa kalktığında çalıştırılacak nihai komut
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]