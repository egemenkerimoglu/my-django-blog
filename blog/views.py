from django.shortcuts import render

# Create your views here.


"""
Burada post_list isimli bir fonksiyon (def) yarattık, 
bu fonksiyon girdi olarak request (isteği) alıp,
blog/post_list.html template'ini işleyecek olan render
fonksiyonunu döndürüyor.
"""
def post_list(request):
    return render(request,'blog/post_list.html',{})