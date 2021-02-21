from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    data = Article.objects.all()
    return render(request, "cm/index.html", context={"data": data})


"""
[
        {
            "title": "Future of EVs",
            "text": " this article talks about the future of electric vehicles",
        },
        {
            "title": "Climate change: What is unexpected",
            "text": " this article talks about the future of electric vehicles",
        },
        {
            "title": "Climate change: What is unexpected",
            "text": " this article talks about the future of electric vehicles",
        },
        {
            "title": "Climate change: What is unexpected",
            "text": " this article talks about the future of electric vehicles",
        },
        {
            "title": "Climate change: What is unexpected",
            "text": " this article talks about the future of electric vehicles",
        },
        {
            "title": "Climate change: What is unexpected",
            "text": " this article talks about the future of electric vehicles",
        },
        {
            "title": "Climate change: What is unexpected",
            "text": " this article talks about the future of electric vehicles",
        },
        {
            "title": "Climate change: What is unexpected",
            "text": " this article talks about the future of electric vehicles",
        },
    ]
"""