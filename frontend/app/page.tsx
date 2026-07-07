'use client';

import { useState } from 'react';
import ReactMarkdown from 'react-markdown';

export default function Home() {
  const [symbol, setSymbol] = useState('BTC-USD');
  const [report, setReport] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setReport(null);

    try {
      // Bizim FastAPI backend sunucumuza istek atıyoruz
      const res = await fetch(`https://financial-ai-agent-4hb3.onrender.com`);
      if (!res.ok) {
        throw new Error('Analiz istenirken bir hata oluştu. Sunucu açık mı?');
      }
      const data = await res.json();
      if (data.status === 'success') {
        setReport(data.report);
      } else {
        throw new Error(data.detail || 'Bir hata oluştu.');
      }
    } catch (err: any) {
      setError(err.message || 'Sunucuya bağlanılamadı.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 p-4 md:p-8">
      <div className="max-w-4xl mx-auto">
        
        {/* Başlık Bölümü */}
        <header className="mb-12 text-center">
          <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-500 to-indigo-500 mb-2">
            FAA: Financial AI Agent
          </h1>
          <p className="text-slate-400 text-sm md:text-base">
            Çoklu Yapay Zeka Ajanları ile Canlı Piyasa ve Risk Analiz Platformu
          </p>
        </header>

        {/* Form Alanı */}
        <form onSubmit={handleAnalyze} className="flex flex-col sm:flex-row gap-3 mb-10 max-w-md mx-auto">
          <input
            type="text"
            value={symbol}
            onChange={(e) => setSymbol(e.target.value)}
            placeholder="Örn: BTC-USD, AAPL, TSLA"
            className="flex-1 px-4 py-3 rounded-xl bg-slate-900 border border-slate-800 text-white focus:outline-none focus:border-cyan-500 uppercase font-semibold tracking-wider text-center sm:text-left transition"
          />
          <button
            type="submit"
            disabled={loading}
            className="px-6 py-3 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-xl font-semibold hover:from-cyan-600 hover:to-blue-700 transition disabled:opacity-50 shadow-lg shadow-cyan-500/10"
          >
            {loading ? 'Ajanlar Çalışıyor...' : 'Analiz Et'}
          </button>
        </form>

        {/* Yükleniyor Durumu */}
        {loading && (
          <div className="text-center p-12 bg-slate-900/50 rounded-2xl border border-slate-900 animate-pulse max-w-2xl mx-auto">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-cyan-500 mb-4"></div>
            <p className="text-cyan-400 font-medium text-lg">Yapay Zeka Ekibi Toplantıda...</p>
            <p className="text-xs text-slate-500 mt-2 max-w-md mx-auto">
              Teknik Analist grafikleri inceliyor, Temel Analist piyasa risklerini çıkartıyor ve CIO nihai raporu derliyor. Bu işlem 10-15 saniye sürebilir.
            </p>
          </div>
        )}

        {/* Hata Mesajı */}
        {error && (
          <div className="p-4 bg-red-950/40 border border-red-950 text-red-400 rounded-xl text-center max-w-md mx-auto">
            {error}
          </div>
        )}

        {/* Başarılı Sonuç - Rapor Ekranı */}
        {report && (
          <div className="bg-slate-900/60 p-6 md:p-10 rounded-2xl border border-slate-900 shadow-2xl backdrop-blur-sm transition-all duration-300">
            <div className="prose prose-invert max-w-none text-slate-300 leading-relaxed">
              <ReactMarkdown 
                components={{
                  h1: ({node, ...props}) => <h1 className="text-2xl font-bold text-white border-b border-slate-800 pb-3 mb-6" {...props} />,
                  h2: ({node, ...props}) => <h2 className="text-xl font-semibold text-slate-200 mt-8 mb-4" {...props} />,
                  h3: ({node, ...props}) => <h3 className="text-lg font-medium text-slate-300 mt-6 mb-2" {...props} />,
                  p: ({node, ...props}) => <p className="mb-4 text-slate-300" {...props} />,
                  ul: ({node, ...props}) => <ul className="list-disc pl-5 mb-4 space-y-2 text-slate-300" {...props} />,
                  ol: ({node, ...props}) => <ol className="list-decimal pl-5 mb-4 space-y-2 text-slate-300" {...props} />,
                  li: ({node, ...props}) => <li className="text-slate-300" {...props} />,
                  strong: ({node, ...props}) => <strong className="text-cyan-400 font-semibold" {...props} />,
                  hr: ({node, ...props}) => <hr className="border-slate-800 my-6" {...props} />,
                }}
              >
                {report}
              </ReactMarkdown>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}