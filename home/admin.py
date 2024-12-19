from django.contrib import admin
from .models import (  Lwes,
                     Nodes,
                     No,
                     Nodwes,
                     Sid,
                     Sides,
                     Grandans,
                     Nip,
                     Sant,
                     Latibonit
                     )
class AdminLwes(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Lwes, AdminLwes)
class AdminNodes(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Nodes,AdminNodes)
class AdminNo(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(No,AdminNo)
class AdminNodwes(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Nodwes, AdminNodwes)

class AdminSid(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Sid, AdminSid)
class AdminSides(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Sides, AdminSides)

class AdminGrandans(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Grandans, AdminGrandans)

class AdminNip(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Nip, AdminNip)

class AdminSant(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Sant, AdminSant)
class AdminLatibonit(admin.ModelAdmin) :
    list_display = [
        "departement","prenom","nom","email","telephone","sexe",
        "date_naissance","photo_identite","pays_residence",
        "ville","disponibilite","explication_origine","langues_parlees",
        "experience_professionnelle","type_travail",
        "region_haïtienne","connexion_culturelle",
        "engagement_communautaire","disponibilite_contribuer",
        "date_creation","date_mise_a_jour",
    ]
admin.site.register(Latibonit, AdminLatibonit)
