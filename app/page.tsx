// app page.tsx
'use client';
import {useState, useEffect} from 'react';

// Improvement: Typescript Interfaces
interface Wallet {
  currency: string;
  balance: number;
  user: string;
}

export default function QuantasDashboard () {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);


useEffect (() => {
  const load = async () => {
    const res = await fetch("http://localhost:8000/api/vi/settlement/1");
    const json = await res.json();
    setData(json);
    setLoading(false);
  };
  load()
}, []); 

return (
  <main className='min-h-screen bg-[#F8FAFC] p-4 text-slate-900 font-sans'>
    <div className='max-w-md mx-auto pt-8'>
      {/* Header Section */}
      <div className='flex justify-between items-end mb-8'>
        <div>
          <h1 className='text-sm font-bold text-blue-600 uppercase tracking-widest'>Quantas Gateway</h1>
          <p className='text-3xl font-extrabold'>Settlement</p>
        </div>
        {data?.cached && (
          <span className='text-[10px] bg-amber-100 text-amber-700 px-2 py-1 rounded font-bold'>CACHED</span>
        )}
      </div>
      {/* Wallet Cards */}
      <div className='space-y-4'>
        {loading ? [1, 2].map(i => <div key={i} className='h-32 bg-slate-200 animate-pulse rounded-3xl' />):
        data?.data?.map((wallet: Wallet, i:number) => (
          <div key={i} className='bg-white p-6 rounded-[2rem] shadow-xl shadow-slate-200/50 border border-white relative overflow-hidden group transition-all hover:shadow-2xl'>
            <div className='flex justify-between items-start'>
              <div>
                <p className='text-slate-400 text-xs font-bold uppercase mb-1'>{wallet.currency} Assets </p>
                <p className='text-4xl font-mono font-bold tracking-lighter'>
                  {wallet.balance.toLocaleString()}
                </p>
              </div>
              <div className='bg-slate-100 p-3 rounded-2xl group-hover:bg-blue-50 transition-colors'>
                <span className='font-bold text-blue-600'>{wallet.currency} </span>
            </div>
          </div>
        </div>
        ))}
      </div>
      {/* Stats Footer */}
      <footer className='mt-10 p-6 bg-slate-900 rounded-[2rem] text-white'>
        <p className='text-slate-400 text-xs mb-2'>Market Indicators</p>
        <div className='flex justify-between font-mono text-sm'>
          <span>BTC/USD</span>
          <span className='text-green-400'>↑ {data?.rates?.BTC} </span>
        </div>
      </footer>
    </div>
  </main>
);}