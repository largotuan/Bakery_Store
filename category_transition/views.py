from django.shortcuts import render, get_object_or_404
from category_transition.models import Category, Transition


# Create your views here.
def detail(request):
    category = get_object_or_404(Category)
    context = {
        'category': Category,
        'detail': Category.objects.all()
    }
    return render(request, 'category/', context)

