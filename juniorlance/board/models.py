# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

MAX_VACANCY_INFO_LENGTH=1024
MAX_DEALER_INFO_LENGTH=1024
MAX_CONTACTS_LENGTH=64
MAX_MESSAGE_LENGTH=256
MAX_COMMENT_LENGTH=256
MAX_NAME_LENGTH=64

class Dealer(models.Model):
	name = models.CharField(verbose_name='Название',max_length=MAX_NAME_LENGTH)
	user = models.ForeignKey(User, verbose_name='Пользователь')
	info = models.TextField(verbose_name='Персональная информация', max_length=MAX_DEALER_INFO_LENGTH)
	contacts = models.ManyToManyField('Contact', verbose_name='Контакты')
	skills = models.ManyToManyField('Skill',verbose_name='Навыки')
	cost_hour = models.IntegerField(verbose_name='Цена оплаты за час')
	cost_month = models.IntegerField(verbose_name='Цена оплаты за месяц')
	location = models.ForeignKey('City',verbose_name='Город')

	def __unicode__(self):
		return self.name


class Vacancy(models.Model):
	JOB_KINDS = (
			(0,'За проект'),
			(1,'Почасовая'),
		)
	LOCATION_KINDS = (
			(0,'На месте'),
			(1,'Удаленная'),
		)
	VACANCY_STATES = (
			(0,'Активная'),
			(1,'Снята'),
		)
	name = models.CharField(max_length=128, verbose_name='Название вакансии')
	recruter = models.ForeignKey(Dealer, verbose_name='Рекрутер')
	info = models.TextField(max_length=MAX_VACANCY_INFO_LENGTH, verbose_name='Описание вакансии' )
	job_kind = models.IntegerField(verbose_name='Тип оплаты', choices=JOB_KINDS )
	location_kind = models.IntegerField(verbose_name='Требования к расположению', choices=LOCATION_KINDS )
	location = models.ForeignKey('City',verbose_name='Город')
	skills = models.ManyToManyField('Skill',verbose_name='Требования')
	cost = models.PositiveIntegerField(verbose_name='Цена', blank=True)
	state = models.IntegerField(verbose_name='Статус', choices=VACANCY_STATES )
	expieres = models.DateTimeField(verbose_name='Строк окончания', blank=True)

	def __unicode__(self):
		return self.name[:50]


class VacancyAppliement(models.Model):
	APPLY_STATES = (
			(0,'Не прочитаная'),
			(1,'Прочитаная'),
			(2,'Отказанная'),
			(3,'Выполненая'),
		)
	vacancy = models.ForeignKey(Vacancy,verbose_name='Вакансия')
	dealer = models.ForeignKey(Dealer,verbose_name='Пользователь')
	date = models.DateTimeField(verbose_name='Время отклика')
	status = models.IntegerField(verbose_name='Статус', choices=APPLY_STATES )

	def __unicode__(self):
		return self.date+':'+self.vacancy.name+'<->'+self.dealer.name


class Message(models.Model):
	MESSAGE_STATES = (
			(0,'Прочитанное'),
			(1,'Не прочитанное'),
		)
	message_box = models.ForeignKey(Dealer, related_name='box', verbose_name='Владелец сообщения', blank=True)
	message_sender = models.ForeignKey(Dealer,related_name='sender', verbose_name='Отправитель', blank=True)
	message_reciver = models.ForeignKey(Dealer,related_name='reciver', verbose_name='Получатель', blank=True)
	date = models.DateTimeField(verbose_name='Время отправки')
	text = models.TextField(max_length=MAX_MESSAGE_LENGTH,verbose_name='Текст сообщения')
	message_state = models.IntegerField(verbose_name='Статус сообщения', choices=MESSAGE_STATES )

	def __unicode__(self):
		return self.date+':'+self.sender.name+'-'+self.reciver.name+':'+self.text[:20]


class Comment(models.Model):
	vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия')
	sender = models.ForeignKey(Dealer, verbose_name='Отправитель')
	date = models.DateTimeField(verbose_name='Время')
	text = models.TextField(max_length=MAX_COMMENT_LENGTH,verbose_name='Текст коментария')

	def __unicode__(self):
		return self.vacancy.name+':<'+self.date+'>:'+self.sender.name+':'+self.text[:20]


class Contact(models.Model):
	CONTACT_KINDS = (
			(0,'телефон'),
			(1,'профиль в соцсети'),
			(2,'почта'),
			(3,'IRC'),
		)
	contact_kind = models.IntegerField(verbose_name='Тип контакта', choices=CONTACT_KINDS )
	value = models.CharField(max_length=MAX_CONTACTS_LENGTH,verbose_name='Контакт')

	def __unicode__(self):
		return self.contact_kind+":"+self.value


class Skill(models.Model):
	name = models.CharField(max_length=20, verbose_name='Название навыка')

	def __unicode__(self):
		return self.name


class City(models.Model):
	country = models.ForeignKey('Country',verbose_name='Страна')
	name = models.CharField(max_length=20, verbose_name='Название города')

	def __unicode__(self):
		return self.country.name+', '+self.name


class Country(models.Model):
	name = models.CharField(max_length=20,verbose_name='Название страны')

	def __unicode__(self):
		return self.name


