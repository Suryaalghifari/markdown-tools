# Markdown Tools

Markdown Tools adalah tool sederhana berbasis Python untuk mengonversi dokumen dari folder `docs/` menjadi file Markdown di folder `md/`.

Tool ini menggunakan Microsoft MarkItDown.

## Struktur Folder

```text
markdown-tools/
├── docs/
│   └── taruh-file-di-sini.pdf
├── md/
│   └── hasil-convert-akan-masuk-di-sini.md
├── convert.py
├── requirements.txt
└── README.md
```

## Syarat Instalasi

Pastikan laptop sudah memiliki:

* Python 3
* pip
* Git

Cek Python:

```bash
python3 --version
```

Cek pip:

```bash
pip --version
```

## Cara Instalasi

Clone repository:

```bash
git clone git@github.com:Suryaalghifari/markdown-tools.git
cd markdown-tools
```

Buat virtual environment:

```bash
python3 -m venv .venv
```

Aktifkan virtual environment.

Untuk Linux/macOS bash atau zsh:

```bash
source .venv/bin/activate
```

Untuk fish shell:

```fish
source .venv/bin/activate.fish
```

Untuk Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependency:

```bash
pip install -r requirements.txt
```

## Cara Menggunakan

Masukkan file yang ingin dikonversi ke folder:

```text
docs/
```

Contoh:

```text
docs/laporan.pdf
docs/dokumen.docx
docs/presentasi.pptx
```

Jalankan program:

```bash
python convert.py
```

Pilih menu:

```text
1. Lihat file di docs/
2. Convert satu file
3. Convert semua file
4. Keluar
```

Hasil konversi akan masuk ke folder:

```text
md/
```

Contoh:

```text
md/laporan.md
md/dokumen.md
md/presentasi.md
```

## Catatan

Hasil Markdown dari PDF mungkin belum selalu rapi, terutama untuk tabel, gambar, header/footer, caption, dan rumus. Setelah konversi, file Markdown sebaiknya tetap diperiksa dan dirapikan kembali.
