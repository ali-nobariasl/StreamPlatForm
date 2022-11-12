from django.contrib import admin


from watchlist_app.models import StreamPlatform,WatchList,Review


admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(Review)

admin.site.site_header = "Im the best, eat my moz please!"

