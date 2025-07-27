from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def render_icon(icon_text, size="1rem"):
    """
    Filter untuk merender icon Font Awesome atau emoji
    Usage: {{ feature.icon|render_icon:"3rem" }}
    """
    if not icon_text:
        return ""
    
    # Cek apakah ini Font Awesome icon (dimulai dengan fas, fab, far, fal, fad, dll)
    fa_prefixes = ['fas', 'fab', 'far', 'fal', 'fad', 'fass', 'fasr', 'fasl']
    
    # Split untuk mengecek prefix
    icon_parts = str(icon_text).strip().split()
    
    if len(icon_parts) >= 2 and icon_parts[0] in fa_prefixes:
        # Ini adalah Font Awesome icon
        icon_class = " ".join(icon_parts)
        return mark_safe(f'<i class="{icon_class}" style="font-size: {size};"></i>')
    else:
        # Ini adalah emoji atau text biasa
        return mark_safe(f'<span style="font-size: {size};">{icon_text}</span>')

@register.filter
def is_fontawesome(icon_text):
    """
    Cek apakah icon adalah Font Awesome
    """
    if not icon_text:
        return False
    
    fa_prefixes = ['fas', 'fab', 'far', 'fal', 'fad', 'fass', 'fasr', 'fasl']
    icon_parts = str(icon_text).strip().split()
    
    return len(icon_parts) >= 2 and icon_parts[0] in fa_prefixes
