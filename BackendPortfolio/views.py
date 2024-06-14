from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import numpy as np
from . import models


def index (request):
    data = {
        'JS' : models.jesuis.objects.all(),

        'MP' : models.mypic.objects.all(),

        'MC' : models.mescomptes.objects.all(),

        'audio' : models.audio.objects.all(),

        'MonNom' : models.mynameis.objects.all(),

        'ABme' : models.APM_H.objects.all(),

        'Title' : models.Title.objects.all(),

        'Title_header' : models.Title_header.objects.all(),

        'JM' : models.JustMe.objects.all(),

        'fact_project' : models.Portfolio_carte.objects.count(),


        'Competence_head' : models.Competences_header.objects.all(), 
        'competence' : models.Competences.objects.all(),

        'formation_head' : models.formation_header.objects.all(),
        'form' : models.formation.objects.all(),
        'EXP' : models.EXP_pro.objects.all(),

        'Portfolio_head' : models.Portfolio_header.objects.all(),
        'Portfolio_carte' : models.Portfolio_carte.objects.all(),
        'Portfolio_cat' : models.Portfolio_categorie.objects.all(),
        
        'service_head' : models.Service_header.objects.all(),
        'service_carte' : models.Service.objects.all(),
        'service_cat' : models.Service_categorie.objects.all(),

        'Contact_header' : models.Contact_header.objects.all(),

        'contact_message' : models.Contact_message.objects.all(),

    }
    return render (request, 'index.html', data)


def Portfolio_detail (request, portfolio_carte_id):
    
    data = {
        'carte' : models.Portfolio_carte.objects.get(id = portfolio_carte_id),
        'MC' : models.mescomptes.objects.all(),
        'JS' : models.jesuis.objects.all(),
        'MP' : models.mypic.objects.all(),
        'audio' : models.audio.objects.all(),
    }
    return render (request, 'portfolio-details.html', data)




def formulaire (request: HttpRequest) -> HttpResponse :

    if request.method == 'POST' :
        nom = request.POST.get('name')
        mail = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        textme = models.Contact_message (
            NomPrenom = nom,
            Mail = mail,
            Object = subject,
            Message = message
        )
        textme.save()
    return HttpResponse('Succes')