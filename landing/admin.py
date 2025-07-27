from django.contrib import admin
from .models import (
    LandingContent, Feature, ContactInfo, 
    AboutContent, MissionItem, TeamMember, CompanyValue, StatItem
)

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

class MissionItemInline(admin.TabularInline):
    model = MissionItem
    extra = 1
    fields = ('text', 'order')

@admin.register(LandingContent)
class LandingContentAdmin(admin.ModelAdmin):
    inlines = [FeatureInline]
    list_display = ('title', 'subtitle')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address')

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    inlines = [MissionItemInline]
    list_display = ('title', 'vision_title', 'mission_title')
    fieldsets = (
        ('Header Section', {
            'fields': ('title', 'description')
        }),
        ('Vision Section', {
            'fields': ('vision_title', 'vision_description')
        }),
        ('Mission Section', {
            'fields': ('mission_title',)
        }),
        ('Team Section', {
            'fields': ('team_section_title', 'team_section_description')
        }),
        ('Values Section', {
            'fields': ('values_section_title', 'values_section_description')
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order', 'is_active')
    list_filter = ('is_active', 'position')
    search_fields = ('name', 'position')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'description')
        }),
        ('Social Links', {
            'fields': ('email', 'linkedin_url', 'twitter_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('order', 'is_active')
    ordering = ('order',)

@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ('number', 'label', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('label', 'number')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
    fieldsets = (
        ('Content', {
            'fields': ('number', 'label')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )
