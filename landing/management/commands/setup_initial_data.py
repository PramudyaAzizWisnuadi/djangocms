from django.core.management.base import BaseCommand
from landing.models import LandingContent, Feature, ContactInfo

class Command(BaseCommand):
    help = 'Membuat data awal untuk landing page'

    def handle(self, *args, **options):
        # Hapus data lama jika ada
        LandingContent.objects.all().delete()
        ContactInfo.objects.all().delete()
        
        # Buat LandingContent
        landing = LandingContent.objects.create(
            title='Selamat Datang di Company',
            subtitle='Solusi Terbaik untuk Kebutuhan Digital Anda',
            description='Kami menyediakan layanan terbaik dengan teknologi terdepan untuk membantu mengembangkan bisnis Anda.'
        )
        
        # Buat Features dengan Font Awesome dan Emoji
        features_data = [
            {
                'title': 'Desain Modern',
                'description': 'Interface yang modern dan user-friendly',
                'icon': 'fas fa-palette'  # Font Awesome
            },
            {
                'title': 'Responsif',
                'description': 'Tampil sempurna di semua perangkat',
                'icon': 'fas fa-mobile-alt'  # Font Awesome
            },
            {
                'title': 'Cepat & Aman',
                'description': 'Performa tinggi dengan keamanan terjamin',
                'icon': '🚀'  # Emoji
            }
        ]
        
        for feature_data in features_data:
            Feature.objects.create(
                landing=landing,
                **feature_data
            )
        
        # Buat ContactInfo
        ContactInfo.objects.create(
            email='info@company.com',
            phone='+62 123 456 7890',
            address='Jl. Contoh No. 123, Jakarta, Indonesia'
        )
        
        self.stdout.write(
            self.style.SUCCESS('Data awal berhasil dibuat!')
        )
