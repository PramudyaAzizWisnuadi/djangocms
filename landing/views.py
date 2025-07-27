from django.shortcuts import render
from .models import LandingContent, Feature, ContactInfo, AboutContent, TeamMember, CompanyValue, StatItem

def home(request):
    landing = LandingContent.objects.first()
    features = Feature.objects.filter(landing=landing) if landing else []
    stats = StatItem.objects.filter(is_active=True).order_by('order')
    
    context = {
        'title': landing.title if landing else 'Selamat Datang',
        'subtitle': landing.subtitle if landing else 'Solusi Terbaik untuk Kebutuhan Digital Anda',
        'description': landing.description if landing else 'Kami menyediakan layanan terbaik dengan teknologi terdepan untuk membantu mengembangkan bisnis Anda.',
        'features': features,
        'stats': stats,
    }
    return render(request, 'landing/home.html', context)

def about(request):
    about_content = AboutContent.objects.first()
    team_members = TeamMember.objects.filter(is_active=True).order_by('order')
    company_values = CompanyValue.objects.filter(is_active=True).order_by('order')
    
    context = {
        'title': about_content.title if about_content else 'Tentang Kami',
        'description': about_content.description if about_content else 'Kami adalah tim yang berpengalaman dalam mengembangkan solusi digital inovatif.',
        'vision_title': about_content.vision_title if about_content else 'Visi Kami',
        'vision_description': about_content.vision_description if about_content else 'Menjadi perusahaan teknologi terdepan.',
        'mission_title': about_content.mission_title if about_content else 'Misi Kami',
        'mission_items': about_content.mission_items.all() if about_content else [],
        'team_section_title': about_content.team_section_title if about_content else 'Tim Kami',
        'team_section_description': about_content.team_section_description if about_content else 'Bertemu dengan profesional berpengalaman yang siap membantu mewujudkan visi digital Anda',
        'team_members': team_members,
        'values_section_title': about_content.values_section_title if about_content else 'Nilai-Nilai Kami',
        'values_section_description': about_content.values_section_description if about_content else 'Prinsip yang memandu setiap langkah kami',
        'company_values': company_values,
    }
    return render(request, 'landing/about.html', context)

def contact(request):
    contact_info = ContactInfo.objects.first()
    context = {
        'title': 'Hubungi Kami',
        'description': 'Jangan ragu untuk menghubungi kami untuk konsultasi gratis.',
        'contact_info': {
            'email': contact_info.email if contact_info else 'info@company.com',
            'phone': contact_info.phone if contact_info else '+62 123 456 7890',
            'address': contact_info.address if contact_info else 'Jl. Contoh No. 123, Jakarta, Indonesia'
        }
    }
    return render(request, 'landing/contact.html', context)
