import tempfile
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from django.shortcuts import render,get_object_or_404
from django.utils.crypto import get_random_string
from fpdf import FPDF
from io import BytesIO
from django import template
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import io
from django.core.files import File
from .models import (Lwes,
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
def Register_in_all_table(request) :
    """
 la logique pour inscrire les users dans une table specifique se trouve dans cette fonction
 l'inscription dans les tables se fait selon le choix de user lors du remplissage de données

    """
    message =""
    if request.method == "POST" :
        departement = request.POST.get("departement")
        prenom = request.POST.get("prenom")
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        sexe = request.POST.get("sexe")
        date_naissance = request.POST.get("date_naissance")
        photo_identite = request.FILES['photo_identite']
        pays_residence = request.POST.get("pays_residence")
        ville = request.POST.get("ville")
        disponibilite = request.POST.get("disponibilite")
        langues_parlees = request.POST.get("langues_parlees")
        explication_origine = request.POST.get("explication_origine")
        engagement_communautaire = request.POST.get("engagement_communautaire")
        disponibilite_contribuer = request.POST.get("disponibilite_contribuer")
        """
        je veux verifier les champs requis: nom, departement, ...
        
        """
        if departement is None or prenom is None or nom is None or email is None or sexe is None or date_naissance is None  or pays_residence is None or ville is None or disponibilite is None or disponibilite_contribuer is None or langues_parlees is None :
            message = "certains champ obligatoires en etoile rouge ne sont pas remplis !"
            return render(request, "dashbord/login.html", context={"message":message})
        try : 
            """

            creation du pdf automatiquement quand l'user soumet les infos
            
            """
            pdf_buffer = io.BytesIO()
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="user_info.pdf"'
            # Ajout des informations dans le PDF
            c = canvas.Canvas(response)
            c.drawString(100, 800, f"Nom: {prenom} {nom}")
            c.drawString(100, 780, f"Département: {departement}")
            c.drawString(100, 760, f"Email: {email}")
            c.drawString(100, 740, f"Téléphone: {telephone}")
            c.drawString(100, 720, f"Sexe: {sexe}")
            c.drawString(100, 700, f"Date de Naissance: {date_naissance}")
            c.drawString(100, 680, f"Pays de Résidence: {pays_residence}")
            c.drawString(100, 660, f"Ville: {ville}")
            c.drawString(100, 640, f"Disponibilité: {disponibilite}")
            c.drawString(100, 620, f"Langues Parlées: {langues_parlees}")
            c.drawString(100, 600, f"Explication de l'origine: {explication_origine}")
            c.drawString(100, 580, f"Engagement communautaire: {engagement_communautaire}")
            c.drawString(100, 560, f"Disponibilité à contribuer: {disponibilite_contribuer}")

            
            c.save()
            pdf_buffer.seek(0)

            # Créer un fichier à partir du PDF en mémoire
            pdf_file = File(pdf_buffer, name=f"user_info_{nom}.pdf")

            datas = {"pdf":pdf_file,
                "departement"  :departement,
                        "prenom" :prenom,
                        "nom" :nom,
                        "email" :email,
                        "telephone" : telephone,
                        "sexe" : sexe,
                        "date_naissance" : date_naissance,
                        "photo_identite" : photo_identite,
                        "pays_residence" :pays_residence,
                        "ville" :ville,
                        "disponibilite" : disponibilite,
                        "langues_parlees" : langues_parlees,
                        "explication_origine" : explication_origine,
                        "engagement_communautaire" : engagement_communautaire,
                        "disponibilite_contribuer" :disponibilite_contribuer}
            if departement == "Lwes" :
                    if Lwes.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                    user_create = Lwes.objects.create(**datas)
                    user_create.save()
                    if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})
            elif departement == 'No' :
                if No.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                user_create = No.objects.create(**datas)
                user_create.save()
                if user_create:
                    message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                    return render(request, "dashbord/login.html", context={"messages":message})
            elif departement == "Nodes" :
                if Nodes.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                user_create = Nodes.objects.create(**datas)
                user_create.save()
                if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})
            elif departement == "Nodwes" :
                if Nodwes.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                user_create = Nodwes.objects.create(**datas)
                user_create.save()
                if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})   
            elif departement == "Sid" :
                if Sid.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                user_create = Sid.objects.create(**datas)
                user_create.save()
                if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})   
            elif departement == "Sides" :
                    if Sides.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                    user_create = Sides.objects.create(**datas)
                    user_create.save()
                    if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})   
            elif departement == "Grandans" :
                    if Grandans.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                    user_create = Grandans.objects.create(**datas)
                    user_create.save()
                    if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})   
            elif departement == "Nip" :
                    if Nip.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                    user_create = Nip.objects.create(**datas)
                    user_create.save()
                    if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})   
            elif departement == "Sant" :
                    if Sant.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                    user_create = Sant.objects.create(**datas)
                    user_create.save()
                    if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})   
            elif departement == "Latibonit" :
                    if Latibonit.objects.filter(email=email).exists():
                        message = f"Imèl sa déjà anrejistre. Silvouplè itilize yon lòt. :'{email}'  "
                        return render(request, "dashbord/login.html", context={"message":message})
                    user_create = Latibonit.objects.create(**datas)
                    user_create.save()
                    if user_create:
                        message = f"Mèsi paske w soumèt enfòmasyon w yo bay Resansman Djaspora! {departement}"
                        return render(request, "dashbord/login.html", context={"messages":message})   
            else :
                message = f" '{departement}' n'est pas pris en en charge"
                return render(request, "dashbord/page_error.html", context={"message":message})
        except Exception as e :
            message = f"verification échouée ! {e} "
            return render(request, "dashbord/login.html", context={"message": message})
        departement=""
        return response
    return render(request, "dashbord/login.html")
