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


 }