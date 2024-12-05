from django.contrib import admin
from .models import sliders, main_trending_headline, comment, sub_trending_col_1

# Register your models here.
admin.site.register(sliders)
admin.site.register(main_trending_headline)
admin.site.register(comment)
admin.site.register(sub_trending_col_1)
