from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm,UserAdminProfileForm,ProductCategoryEditForm

from mainapp.models import ProductCategory,Product



@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')

class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView,self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('adminapp:admin_users')
    form_class = UserAdminRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         # else:
#         #     print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#         # messages.error(request,print(form.errors))
#
#     context = {'form':form}
#     return render(request, 'adminapp/admin-users-create.html', context,print(form.errors))




class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_users')
    form_class = UserAdminProfileForm
    
    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        # context.update()
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, user_id):
#     user = User.objects.get(id =user_id)
#
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user)
#     # baskets = Basket.objects.filter(user=request.user)
#     context = {'form':form, 'user': user}
#     return render(request, 'adminapp/admin-users-update-delete.html',context)



class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_users')

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.is_active = False
       self.object.save()
       return HttpResponseRedirect(self.get_success_url())






# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_remove(request, user_id):
#     user = User.objects.get(id=user_id)
#     user.is_active = False
#     user.save()
#     # user.delete()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))

# пробная модель категорий
def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()

    context ={
        'title':title,
        'objects':categories_list
    }
    return render(request,'adminapp/admin-categories.html',context)

# class ProductCategory(ListView):
#     model = User
#     template_name = 'adminapp/admin-categories.html'
#
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super(ProductCategory,self).dispatch(request, *args, **kwargs)

def category_create(self, request, pk, *args, **kwargs):
    pass

@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk, *args, **kwargs):
    title = 'админка/редактирование/удаление',
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.metod == 'POST':
        form = ProductCategoryEditForm(data =request.POST, files =request.FILES, instance = category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
        else:
            pass

    context ={'form':form, 'category':category}
    return render(request,'adminapp/admin-categories.html', context)


def category_delete(self, request, pk, *args, **kwargs):
    pass



def products(request, pk, *args, **kwargs):
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category_pk=pk).order_by ('name')
    context ={
        'title':title,
        'category':category,
        'objects':products_list
    }
    return render(request,'adminapp/products.html', context)

def product_create(request, pk, *args, **kwargs):
    pass


def product_read (request, pk, *args, **kwargs):
    pass

def product_update(request, pk, *args, **kwargs):
    pass

def product_delete(request, pk, *args, **kwargs):
    pass