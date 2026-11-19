from django.shortcuts import render
from .models import Topic

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Display all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Display a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    context = {'topic': topic}
    return render(request, 'learning_logs/topic.html', context)