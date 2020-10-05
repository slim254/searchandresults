

from django.db.models import Q
from django.http import request
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import Testform
from .models import test

#createview for form
class PostCreateView(CreateView):
    form_class = Testform
    model = test
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        return super().form_valid(form)


class PostListView(ListView):
    model = test
    template_name = 'main/posts.html'  # app->model->viewtype->.html
#passing context to listview
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['post'] = test.objects.all()

        return context
def SearchResultsView(request):  # search result


    posts = test.objects.all()

    query = request.GET.get('q')
    queries=query.split(" ")
    for q in queries:
        posts = test.objects.filter(
            Q(username__icontains=q) |
            Q(userid__icontains=q)

        )


    context = {
        'posts': posts,

    }

    return render(request, 'main/search.html', context)