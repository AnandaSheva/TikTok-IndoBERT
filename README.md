# TikTok IndoBERT Sentiment Analysis

Proyek ini adalah skripsi analisis sentimen komentar TikTok berbahasa Indonesia. Tujuan utama adalah membuat pipeline dari scraping, preprocessing, hingga fine-tuning model IndoBERT untuk klasifikasi sentimen.

## Ringkasan
- Data utama berasal dari komentar TikTok berbahasa Indonesia.
- Preprocessing mencakup normalisasi teks, stopword removal, dan tokenisasi.
- Model utama yang digunakan adalah `indobenchmark/indobert-base-p1` untuk fine-tuning klasifikasi sentimen.
- Evaluasi dilakukan pada data yang sudah dilabeli dengan sentimen `Positif`, `Negatif`, dan `Netral`.

## Struktur Project
- `dataset/` - berisi dataset mentah dan versi lama.
- `dataset_balanced.csv` - dataset yang sudah diseimbangkan untuk pelatihan.
- `Hasil_Labelling_Data_3class.csv` - hasil pelabelan sentimen 3 kelas.
- `lexicon_label.csv` - kamus/lexicon untuk analisis sentimen.
- `img/` - folder gambar yang di-ignore di Git.
- `results/` - folder hasil model dan checkpoint yang di-ignore di Git.
- `main.py` - contoh kode Python sederhana (algoritma dasar) yang tidak terkait langsung dengan pipeline NLP utama.
- Notebook utama:
  - `scraping.ipynb` - scraping data TikTok.
  - `normalisasi.ipynb` - normalisasi dan preprocessing teks.
  - `prepro-new.ipynb` - eksperimen preprocessing lanjutan.
  - `train.ipynb` - pelatihan model dan evaluasi.
  - `notebook.ipynb` - pipeline end-to-end termasuk visualisasi dan IndoBERT fine-tuning.
  - `wordcloud&ngram.ipynb` - analisis frekuensi kata dan n-gram.

## Instalasi
1. Buat virtual environment Python:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install paket yang diperlukan. Contoh:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn transformers torch datasets openpyxl
   ```

> Catatan: `transformers` dan `torch` diperlukan untuk fine-tuning IndoBERT.

## Cara Jalankan
1. Aktifkan environment:
   ```bash
   .venv\Scripts\activate
   ```
2. Jalankan notebook sesuai alur:
   - `scraping.ipynb` untuk ambil data TikTok.
   - `normalisasi.ipynb` untuk preprocessing awal.
   - `prepro-new.ipynb` untuk eksperimen preprocessing dan analisis teks.
   - `train.ipynb` untuk melatih model klasifikasi.
   - `notebook.ipynb` untuk pipeline lengkap dan visualisasi.

3. Jika ingin langsung melatih model IndoBERT, buka dan jalankan sel di notebook yang berisi bagian `IndoBERT FINETUNING`.

## Catatan Git
File besar dan model weights sengaja di-ignore agar repo tetap ringan. File yang di-ignore meliputi:
- folder virtual environment: `.venv/`, `venv/`, `ENV/`
- folder `img/`
- folder `result/`
- file model dan dataset besar: `*.bin`, `*.pt`, `*.safetensors`, `*.pkl`, `*.json`

## Hasil dan Evaluasi
- Model checkpoint berada di folder `results/checkpoint-*` (tidak di-push karena di-ignore).
- Dataset yang sudah disiapkan untuk pelatihan ada di `dataset_balanced.csv` dan `Hasil_Labelling_Data_3class.csv`.

## Keterangan
Proyek ini fokus pada analisis sentimen komentar TikTok Indonesia dengan pendekatan NLP berbasis IndoBERT. Seluruh proses memanfaatkan notebook untuk eksperimen, visualisasi, dan pengolahan data.

