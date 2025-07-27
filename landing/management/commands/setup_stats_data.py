from django.core.management.base import BaseCommand
from landing.models import StatItem

class Command(BaseCommand):
    help = 'Setup initial statistics data for home page'

    def handle(self, *args, **options):
        # Create default stats
        stats_data = [
            {
                'number': '100+',
                'label': 'Proyek Selesai',
                'order': 1
            },
            {
                'number': '50+',
                'label': 'Klien Puas',
                'order': 2
            },
            {
                'number': '5+',
                'label': 'Tahun Pengalaman',
                'order': 3
            },
            {
                'number': '24/7',
                'label': 'Dukungan',
                'order': 4
            },
            {
                'number': '99%',
                'label': 'Tingkat Kepuasan',
                'order': 5
            },
            {
                'number': '15+',
                'label': 'Tim Ahli',
                'order': 6
            }
        ]

        for stat_data in stats_data:
            stat_item, created = StatItem.objects.get_or_create(
                number=stat_data['number'],
                label=stat_data['label'],
                defaults={
                    'order': stat_data['order'],
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Stat created: {stat_data["number"]} - {stat_data["label"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Stat already exists: {stat_data["number"]} - {stat_data["label"]}'))

        self.stdout.write(self.style.SUCCESS('\nStatistics data setup completed successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now manage statistics through Django Admin at /admin/'))
        self.stdout.write(self.style.SUCCESS('Note: Only the first 4 stats will be displayed in the current layout.'))
