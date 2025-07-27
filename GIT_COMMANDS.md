# Git Commands untuk Share Project

## Inisialisasi Git Repository (jika belum ada)

```bash
git init
git add .
git commit -m "Initial commit: Django Landing Page with Admin Panel"
```

## Connect ke GitHub Repository

```bash
# Ganti dengan URL repository Anda
git remote add origin https://github.com/username/djangocms.git
git branch -M main
git push -u origin main
```

## Workflow Development

```bash
# Sebelum mulai development
git pull origin main

# Setelah selesai development
git add .
git commit -m "Add: feature description"
git push origin main
```

## Branching Strategy

```bash
# Buat feature branch
git checkout -b feature/new-feature
git add .
git commit -m "Add: new feature"
git push origin feature/new-feature

# Merge ke main branch
git checkout main
git merge feature/new-feature
git push origin main
```

## Clone Repository (untuk user lain)

```bash
git clone https://github.com/username/djangocms.git
cd djangocms

# Windows
setup.bat

# Linux/Mac
chmod +x setup.sh
./setup.sh
```
