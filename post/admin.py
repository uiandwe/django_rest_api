from django.contrib import admin

# Register your models here.


from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "created_at"]
	list_display_links = ["created_at"]
	list_editable = ["title"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)