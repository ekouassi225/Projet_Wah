# vim: set fileencoding=utf-8 :
from django.contrib import admin

import BackendPortfolio.models as models


class mypicAdmin(admin.ModelAdmin):

    list_display = ('id', 'mypic')
    list_filter = ('id', 'mypic')


class mynameisAdmin(admin.ModelAdmin):

    list_display = ('id', 'mynameis')
    list_filter = ('id', 'mynameis')


class mescomptesAdmin(admin.ModelAdmin):

    list_display = ('id', 'facebook', 'twitter', 'insta', 'link')
    list_filter = ('id', 'facebook', 'twitter', 'insta', 'link')


class jesuisAdmin(admin.ModelAdmin):

    list_display = ('id', 'jesuis1', 'jesuis2', 'jesuis3', 'jesuis4')
    list_filter = ('id', 'jesuis1', 'jesuis2', 'jesuis3', 'jesuis4')


class APM_HAdmin(admin.ModelAdmin):

    list_display = ('id', 'Aboutme_header')
    list_filter = ('id', 'Aboutme_header')


class TitleAdmin(admin.ModelAdmin):

    list_display = ('id', 'Title')
    list_filter = ('id', 'Title')


class Title_headerAdmin(admin.ModelAdmin):

    list_display = ('id', 'Title_header')
    list_filter = ('id', 'Title_header')


class JustMeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'birthday',
        'Number',
        'City',
        'Pays',
        'Age',
        'LastDiploma',
        'Mail',
        'Linked',
        'Freelance',
    )
    list_filter = (
        'birthday',
        'id',
        'Number',
        'City',
        'Pays',
        'Age',
        'LastDiploma',
        'Mail',
        'Linked',
        'Freelance',
    )


class Competences_headerAdmin(admin.ModelAdmin):

    list_display = ('id', 'header')
    list_filter = ('id', 'header')


class CompetencesAdmin(admin.ModelAdmin):

    list_display = ('id', 'skills', 'Percent')
    list_filter = ('id', 'skills', 'Percent')


class formation_headerAdmin(admin.ModelAdmin):

    list_display = ('id', 'header')
    list_filter = ('id', 'header')


class formationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'Diplome',
        'Year_debut',
        'Year_end',
        'University',
        'Location_ville',
        'Location_pays',
    )
    list_filter = (
        'Year_debut',
        'Year_end',
        'id',
        'Diplome',
        'University',
        'Location_ville',
        'Location_pays',
    )


class EXP_proAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'Poste',
        'Year_debut',
        'Year_end',
        'Entreprise',
        'Location_ville',
        'Location_pays',
        'Description',
    )
    list_filter = (
        'Year_debut',
        'Year_end',
        'id',
        'Poste',
        'Entreprise',
        'Location_ville',
        'Location_pays',
        'Description',
    )


class Portfolio_headerAdmin(admin.ModelAdmin):

    list_display = ('id', 'header')
    list_filter = ('id', 'header')


class Portfolio_categorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'Categorie')
    list_filter = ('id', 'Categorie')


class Portfolio_carteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'Carte',
        'Carte_suplementaire',
        'Description',
        'Name',
        'DateProjet',
        'Url',
        'NomProjet',
    )
    list_filter = (
        'categorie',
        'DateProjet',
        'id',
        'Carte',
        'Carte_suplementaire',
        'Description',
        'Name',
        'Url',
        'NomProjet',
    )


class Service_headerAdmin(admin.ModelAdmin):

    list_display = ('id', 'header')
    list_filter = ('id', 'header')


class Service_categorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'Categorie')
    list_filter = ('id', 'Categorie')


class ServiceAdmin(admin.ModelAdmin):

    list_display = ('id', 'categorie', 'Titre', 'Description')
    list_filter = ('categorie', 'id', 'Titre', 'Description')


class Contact_messageAdmin(admin.ModelAdmin):

    list_display = ('id', 'NomPrenom', 'Mail', 'Object', 'Message')
    list_filter = ('id', 'NomPrenom', 'Mail', 'Object', 'Message')


class Contact_headerAdmin(admin.ModelAdmin):

    list_display = ('id', 'header')
    list_filter = ('id', 'header')


class audioAdmin(admin.ModelAdmin):

    list_display = ('id', 'audio')
    list_filter = ('id', 'audio')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.mypic, mypicAdmin)
_register(models.mynameis, mynameisAdmin)
_register(models.mescomptes, mescomptesAdmin)
_register(models.jesuis, jesuisAdmin)
_register(models.APM_H, APM_HAdmin)
_register(models.Title, TitleAdmin)
_register(models.Title_header, Title_headerAdmin)
_register(models.JustMe, JustMeAdmin)
_register(models.Competences_header, Competences_headerAdmin)
_register(models.Competences, CompetencesAdmin)
_register(models.formation_header, formation_headerAdmin)
_register(models.formation, formationAdmin)
_register(models.EXP_pro, EXP_proAdmin)
_register(models.Portfolio_header, Portfolio_headerAdmin)
_register(models.Portfolio_categorie, Portfolio_categorieAdmin)
_register(models.Portfolio_carte, Portfolio_carteAdmin)
_register(models.Service_header, Service_headerAdmin)
_register(models.Service_categorie, Service_categorieAdmin)
_register(models.Service, ServiceAdmin)
_register(models.Contact_message, Contact_messageAdmin)
_register(models.Contact_header, Contact_headerAdmin)
_register(models.audio, audioAdmin)
