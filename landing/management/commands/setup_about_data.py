from django.core.management.base import BaseCommand
from landing.models import AboutContent, MissionItem, TeamMember, CompanyValue

class Command(BaseCommand):
    help = 'Setup initial data for About page'

    def handle(self, *args, **options):
        # Create About Content
        about_content, created = AboutContent.objects.get_or_create(
            defaults={
                'title': 'Tentang Kami',
                'description': 'Kami adalah tim yang berpengalaman dalam mengembangkan solusi digital inovatif untuk membantu bisnis berkembang di era digital.',
                'vision_title': 'Visi Kami',
                'vision_description': 'Menjadi perusahaan teknologi terdepan yang memberikan solusi inovatif untuk mengoptimalkan pertumbuhan bisnis digital di Indonesia.\n\nKami berkomitmen untuk terus mengembangkan teknologi yang mudah digunakan, efisien, dan memberikan dampak positif bagi perkembangan bisnis klien kami.',
                'mission_title': 'Misi Kami',
                'team_section_title': 'Tim Kami',
                'team_section_description': 'Bertemu dengan profesional berpengalaman yang siap membantu mewujudkan visi digital Anda',
                'values_section_title': 'Nilai-Nilai Kami',
                'values_section_description': 'Prinsip yang memandu setiap langkah kami'
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('About content created successfully'))
        else:
            self.stdout.write(self.style.WARNING('About content already exists'))

        # Create Mission Items
        mission_items = [
            'Memberikan layanan berkualitas tinggi dengan teknologi terdepan',
            'Membangun hubungan jangka panjang dengan klien',
            'Mengembangkan solusi yang mudah digunakan dan efektif',
            'Mendukung transformasi digital UMKM di Indonesia',
            'Menciptakan inovasi yang memberikan value bagi masyarakat'
        ]

        for i, item_text in enumerate(mission_items):
            mission_item, created = MissionItem.objects.get_or_create(
                about=about_content,
                text=item_text,
                defaults={'order': i + 1}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Mission item created: {item_text}'))

        # Create Team Members
        team_members = [
            {
                'name': 'John Doe',
                'position': 'CEO & Founder',
                'description': 'Pengalaman 10+ tahun di bidang teknologi dan pengembangan bisnis digital. Memimpin visi strategis perusahaan.',
                'email': 'john@company.com',
                'linkedin_url': 'https://linkedin.com/in/johndoe',
                'order': 1
            },
            {
                'name': 'Jane Smith',
                'position': 'CTO',
                'description': 'Expert dalam pengembangan web dan mobile dengan spesialisasi dalam arsitektur sistem yang scalable.',
                'email': 'jane@company.com',
                'linkedin_url': 'https://linkedin.com/in/janesmith',
                'order': 2
            },
            {
                'name': 'Mike Johnson',
                'position': 'Lead Designer',
                'description': 'Spesialis UI/UX dengan portofolio internasional. Menciptakan pengalaman pengguna yang memukau.',
                'email': 'mike@company.com',
                'linkedin_url': 'https://linkedin.com/in/mikejohnson',
                'order': 3
            },
            {
                'name': 'Sarah Wilson',
                'position': 'Marketing Director',
                'description': 'Ahli strategi pemasaran digital dengan track record sukses dalam brand development dan growth hacking.',
                'email': 'sarah@company.com',
                'linkedin_url': 'https://linkedin.com/in/sarahwilson',
                'order': 4
            }
        ]

        for member_data in team_members:
            team_member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Team member created: {member_data["name"]}'))

        # Create Company Values
        company_values = [
            {
                'title': 'Inovasi',
                'description': 'Selalu mencari cara baru dan kreatif untuk memecahkan masalah dengan pendekatan yang out-of-the-box.',
                'icon': 'fas fa-lightbulb',
                'order': 1
            },
            {
                'title': 'Integritas',
                'description': 'Berkomitmen pada transparansi dan kejujuran dalam setiap interaksi dengan klien dan partner bisnis.',
                'icon': 'fas fa-handshake',
                'order': 2
            },
            {
                'title': 'Keunggulan',
                'description': 'Berusaha memberikan hasil terbaik dalam setiap proyek dengan standar kualitas tinggi.',
                'icon': 'fas fa-trophy',
                'order': 3
            },
            {
                'title': 'Kolaborasi',
                'description': 'Membangun kerjasama yang solid dengan tim internal dan eksternal untuk mencapai tujuan bersama.',
                'icon': 'fas fa-users',
                'order': 4
            },
            {
                'title': 'Adaptabilitas',
                'description': 'Mampu beradaptasi dengan perubahan teknologi dan tren pasar yang berkembang pesat.',
                'icon': 'fas fa-sync-alt',
                'order': 5
            },
            {
                'title': 'Fokus Customer',
                'description': 'Mengutamakan kepuasan dan kebutuhan customer dalam setiap pengambilan keputusan bisnis.',
                'icon': 'fas fa-heart',
                'order': 6
            }
        ]

        for value_data in company_values:
            company_value, created = CompanyValue.objects.get_or_create(
                title=value_data['title'],
                defaults=value_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Company value created: {value_data["title"]}'))

        self.stdout.write(self.style.SUCCESS('\nAbout page data setup completed successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now manage all content through Django Admin at /admin/'))
