from django.db import models

class LandingContent(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Feature(models.Model):
    landing = models.ForeignKey(LandingContent, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    icon = models.CharField(
        max_length=50, 
        help_text='Font Awesome: "fas fa-laptop-code" atau Emoji: "🎨"'
    )

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class AboutContent(models.Model):
    title = models.CharField(max_length=100, default="Tentang Kami")
    description = models.TextField()
    vision_title = models.CharField(max_length=100, default="Visi Kami")
    vision_description = models.TextField()
    mission_title = models.CharField(max_length=100, default="Misi Kami")
    team_section_title = models.CharField(max_length=100, default="Tim Kami")
    team_section_description = models.TextField()
    values_section_title = models.CharField(max_length=100, default="Nilai-Nilai Kami")
    values_section_description = models.TextField()

    class Meta:
        verbose_name = "About Content"
        verbose_name_plural = "About Content"

    def __str__(self):
        return self.title

class MissionItem(models.Model):
    about = models.ForeignKey(AboutContent, related_name='mission_items', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.position}"

class CompanyValue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(
        max_length=50, 
        help_text='Font Awesome: "fas fa-lightbulb" atau Emoji: "💡"'
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class StatItem(models.Model):
    number = models.CharField(max_length=20, help_text='Contoh: "100+", "24/7", "5+"')
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Statistik"
        verbose_name_plural = "Statistik"

    def __str__(self):
        return f"{self.number} - {self.label}"
