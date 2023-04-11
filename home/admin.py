from django.contrib import admin
from django.utils.html import format_html
from home.models import About, AnnualReport, Archive, Article, Contact, KeyAchievement, Mission, News, Course, Events, Facility, ImageCategory, ImageGallery, MessageFromDirector, OurPartner, OurPartnerDatas, Outcome, Program, SocialAccount, Team, ThreeZero, Slider, Testomonials, Video

admin.site.site_header = 'NLR Nepal'
admin.site.site_title = 'NGO Dashboard'

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag', 'is_active',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    list_editable = ('is_active',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(Slider, SliderAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(About, AboutAdmin)

class MessageFromDirectorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(MessageFromDirector, MessageFromDirectorAdmin)

class KeyAchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(KeyAchievement, KeyAchievementAdmin)

class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(Mission, MissionAdmin)

class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_per_page = 20
    
admin.site.register(Outcome, OutcomeAdmin)

class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 20
    
admin.site.register(AnnualReport, AnnualReportAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(Course, CourseAdmin)

class ThreeZeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(ThreeZero, ThreeZeroAdmin)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(Facility, FacilityAdmin)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'image_tag','status')
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    prepopulated_fields = {'slug': ('title',)}
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(Program, ProgramAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    prepopulated_fields = {'slug': ('title',)}
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
 
admin.site.register(News, BlogAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    prepopulated_fields = {'slug': ('title',)}
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
 
admin.site.register(Article, ArticleAdmin)

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','title',)
    prepopulated_fields = {'slug': ('title',)}
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'

admin.site.register(Events, EventsAdmin)

class TestomonialsAdmin(admin.ModelAdmin):
    list_display = ('fullname','designation', 'description', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','fullname',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(Testomonials, TestomonialsAdmin)

class ImageCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag',)
    list_per_page = 20
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('image_tag','title',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    

admin.site.register(ImageCategory, ImageCategoryAdmin)

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('category', 'image_tag',)
    list_per_page = 20
    list_display_links = ('image_tag','category',)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100 />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    
admin.site.register(ImageGallery, ImageGalleryAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('link',)
    list_per_page = 20
    
admin.site.register(Video, VideoAdmin)

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 20
    
admin.site.register(Archive, ArchiveAdmin)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 20
    
admin.site.register(OurPartner, PartnerAdmin)

class PartnerDataAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 20
    
admin.site.register(OurPartnerDatas, PartnerDataAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('fullname','designation','position',)
    list_per_page = 20
    
admin.site.register(Team, TeamAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject',)
    list_per_page = 20
    
admin.site.register(Contact, ContactAdmin)

class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('facebook','linkedin',)
    list_per_page = 20
    
admin.site.register(SocialAccount, SocialAccountAdmin)