from django.contrib import admin

from app_home.models import ToLetModel, CityModel, AreaModel, ToletCommentModel, HomeOwnerMessageModel

# Register your models here.

admin.site.register(ToLetModel)
admin.site.register(CityModel)
admin.site.register(AreaModel)
admin.site.register(ToletCommentModel)
admin.site.register(HomeOwnerMessageModel)