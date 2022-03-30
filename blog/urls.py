from unicodedata import name
from django.urls import path
from . import views

"""
Gördüğünüz üzere, ana URL'e post_list adında bir view atıyoruz.
 Django URL resolver ful URL'in başındaki domain adını 
 (yani, http://127.0.0.1:8000 /) göz ardı eder, böylece bu URL
  kalıbı (pattern) boş bir string ile eşleşecek. Bu kalıp, 
  Django'ya eğer siteye biri 'http://127.0.0.1:8000/' adresinden 
  gelirse gitmesi gereken yerin views.post_list olduğunu söylüyor.

Son kısım name='post_list', görünümü (view) tanımlamak için kullanılan
URL'in adıdır. Bu view'un adı ile aynı olabilir ama tamamen farklı bir
 şey de olabilir. Bundan sonra projede isimlendirilmiş URL'leri 
 kullanıyor olacağız, bu yüzden uygulamadaki her URL'i isimlendirmek 
 önemli. Aynı zamanda URL isimlerini eşsiz ve kolay hatırlanabilir 
 şekilde seçmeliyiz.
"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]