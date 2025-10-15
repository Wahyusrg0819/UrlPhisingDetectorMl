'use client'

import { useState } from 'react'

interface PredictionResult {
  url: string
  prediction: string
  confidence?: number
  probabilities: Record<string, number>
  features: {
    url_length: number
    num_dots: number
    has_www: boolean
    has_https: boolean
    num_hyphens: number
    num_slashes: number
    has_numeric: boolean
  }
  model_info?: {
    algorithm: string
    n_estimators: number
    classes: string[]
  }
}

export default function Home() {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<PredictionResult | null>(null)
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    setResult(null)

    try {
      // Backend URL from environment variable or fallback to ngrok
      const BACKEND_URL = process.env.NEXT_PUBLIC_API_URL || 'https://ef8848b14210.ngrok-free.app'

      const response = await fetch(`${BACKEND_URL}/api/predict/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',  // Skip ngrok warning page
        },
        body: JSON.stringify({ url }),
      })

      if (!response.ok) {
        throw new Error('Gagal melakukan prediksi')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Terjadi kesalahan')
    } finally {
      setLoading(false)
    }
  }

  const getResultClass = (prediction: string) => {
    if (prediction === 'benign') return 'benign'
    if (prediction === 'phishing' || prediction === 'malware') return 'danger'
    return 'warning'
  }

  const getResultMessage = (prediction: string) => {
    const messages: Record<string, string> = {
      benign: '✓ URL Aman',
      phishing: '⚠ URL Phishing Terdeteksi!',
      malware: '⚠ URL Malware Terdeteksi!',
      defacement: '⚠ URL Defacement Terdeteksi!',
      defaceme: '⚠ URL Defacement Terdeteksi!',
    }
    return messages[prediction] || '⚠ URL Mencurigakan'
  }

  return (
    <div className="container">
      <div className="card">
        <h1>🔒 Phishing URL Detector</h1>
        <p className="subtitle">Deteksi URL berbahaya menggunakan analisis fitur lexical</p>
        <p className="model-info">Model: Random Forest Classifier (100 trees)</p>

        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Masukkan URL (contoh: https://example.com)"
              required
            />
            <button type="submit" disabled={loading}>
              {loading ? 'Menganalisis...' : 'Analisis'}
            </button>
          </div>
        </form>

        {error && <div className="error">{error}</div>}

        {result && (
          <div className="result">
            <div className="result-left">
              <div className="result-title">Hasil Analisis</div>

              <div className={`result-status ${getResultClass(result.prediction)}`}>
                {getResultMessage(result.prediction)}
              </div>

              <div className="result-info">
                <p><strong>URL:</strong> {result.url}</p>
                <p><strong>Klasifikasi:</strong> {result.prediction.toUpperCase()}</p>
                {result.confidence && (
                  <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(1)}%</p>
                )}
              </div>

              <div className="result-title" style={{ marginTop: '20px' }}>Fitur Lexical</div>
              <div className="feature-grid">
                <div className="feature-item">Panjang URL: {result.features.url_length}</div>
                <div className="feature-item">Jumlah Titik: {result.features.num_dots}</div>
                <div className="feature-item">Ada WWW: {result.features.has_www ? 'Ya' : 'Tidak'}</div>
                <div className="feature-item">HTTPS: {result.features.has_https ? 'Ya' : 'Tidak'}</div>
                <div className="feature-item">Jumlah Hyphen: {result.features.num_hyphens}</div>
                <div className="feature-item">Jumlah Slash: {result.features.num_slashes}</div>
                <div className="feature-item">Ada Angka: {result.features.has_numeric ? 'Ya' : 'Tidak'}</div>
              </div>
            </div>

            <div className="result-right">
              <div className="result-title">Probabilitas</div>
              {Object.entries(result.probabilities)
                .sort(([, a], [, b]) => b - a)
                .map(([cls, prob]) => (
                  <div key={cls} className="prob-bar">
                    <div className="prob-label">
                      <span>{cls}</span>
                      <span>{(prob * 100).toFixed(1)}%</span>
                    </div>
                    <div className="prob-progress">
                      <div className="prob-fill" style={{ width: `${prob * 100}%` }} />
                    </div>
                  </div>
                ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