def home(request):
    context = {
    "nodes" : Nodes.objects.count(),
    "lwes" : Lwes.objects.count(),
    "no" : No.objects.count(),
    "nodwes" : Nodwes.objects.count(),
    "sid" : Sid.objects.count(),
    "sides" : Sides.objects.count(),
    "grandans" : Grandans.objects.count(),
    "nip" :Nip.objects.count(),
    "sant":Sant.objects.count(),
    "latibonit":Latibonit.objects.count(),
    }
    return render(request, "dashbord/index.html", context)

    
def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser) 
def index(request):
 
    context = {
    "nodes" : Nodes.objects.count(),
    "lwes" : Lwes.objects.count(),
    "no" : No.objects.count(),
    "nodwes" : Nodwes.objects.count(),
    "sid" : Sid.objects.count(),
    "sides" : Sides.objects.count(),
    "grandans" : Grandans.objects.count(),
    "nip" :Nip.objects.count(),
    "sant":Sant.objects.count(),
    "latibonit":Latibonit.objects.count(),
    'segment': 'index'
    } 
   
    return render(request, "home/index.html", context)

@user_passes_test(is_superuser)
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


 
@user_passes_test(is_superuser)
def model_counts_view(request):
    
    model_counts = [
        {'model_name': 'Lwes', 'count': Lwes.objects.count()},
        {'model_name': 'No', 'count': No.objects.count()},
        {'model_name': 'Nodes', 'count': Nodes.objects.count()},
        {'model_name': 'Nodwes', 'count': Nodwes.objects.count()},
        {'model_name': 'Sid', 'count': Sid.objects.count()},
        {'model_name': 'Sides', 'count': Sides.objects.count()},
        {'model_name': 'Grandans', 'count': Grandans.objects.count()},
        {'model_name': 'Nip', 'count': Nip.objects.count()},
        {'model_name': 'Sant', 'count': Sant.objects.count()},
        {'model_name': 'Latibonit', 'count': Latibonit.objects.count()},
    ]
    
    return render(request, 'home/tables.html', {'model_counts': model_counts})

@user_passes_test(is_superuser)
def model_people_view(request, model_name):
    """
    Affiche la liste des personnes d'un département donné.
    """
    # Récupérer le modèle en fonction du nom fourni
    if model_name == 'Lwes':
        model = Lwes
    elif model_name == 'No':
        model = No
    elif model_name == 'Nodes':
        model = Nodes
    elif model_name == 'Nodwes':
        model = Nodwes
    elif model_name == 'Sid':
        model = Sid
    elif model_name == 'Sides':
        model = Sides
    elif model_name == 'Grandans':
        model = Grandans
    elif model_name == 'Nip':
        model = Nip
    elif model_name == 'Sant':
        model = Sant
    elif model_name == 'Latibonit':
        model = Latibonit
    else:
        return render(request, 'dashboard/error.html', {'message': 'Département non trouvé'})

    # Récupérer toutes les personnes du modèle spécifié
    people = model.objects.all()

    # Passer les personnes au template
    return render(request, 'home/member.html', {'people': people, 'model_name': model_name})

def download_pdf(request, person_id):
    """
    Permet de télécharger le PDF d'un utilisateur. le lien qui est passé est celui-ci : 127.0.0.1:8000/download_pdf/<int:person_id>/
    donc person_id sera remplacer par chaque id de l'utilisateur inscrit
    """
  
    user = None
    for model in [Lwes, Nodes, No, Nodwes, Sid, Sides, Grandans, Nip, Sant, Latibonit]:
        try:
            user = model.objects.get(id=person_id)
            break
        except model.DoesNotExist:
            continue

    if not user:
        return HttpResponse("Utilisateur non trouvé", status=404)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="user_{user.id}_info.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    c.drawString(100, 750, f"Nom: {user.nom} {user.prenom}")
    c.drawString(100, 730, f"Département: {user.departement}")
    c.drawString(100, 710, f"Email: {user.email}")
    c.drawString(100, 690, f"Téléphone: {user.telephone}")
    c.drawString(100, 670, f"Sexe: {user.sexe}")
    c.drawString(100, 650, f"Date de naissance: {user.date_naissance}")
    c.drawString(100, 630, f"Ville: {user.ville}")
    c.drawString(100, 610, f"Disponibilité: {user.disponibilite}")
    c.drawString(100, 590, f"Langues parlées: {user.langues_parlees}")
    c.drawString(100, 570, f"Engagement communautaire: {user.engagement_communautaire}")
    c.drawString(100, 550, f"Disponibilité à contribuer: {user.disponibilite_contribuer}")
    c.save()

    return response

def Resansman(request) :
    return render(request, "home/service.html")