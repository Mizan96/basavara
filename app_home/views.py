from django.shortcuts import render, get_object_or_404, redirect

from app_home.models import ToLetModel, AreaModel, ToletCommentModel, ToLetModel, HomeOwnerMessageModel

from django.contrib.auth.decorators import login_required

from app_home.forms import EditProfileForm, PostToLetForm

from django.db.models import Q

# Create your views here.

"""
    this is home page
"""


def index(request):
    tolets = ToLetModel.objects.filter(open=True)
    form = PostToLetForm()
    if request.method == 'POST':
        city = request.POST.get('city')
        area = request.POST.get('area')
        # tolets = ToLetModel.objects.filter(
        #     Q(open=True) & (Q(city=city) | Q(area=area))
        # )
        tolets = ToLetModel.objects.filter(open=True, city=city, area=area)
    context = {
        'tolets': tolets,
        'form': form
    }
    return render(request, 'index.html', context)


"""
    this is detail page
"""


def detail(request, id):
    obj = get_object_or_404(ToLetModel, pk=id)
    comments = ToletCommentModel.objects.filter(tolet=obj)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        message = request.POST.get('message')
        if comment:
            ToletCommentModel.objects.create(
                tolet = obj,
                comment = comment
            )
        if message:
            HomeOwnerMessageModel.objects.create(
                user = obj.user,
                message = message
            )
    context = {
        'obj': obj,
        'comments': comments
    }
    return render(request, 'detail.html', context)


"""
    this is for posting to-let
"""


@login_required
def postTolet(request):
    context = {
        'form': PostToLetForm
    }
    if request.method == 'POST':
        form = PostToLetForm(request.POST, request.FILES)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            context['ok']='ok'
        else:
            context = {
                'form': form
            }
    return render(request, 'postTolet.html', context)


"""
this is for adding to-let
"""


@login_required
def postToletEdit(request, id):
    obj = get_object_or_404(ToLetModel, id=id)
    form = PostToLetForm(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'postTolet.html', context)


@login_required
def deleteTolet(request, id):
    obj = get_object_or_404(ToLetModel, id=id)
    obj.delete()
    return redirect('profile')

@login_required
def toletOpen(request, id):
    obj = get_object_or_404(ToLetModel, id=id)
    if obj.open == True:
        obj.open = False
        obj.save()
    else:
        obj.open = True
        obj.save()
    print(obj.open)
    return redirect('profile')

"""
This is for profile view
"""


@login_required
def profile(request):
    form = EditProfileForm(request.POST or None, instance=request.user)
    tolets = ToLetModel.objects.filter(user=request.user)
    messages = HomeOwnerMessageModel.objects.filter(user=request.user)
    context = {
        'form': form,
        'tolets': tolets,
        'messages': messages
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'profile.html', context)


# s
