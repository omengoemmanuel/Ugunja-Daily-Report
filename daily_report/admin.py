from django.contrib import admin
from .models import sliders, main_trending_headline, comment, sub_trending_col_1, sub_trending_col_2, \
    sub_trending_col_3, comment_col1, comment_col2, comment_col3, culture_main, culture_main_support, culture_col11, \
    culture_col12, comment_cul_col1, culture_col2

# Register your models here.
admin.site.register(sliders)
admin.site.register(main_trending_headline)
admin.site.register(comment)
admin.site.register(sub_trending_col_1)
admin.site.register(sub_trending_col_2)
admin.site.register(sub_trending_col_3)
admin.site.register(comment_col1)
admin.site.register(comment_col2)
admin.site.register(comment_col3)
admin.site.register(culture_main)
admin.site.register(culture_main_support)
admin.site.register(culture_col11)
admin.site.register(culture_col12)
admin.site.register(comment_cul_col1)
admin.site.register(culture_col2)
