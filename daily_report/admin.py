from django.contrib import admin
from .models import sliders, main_trending_headline, comment, sub_trending_col_1, sub_trending_col_2, \
    sub_trending_col_3, comment_col1, comment_col2, comment_col3, culture_main, culture_main_support, culture_col11, \
    culture_col12, comment_cul_col1, culture_col2, culture_col3, comment_cul_col3, business_col1, comment_bus_col1, \
    business_main, business_main_support, business_sub_trending, business_post_1, comment_bus_col21, new_messages, \
    lifestyle_main, lifestyle_main_support, lifestyle_col1, comment_lifestyle_col1, lifestyle_col_2, \
    comment_lifestyle_col2, lifestyle_col_3, comment_lifestyle_col3, lifestyle_col_4, comment_lifestyle_col4

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

# culture section
admin.site.register(culture_main)
admin.site.register(culture_main_support)
admin.site.register(culture_col11)
admin.site.register(culture_col12)
admin.site.register(comment_cul_col1)
admin.site.register(culture_col2)
admin.site.register(culture_col3)
admin.site.register(comment_cul_col3)

# end culture section

# start business section
admin.site.register(business_col1)
admin.site.register(comment_bus_col1)
admin.site.register(business_main)
admin.site.register(business_main_support)
admin.site.register(business_sub_trending)
admin.site.register(business_post_1)
admin.site.register(comment_bus_col21)

# messages
admin.site.register(new_messages)

# lifestyle
admin.site.register(lifestyle_main)
admin.site.register(lifestyle_main_support)
admin.site.register(lifestyle_col1)
admin.site.register(comment_lifestyle_col1)
admin.site.register(lifestyle_col_2)
admin.site.register(comment_lifestyle_col2)
admin.site.register(lifestyle_col_3)
admin.site.register(comment_lifestyle_col3)
admin.site.register(lifestyle_col_4)
admin.site.register(comment_lifestyle_col4)