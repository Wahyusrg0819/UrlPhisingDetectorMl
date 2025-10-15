import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Phishing URL Detector',
  description: 'Deteksi URL Phishing menggunakan Machine Learning',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="id">
      <body>{children}</body>
    </html>
  )
}
