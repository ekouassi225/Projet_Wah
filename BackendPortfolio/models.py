from django.db import models

class mypic (models.Model):
    mypic = models.ImageField(upload_to="Projet_Wah\media\media_cdn", height_field=None, width_field=None, max_length=None)

    class Meta :
        verbose_name = 'maphoto'
        verbose_name_plural = 'MesPhotos'


class mynameis (models.Model):
    mynameis = models.CharField(max_length=50)

    class Meta :
        verbose_name = 'MonNom'
        verbose_name_plural = 'MesNoms'

    def __str__(self) :
        return self.mynameis


class mescomptes (models.Model):
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    insta = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    class Meta :
        verbose_name = 'MonCompte'
        verbose_name_plural = 'mescomptes'

    def __str__(self) :
        return 'Reseau'
        

class jesuis (models.Model):
    jesuis1 = models.CharField(max_length=50, default=None)
    jesuis2 = models.CharField(max_length=50, default=None)
    jesuis3 = models.CharField(max_length=50, default=None)
    jesuis4 = models.CharField(max_length=50, default=None)

    class Meta :
        verbose_name = 'jesuis'
        verbose_name_plural = 'JeSuiS'


class APM_H (models.Model):
    Aboutme_header= models.TextField ()

    class Meta :
        verbose_name = 'Aboutme_header'
        verbose_name_plural = 'AboutMe_header'



class Title (models.Model):
    Title = models.CharField(max_length=50)

    class Meta :
        verbose_name = 'Titre'
        verbose_name_plural = 'Titres'

    def __str__(self) :
        return self.Title



class Title_header (models.Model):
    Title_header = models.TextField()

    class Meta :
        verbose_name = 'header_titre'
        verbose_name_plural = 'Header_Titres'

    def __str__(self) :
        return self.Title_header



class JustMe (models.Model):
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    Number = models.CharField(max_length=10)
    City = models.CharField(max_length=50)
    Pays = models.CharField(max_length=50)
    Age = models.PositiveIntegerField()
    LastDiploma = models.CharField(max_length=50)
    Mail = models.EmailField(max_length=254)
    Linked = models.CharField(max_length=50)
    Freelance = models.CharField(max_length=50)

    class Meta :
        verbose_name = 'juste_moi'
        verbose_name_plural = 'Juste_Moi'




class Competences_header (models.Model):
    header = models.TextField()
    class Meta :
        verbose_name = 'competence_header'
        verbose_name_plural = 'Competences_Headers'


class Competences (models.Model):
    skills = models.CharField(max_length=50)
    Percent = models.PositiveIntegerField()

    class Meta :
        verbose_name = 'competence'
        verbose_name_plural = 'Competences'

    def __str__(self) :
        return self.skills


class formation_header (models.Model):
    header = models.TextField()
    class Meta :
        verbose_name = 'formation_header'
        verbose_name_plural = 'Formation_Headers'


class formation (models.Model):
    Diplome = models.CharField(max_length=100)
    Year_debut = models.DateField(auto_now=False, auto_now_add=False)
    Year_end = models.DateField(auto_now=False, auto_now_add=False, default=None)
    University = models.CharField(max_length=100)
    Location_ville = models.CharField(max_length=50)
    Location_pays = models.CharField(max_length=50)

    class Meta :
        verbose_name = 'formation'
        verbose_name_plural = 'Formations'

    def __str__(self) :
        return self.Diplome


class EXP_pro (models.Model):
    Poste = models.CharField(max_length=50)
    Year_debut = models.DateField(auto_now=False, auto_now_add=False)
    Year_end = models.DateField(auto_now=False, auto_now_add=False)
    Entreprise = models.CharField(max_length=50)
    Location_ville = models.CharField(max_length=50)
    Location_pays = models.CharField(max_length=50)
    Description = models.TextField(default=None)

    class Meta :
        verbose_name = 'EXP_pro'
        verbose_name_plural = 'EXPs_Pro'

    def __str__(self) :
        return self.Poste



class Portfolio_header (models.Model):
    header = models.TextField()
    class Meta :
        verbose_name = 'portfolio_header'
        verbose_name_plural = 'Portfolio_headers'



class Portfolio_categorie (models.Model):
    Categorie = models.CharField(max_length=20)
    class Meta :
        verbose_name = 'portfolio_categorie'
        verbose_name_plural = 'Portfolio_categories'

    def __str__(self) -> str:
        return self.Categorie

class Portfolio_carte (models.Model):
    categorie = models.ForeignKey(Portfolio_categorie, on_delete=models.CASCADE)
    Carte = models.ImageField(upload_to='Backend\media\media_cdn', height_field=None, width_field=None, max_length=None, default=None)
    Carte_suplementaire = models.ImageField(upload_to='Backend\media\media_cdn', height_field=None, width_field=None, max_length=None, default=None)
    Description = models.TextField()
    Name = models.CharField(max_length=50,default=None)
    DateProjet = models.DateField(auto_now_add=True)
    Url = models.CharField(max_length=50,default=None)
    NomProjet = models.CharField(max_length=50, default=None)
    

    class Meta :
        verbose_name = 'portfolio_carte'
        verbose_name_plural = 'Portfolio_cartes'

    def __str__(self) :
        return self.NomProjet



class Service_header (models.Model):
    header = models.TextField()
    class Meta :
        verbose_name = 'service_header'
        verbose_name_plural = 'Services_Headers'
    

class Service_categorie (models.Model):
    Categorie = models.CharField(max_length=30)
    class Meta :
        verbose_name = 'Service_categorie'
        verbose_name_plural = 'Services_categories'
    
    def __str__(self) -> str:
        return self.Categorie


class Service (models.Model):
    categorie = models.ForeignKey(Service_categorie, on_delete=models.CASCADE)
    Titre = models.CharField(max_length=50,default=None)
    Description = models.TextField(default=None)

    class Meta :
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) :
        return self.categorie



class Contact_message (models.Model):
    NomPrenom = models.CharField(max_length=100)
    Mail = models.EmailField(max_length=254)
    Object = models.CharField(max_length=50, default=None)
    Message = models.TextField()
    
    class Meta :
        verbose_name = 'Contact_message'
        verbose_name_plural = 'Contacts_Messages'

    def __str__(self) :
        return self.NomPrenom


class Contact_header (models.Model):
    header = models.TextField()
    class Meta :
        verbose_name = 'Contact_header'
        verbose_name_plural = 'Contacts_Headers'


class audio (models.Model):
    audio = models.FileField(upload_to=None, max_length=100)
    class Meta :
        verbose_name = 'audio'
        verbose_name_plural = 'audios'