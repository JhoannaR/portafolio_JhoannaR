from django .urls import path
from .views import render_posts, post_detail

app_name="blog"
#creo la variable para poder referenciar a todos los path. Es decir de blog visita a posts y de blog visita a post_detail

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),

]