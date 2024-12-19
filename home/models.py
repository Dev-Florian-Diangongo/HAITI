from django.db import models
class Lwes(models.Model):

    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    pdf = models.FileField(upload_to='PDFS')
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.departement}"

    class Meta:
        verbose_name = "Lwes"
        verbose_name_plural = "Lwes"



class No(models.Model):
       
    pdf = models.FileField(upload_to='PDFS')

    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.departement}"

    class Meta:
        verbose_name = "No"
        verbose_name_plural = "Nos"




class Nodes(models.Model):
    pdf = models.FileField(upload_to='PDFS')


    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.departement}"

    class Meta:
        verbose_name = "Nodes"
        verbose_name_plural = "Nodes"




class Nodwes(models.Model) :
      
    pdf = models.FileField(upload_to='PDFS')

    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.departement}"

    class Meta:
        verbose_name = "Nodwes"
        verbose_name_plural = "Nodwes"



class Sid(models.Model) :
    pdf = models.FileField(upload_to='PDFS')

    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name = "Sid"
        verbose_name_plural = "Sids"
class Sides(models.Model) :
    
    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    pdf = models.FileField(upload_to='PDFS')

    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    class Meta :
        verbose_name = "Sides"
        verbose_name_plural = "Sides"
class Grandans(models.Model) :
    
    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    pdf = models.FileField(upload_to='PDFS')

    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Grandans"
        verbose_name_plural = "Grandans"
class Nip(models.Model):
    pdf = models.FileField(upload_to='PDFS')

    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Nip"
        verbose_name_plural = "Nips"
class Sant(models.Model) :
    
    pdf = models.FileField(upload_to='PDFS')

    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Sant"
        verbose_name_plural = "Sants"
class Latibonit(models.Model) :
    pdf = models.FileField(upload_to='PDFS')

    departement = models.CharField(max_length=20,  verbose_name="Dans quel département êtes-vous ?")
    
    # Informations personnelles
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Numéro de téléphone")
    
    # Sexe
    CHOIX_SEXES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=6, choices=CHOIX_SEXES, verbose_name="Sexe")
    
    # Date de naissance
    date_naissance = models.DateField(verbose_name="Date de naissance")
    
    # Photo d'identité
    photo_identite = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo d'identité")
    
    # Adresse actuelle
    pays_residence = models.CharField(max_length=100, verbose_name="Pays de résidence")
    ville = models.CharField(max_length=100, verbose_name="Ville actuelle")
    
    # Disponibilité pour déplacement
    CHOIX_DISPONIBILITE = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Peut-être', 'Peut-être'),
    ]
    disponibilite = models.CharField(max_length=10, choices=CHOIX_DISPONIBILITE, verbose_name="Disponibilité pour déplacement")
    
    # Explication sur l'origine
    explication_origine = models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")
    
    # Langues parlées
    CHOIX_LANGUES = [
        ('Creole', 'Kreyòl Ayisyen'),
        ('Anglais', 'Anglais'),
        ('Espagnol', 'Espagnol'),
        ('Hindi', 'Hindi'),
        ('Portugais', 'Portugais'),
        ('Russe', 'Russe'),
        ('Allemand', 'Allemand'),
        ('Français', 'Français'),
        ('Italien', 'Italien'),
        ('Arabe', 'Arabe'),
        ('Hausa', 'Hausa'),
        ('Japonais', 'Japonais'),
        ('Coréen', 'Coréen'),
        ('Turc', 'Turc'),
        ('Vietnamien', 'Vietnamien'),
        ('Thaï', 'Thaï'),
        ('Bengali', 'Bengali'),
        ('Persan', 'Persan'),
        ('Urdu', 'Urdu'),
        ('Autre', 'Autre'),
    ]
    langues_parlees = models.CharField(max_length=200, choices=CHOIX_LANGUES, verbose_name="Combien de langues parlez-vous ?", blank=True, null=True)
    
    # Expérience professionnelle
    experience_professionnelle = models.TextField(verbose_name="Parlez-nous un peu de votre travail actuel.", blank=True, null=True)
    
    # Type de travail souhaité
    CHOIX_TYPE_TRAVAIL = [
        ('Plein temps', 'Travail à plein temps'),
        ('Temps partiel', 'Travail à temps partiel'),
    ]
    type_travail = models.CharField(max_length=20, choices=CHOIX_TYPE_TRAVAIL, verbose_name="Quel type de travail souhaitez-vous ?", blank=True, null=True)
    
    # Région en Haïti
    region_haïtienne = models.CharField(max_length=200, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?", blank=True, null=True)
    
    # Connexion culturelle
    connexion_culturelle = models.TextField(verbose_name="Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.", blank=True, null=True)
    
    # Engagement communautaire
    engagement_communautaire = models.TextField(verbose_name="Description des activités ou groupes auxquels vous avez participé en Haïti", blank=True, null=True)
    
    # Disponibilité pour contribuer
    CHOIX_DISPONIBILITE_CONTRIBUER = [
        ('À distance', 'À distance'),
        ('En personne', 'En personne'),
    ]
    disponibilite_contribuer = models.CharField(max_length=15, choices=CHOIX_DISPONIBILITE_CONTRIBUER, verbose_name="Disponibilité pour contribuer")
    
    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Latibonit"
        verbose_name_plural = "Latibonits"
        

