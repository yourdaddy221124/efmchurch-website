from django.shortcuts import render, redirect
from .models import Event, Media, Update, PrayerRequest

def home(request):
    events = Event.objects.all().order_by('-date')[:5]
    updates = Update.objects.all().order_by('-date_posted')[:5]
    media_items = Media.objects.all().order_by('-uploaded_at')[:5]
    return render(request, 'core/index.html', {
        'events': events,
        'updates': updates,
        'media_items': media_items
    })

def lumen_spirit(request):
    return render(request, 'core/lumen_spirit.html')

def gallery(request):
    media_items = Media.objects.all().order_by('-uploaded_at')
    return render(request, 'core/gallery.html', {'media_items': media_items})

def prayer_requests(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Anonymous')
        if not name.strip(): name = 'Anonymous'
        category = request.POST.get('category', 'Other')
        prayer_content = request.POST.get('request', '')
        if prayer_content.strip():
            PrayerRequest.objects.create(name=name, category=category, request=prayer_content)
        return redirect('prayer_requests')
    
    requests = PrayerRequest.objects.all().order_by('-created_at')
    return render(request, 'core/prayer_requests.html', {'requests': requests})

def give(request):
    return render(request, 'core/give.html')

def events(request):
    events_list = Event.objects.all().order_by('-date')
    return render(request, 'core/events.html', {'events_list': events_list})
