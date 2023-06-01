from django.shortcuts import render, get_object_or_404
# get_object_or_404 sirve para que si no encuentra un objeto en la ruta dirá no se encontró
from .models import Post

def render_posts(request):
    posts= Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #le paso el modelo: Post y el identificador de la publicación: primary key
    return render(request, 'post_detail.html', {'post':post})