# Generated by Django 5.1.2 on 2024-12-18 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grandans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Grandans',
                'verbose_name_plural': 'Grandans',
            },
        ),
        migrations.CreateModel(
            name='Latibonit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Latibonit',
                'verbose_name_plural': 'Latibonits',
            },
        ),
        migrations.CreateModel(
            name='Lwes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lwes',
                'verbose_name_plural': 'Lwes',
            },
        ),
        migrations.CreateModel(
            name='Nip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Nip',
                'verbose_name_plural': 'Nips',
            },
        ),
        migrations.CreateModel(
            name='No',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'No',
                'verbose_name_plural': 'Nos',
            },
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Nodes',
                'verbose_name_plural': 'Nodes',
            },
        ),
        migrations.CreateModel(
            name='Nodwes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Nodwes',
                'verbose_name_plural': 'Nodwes',
            },
        ),
        migrations.CreateModel(
            name='Sant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sant',
                'verbose_name_plural': 'Sants',
            },
        ),
        migrations.CreateModel(
            name='Sid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sid',
                'verbose_name_plural': 'Sids',
            },
        ),
        migrations.CreateModel(
            name='Sides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(max_length=20, verbose_name='Dans quel département êtes-vous ?')),
                ('pdf', models.FileField(upload_to='PDFS')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('date_naissance', models.DateField(verbose_name='Date de naissance')),
                ('photo_identite', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name="Photo d'identité")),
                ('pays_residence', models.CharField(max_length=100, verbose_name='Pays de résidence')),
                ('ville', models.CharField(max_length=100, verbose_name='Ville actuelle')),
                ('disponibilite', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Peut-être', 'Peut-être')], max_length=10, verbose_name='Disponibilité pour déplacement')),
                ('explication_origine', models.TextField(verbose_name="Expliquez-nous un peu d'où vous venez en Haïti")),
                ('langues_parlees', models.CharField(blank=True, choices=[('Creole', 'Kreyòl Ayisyen'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Hindi', 'Hindi'), ('Portugais', 'Portugais'), ('Russe', 'Russe'), ('Allemand', 'Allemand'), ('Français', 'Français'), ('Italien', 'Italien'), ('Arabe', 'Arabe'), ('Hausa', 'Hausa'), ('Japonais', 'Japonais'), ('Coréen', 'Coréen'), ('Turc', 'Turc'), ('Vietnamien', 'Vietnamien'), ('Thaï', 'Thaï'), ('Bengali', 'Bengali'), ('Persan', 'Persan'), ('Urdu', 'Urdu'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Combien de langues parlez-vous ?')),
                ('experience_professionnelle', models.TextField(blank=True, null=True, verbose_name='Parlez-nous un peu de votre travail actuel.')),
                ('type_travail', models.CharField(blank=True, choices=[('Plein temps', 'Travail à plein temps'), ('Temps partiel', 'Travail à temps partiel')], max_length=20, null=True, verbose_name='Quel type de travail souhaitez-vous ?')),
                ('region_haïtienne', models.CharField(blank=True, max_length=200, null=True, verbose_name="Dans quelle région d'Haïti avez-vous des proches ?")),
                ('connexion_culturelle', models.TextField(blank=True, null=True, verbose_name='Expliquez-nous un peu comment vous êtes connecté à la culture haïtienne.')),
                ('engagement_communautaire', models.TextField(blank=True, null=True, verbose_name='Description des activités ou groupes auxquels vous avez participé en Haïti')),
                ('disponibilite_contribuer', models.CharField(choices=[('À distance', 'À distance'), ('En personne', 'En personne')], max_length=15, verbose_name='Disponibilité pour contribuer')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sides',
                'verbose_name_plural': 'Sides',
            },
        ),
    ]
