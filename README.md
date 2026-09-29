# 🎬 Movie Intelligence & Recommender Hub

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-analytics-recommender-by-elieser.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-TF--IDF%20&%20Cosine%20Similarity-FF007B?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![UI](https://img.shields.io/badge/UI-Glassmorphism-9D00FF)](https://streamlit.io/)

Aplikasi web interaktif berbasis **Data Analytics & Machine Learning** untuk mengevaluasi performa komersial film (anggaran, pendapatan, dan ROI) sekaligus menyajikan sistem rekomendasi film personal berbasis konten secara *real-time*.

---

## 🚀 Live Demo
Coba aplikasinya langsung di sini: **[Movie Intelligence & Recommender Hub App](https://movie-analytics-recommender-by-elieser.streamlit.app/)**

---

## 📊 Konteks Bisnis & Problem Statement
Dalam industri perfilman, memahami hubungan antara performa finansial sebuah produksi (*production budget* dan *box office revenue*) dengan preferensi penonton sangat penting bagi analis maupun pembuat keputusan. Namun, seringkali data finansial yang kompleks sulit disajikan secara intuitif bersamaan dengan sistem penelusuran film yang relevan.

**💡 Solusi:**
Menggabungkan **Analisis Bisnis & Finansial** dengan **Sistem Rekomendasi Machine Learning (Content-Based Filtering)** dalam satu platform terintegrasi. Aplikasi ini menggunakan pemrosesan teks *TF-IDF* dan *Cosine Similarity* untuk mencarikan film serupa, serta dilengkapi optimasi *on-the-fly computation* agar tetap ringan dan memenuhi batas ukuran *deployment cloud*.

---

## ✨ Fitur Utama
- **📈 Business & Financial Analysis:** Menganalisis anggaran produksi, pendapatan *box office*, rating penonton, serta perhitungan persentase ROI (*Return on Investment*) secara otomatis.
- **💡 Executive Summary & Status:** Menampilkan indikator status kesehatan finansial film (seperti *Box Office Hit*, *Break-Even*, atau *Underperformed*) menggunakan panel pemberitahuan khusus.
- **✨ AI-Powered Recommendations:** Menghasilkan rekomendasi film berdasarkan kemiripan konten (genre, pemeran, sutradara, dan ringkasan sinopsis/plot).
- **🎨 Modern UI & Glassmorphism:** Dibangun dengan antarmuka latar belakang gradasi dinamis, ornamen garis gelombang abstrak (*SVG waves*), dan kontainer bergaya *glassmorphism*.
- **⚡ Optimized MLOps Architecture:** Menggunakan komputasi matriks *on-the-fly* berukuran ringan yang dioptimalkan untuk performa server web yang cepat.

---

## 🛠 Teknologi yang Digunakan
- **Bahasa Pemrograman:** Python
- **Machine Learning & NLP:** Scikit-Learn (TF-IDF Vectorizer, Cosine Similarity)
- **Data Manipulation & Serialization:** Pandas, Joblib
- **Web Deployment & UI:** Streamlit, Custom HTML/CSS/SVG

---

## 💻 Cara Menjalankan Secara Lokal (Local Installation)

Jika Anda ingin menjalankan proyek ini di mesin lokal, ikuti langkah-langkah berikut:

1. **Clone repositori ini:**
   ```bash
   git clone [https://github.com/Elieser1945/movie-analytics-recommender.git](https://github.com/Elieser1945/movie-analytics-recommender.git)
   cd movie-analytics-recommender
   ```

2. **Buat Virtual Environment (Opsional namun direkomendasikan):**
   ```bash
   python -m venv venv
   # Untuk Windows:
   .\venv\Scripts\activate
   # Untuk Linux/Mac:
   source venv/bin/activate
   ```

3. **Instal dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit:**
   ```bash
   streamlit run app.py
   ```

---

## 🧑‍💻 Developed By
**Elieser Pasaribu**  
Data Analyst | Data Scientist | Machine Learning Enthusiast  

Terbuka untuk diskusi, masukan, dan peluang kolaborasi! Silakan hubungi saya melalui GitHub atau LinkedIn.
