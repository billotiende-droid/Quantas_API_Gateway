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
     
    </div>
  </main>
)

 }