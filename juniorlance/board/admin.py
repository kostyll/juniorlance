from django.contrib import admin
from django.db.models import Model

from board.models import Dealer, Vacancy, VacancyAppliement, Message, Comment, Contact, Skill, City, Country

admin.site.register(Dealer)
admin.site.register(Vacancy)
admin.site.register(VacancyAppliement)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(City)
admin.site.register(Country)