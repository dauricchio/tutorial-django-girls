from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post#Il punto dopo il from significa directory attuale oppure applicazione attuale. 

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})#aggiungere cose che il template possa utilizzare. 

def post_detail(request, pk, a):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_item.html', {'post' : post})    