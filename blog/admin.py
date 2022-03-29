from django.contrib import admin

from blog.models import Post

# Post modellediğimiz gönderilere ekleme,
#  düzenleme ya da silme işlemi yapmak için
#  Django admini kullanacağız.


#Admin sayfasında modelimizi görünür kılabilmek için,
#  modeli aşağıdaki gibi kaydetmemiz gerekiyor.
admin.site.register(Post)

# artik django adminde Post modeli görüecektir
#Giriş yapabilmek için, sitedeki her şey üzerinde kontrolü 
# olan superuser - bir kullanıcı hesabı oluşturmanız gerekiyor.
#  Komut satırına geri giderek python manage.py createsuperuser
#  yazın ve enter'a basın.
