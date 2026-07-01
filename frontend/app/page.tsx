export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-slate-900 text-white p-24">
      <h1 className="text-4xl font-bold mb-4 text-emerald-400">
        Financial AI Agent (FAA) 🚀
      </h1>
      <p className="text-lg text-slate-300 mb-8">
        Arayüz ve frontend altyapısı başarıyla kuruldu. Sistem çalışmaya hazır!
      </p>
      <div className="animate-pulse flex space-x-4">
        <div className="rounded-full bg-emerald-400 h-10 w-10"></div>
        <div className="flex-1 space-y-6 py-1">
          <div className="h-2 bg-slate-700 rounded w-24"></div>
          <div className="space-y-3">
            <div className="grid grid-cols-3 gap-4">
              <div className="h-2 bg-slate-700 rounded col-span-2"></div>
              <div className="h-2 bg-slate-700 rounded col-span-1"></div>
            </div>
            <div className="h-2 bg-slate-700 rounded w-4/6"></div>
          </div>
        </div>
      </div>
    </main>
  );
}