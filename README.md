# Django Landing Page

Sebuah website landing page yang dibangun dengan Django, dilengkapi dengan admin panel untuk mengelola konten secara dinamis.

## 🌟 Fitur

- **Landing Page Modern**: Hero section, features, statistics, dan call-to-action
- **Halaman About**: Informasi tentang perusahaan, tim, visi, misi, dan nilai-nilai
- **Halaman Contact**: Informasi kontak perusahaan
- **Admin Panel**: Kelola semua konten melalui Django Admin
- **Responsive Design**: Tampilan optimal di desktop dan mobile
- **Font Awesome Icons**: Integration dengan Font Awesome untuk icons
- **Bootstrap 5**: Framework CSS modern untuk styling

## 📋 Requirements

- Python 3.8+
- Django 5.2.4
- Bootstrap 5.3.0
- Font Awesome 6.0.0

## 🚀 Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/username/djangocms.git
   cd djangocms
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan migrasi database**
   ```bash
   python manage.py migrate
   ```

5. **Buat superuser untuk admin**
   ```bash
   python manage.py createsuperuser
   ```

6. **Setup data awal (opsional)**
   ```bash
   python manage.py setup_initial_data
   python manage.py setup_about_data
   python manage.py setup_stats_data
   ```

7. **Jalankan development server**
   ```bash
   python manage.py runserver
   ```

8. **Akses website**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Struktur Project

```
djangotutorial/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── landing/
│   ├── models.py          # Database models
│   ├── views.py           # Views logic
│   ├── admin.py           # Admin configuration
│   ├── urls.py            # URL patterns
│   ├── templatetags/      # Custom template filters
│   └── management/        # Management commands
├── templates/
│   ├── base.html          # Base template
│   └── landing/           # Landing app templates
├── static/
│   └── css/
│       └── style.css      # Custom styling
├── requirements.txt       # Python dependencies
└── manage.py
```

## 🎛️ Admin Panel Features

### Landing Content
- **Home Page**: Title, subtitle, description
- **Features**: Icon, title, description dengan ordering
- **Statistics**: Number, label dengan ordering

### About Page
- **About Content**: Visi, misi, deskripsi tim dan values
- **Mission Items**: Daftar misi yang bisa diatur
- **Team Members**: Nama, posisi, deskripsi, social links
- **Company Values**: Title, description, icon

### Contact Info
- **Contact Information**: Email, phone, address

## 🎨 Customization

### CSS Variables
Ubah tema warna di `static/css/style.css`:
```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --accent-color: #ec4899;
    --text-color: #1f2937;
    --text-muted: #6b7280;
    --bg-light: #f8fafc;
    --border-color: #e2e8f0;
    --dark-color: #1e293b;
}
```

### Font Awesome Icons
Gunakan Font Awesome class di admin panel:
- `fas fa-laptop-code` untuk ikon coding
- `fas fa-mobile-alt` untuk ikon mobile
- `fas fa-chart-line` untuk ikon analytics

## 🚢 Deployment

### Heroku
1. Install Heroku CLI
2. Tambahkan `Procfile`:
   ```
   web: gunicorn mysite.wsgi
   ```
3. Update `requirements.txt`:
   ```
   gunicorn==21.2.0
   ```
4. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Production Settings
Untuk production, update `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## 📝 Management Commands

- `setup_initial_data`: Setup data awal untuk landing page
- `setup_about_data`: Setup data awal untuk halaman about
- `setup_stats_data`: Setup data awal untuk statistik

## 🤝 Contributing

1. Fork repository
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

## 📄 License

Project ini menggunakan MIT License. Lihat file `LICENSE` untuk detail lengkap.

## 📞 Support

Jika ada pertanyaan atau masalah:
- Buka issue di GitHub
- Email: your-email@example.com

---

**Happy Coding! 🚀**
