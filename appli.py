#!/usr/bin/python3


from tkinter import *
from tkinter.ttk import Combobox
import datetime

nb_ingredients = 0
liste_ingredients = []
liste_saison = ["les deux","saison froide","saison chaude"]


class recette:
    """
    une recette consiste en un nom 'name', une liste d'ingrédients, un groupe ("midi_famille", "midi_semaine", "soir_famille", 
    "accompagnement_barbecue",...), une saison et d'éventuels commentaires.
    """
    def __init__(self, name, ingredients = [], groupe = "midi de semaine", saison ="tout le temps", notes = None, ):
        self.name = name
        self.ingredients = ingredients
        self.groupe = groupe
        self.saison = saison
        self.notes = notes

    def afficher(self):
        """
        Affiche les informations de la recette dans la console. (debug)
        """
        print(self.name)
        for s in self.saison:
            print(s,end=" ")
        print("")
        print("INGREDIENTS :")
        for i in range(len(self.ingredients)):
            print(f"-{self.ingredients[i]}")
        if self.notes != None:
            print("NOTES :")
            print(self.notes)

    def ajouter_ingredients(self):
        """
        Ajoute des ingrédients à la recette via la console.
        """
        print("Voici la liste des ingredients :")
        for i in range(len(self.ingredients)):
            print(f"-{self.ingredients[i]}")
        print("Ajoutez des ingrédients à votre recette, un par un. Quand vous avez fini, faites entrée.")
        ingredient = input("Ajoutez un ingrédient : ")
        while ingredient != '':
            self.ingredients.append(ingredient)
            print("Ajouté !")
            ingredient = input("Ajoutez un ingrédient : ")
        self.afficher()

    def modifier_saison(self):
        """
        Modifie la saison pour laquelle la recette est adaptée.
        """
        s = input("Cette recette est-elle adaptée pour une saison en particulier ? Si oui, laquelle ? écrivez 'non' ou seulement la saison concernée, en minuscule et sans accent(s): ")
        while s != 'non':
            while s != 'non' and s != 'ete' and s != 'hiver' and s != 'automne' and s !='printemps':
                s = input("Il y a eu une erreur. S'il vous plaît, vérifiez l'orthographe, les minuscules et les accents. Ré-écrivez votre réponse : ")        
            if s != 'non':
                self.saison.append(s)
                s = input("Cette recette est-elle adaptée pour une saison en particulier ? Si oui, laquelle ? écrivez 'non' ou seulement la saison concernée, en minuscule et sans accent(s): ")

    def modifier_groupe(self):
        """
        Modifie le type de repas pour lequel la recette est adaptée.
        """
        groupe = input("A quelle occasion dégustez-vous ce plat ? (midi_famille, midi_semaine, soir, soir_wk, )")
        

    def ajouter_notes(self):
        """
        Ajoute des commentaires à la recette via la console.
        """
        notes = input("Souhaitez vous ajouter des commentaires ? Sinon, faites simplement entrée. \n")
        self.notes = notes

    def supprimer_ingredients(self):
        """
        Supprime des ingrédients de la recette via la console.
        """
        print("Vous allez supprimer des ingrédients un par un. Quand vous avez fini, faites entrée. ")
        ingredient = '0'
        while ingredient != '':
            print("Voici la liste des ingredients :")
            for i in range(len(self.ingredients)):
                print(f"-{self.ingredients[i]}")
            ingredient = input("Lequel voulez-vous supprimer ? écrivez-le exactement comme dans la recette : ")
            while ingredient not in self.ingredients and ingredient != '':
                ingredient = input("Il y a eu une erreur, vérifiez l'orthographe et les majuscules : ")
            if ingredient in self.ingredients :
                i = 0
                while i < len(self.ingredients) and self.ingredients[i] != ingredient:
                    i += 1
                self.ingredients.pop(i)

    def ajouter(self):
        """
        Ajoute la recette à la base de données (fichier 'recettes').
        """
        liste_recettes = extraire_recettes()
        if self.name in liste_recettes :
            print("Cette recette existe déjà ou alors une autre recette porte le même. Elle ne sera pas ajoutée.")
        else :
            fichier_recettes = open('recettes','a')
            fichier_recettes.write(f"{self.name};{self.ingredients};{self.groupe};{self.saison};{self.notes}\n")
            fichier_recettes.close()
        
def extraire_recettes():
    """
    Extrait les recettes du fichier 'recettes' dans une liste.
    """
    fichier_recettes = open('recettes','r')
    liste_recettes = fichier_recettes.read()
    liste_recettes = liste_recettes.split('\n')
    liste_recettes_objets = []
    for i in range(len(liste_recettes)-1):
        liste_recettes[i] = liste_recettes[i].split(";")
        liste_recettes_objets.append(recette(liste_recettes[i][0],eval(liste_recettes[i][1]),liste_recettes[i][2],liste_recettes[i][3]))
    fichier_recettes.close()
    return liste_recettes_objets

def ajouter_groupe(groupe):
    """
    Ajoute un groupe à la base de données (fichier 'groupes').
    """
    fichier_groupes = open('groupes','a')
    fichier_groupes.write(f";{groupe}")
    fichier_groupes.close()

def extraire_groupes():
    """
    Extrait les groupes du fichier 'groupes' dans une liste.
    """
    fichier_groupes = open('groupes','r')
    liste_groupes = fichier_groupes.read()
    liste_groupes = liste_groupes.split(';')
    fichier_groupes.close()
    return liste_groupes

def trier_recettes_saison(liste_recettes, saison):
    """
    Trie les recettes par saison.
    """
    liste_recettes_saison = []
    for recette in liste_recettes:
        if saison in recette.saison :
            liste_recettes_saison.append(recette)
    return liste_recettes_saison

def cherche_recette(nom, liste):
    """
    Cherche une recette par son nom dans une liste.
    """
    for recette in liste:
        if recette.name.upper() == unidecode.unidecode(nom.upper()):
            return recette
    
def titres_toutes_recettes(liste):
    """
    Retourne une liste des titres de toutes les recettes.
    """
    titres = []
    for recette in liste:
        titres.append(recette.name)
    return titres


#affichage

def ajouter_ingredients_ajout():
    """
    Ajoute un ingrédient à la liste des ingrédients à partir de l'interface graphique et met à jour l'affichage.
    """
    global liste_ingredients, ingredient
    liste_ingredients.append(ingredient.get())
    ingredient.destroy()
    nouvel_ingredient = Label(liste_ingredients_frame, text = liste_ingredients[-1])
    nouvel_ingredient.pack()
    ingredient= Entry(ingredients_frame)
    ingredient.pack()

def ajouter_recette_from_champ():
    """
    Ajoute une recette à la base de données à partir des champs de l'interface graphique.
    """
    groupe = choix_groupe.get()
    liste_groupe = extraire_groupes()
    if groupe not in liste_groupe :
        ajouter_groupe(groupe)
    nouvelle_recette = recette(name.get(),liste_ingredients, groupe, choix_saison.get(), notes.get())
    nouvelle_recette.ajouter()
    retour_accueil_from_ajout()
    aller_vers_ajout()

def jours_semaine(ajd):
    jour = ajd.weekday()
    print(f"jour = {ajd.day}/{ajd.month}")
    print(f"jour de la semaine = {jour}")
    dif = jour - 1 #
    print(f"dif' = {dif}")
    jour1 = ajd-datetime.timedelta(days = dif)
    print(f"mardi {jour1.day}/{ jour1.month}")
    jour7 = ajd+datetime.timedelta(days = (6-dif))
    print(f"lundi {jour7.day}/{ jour7.month}")
    return jour1,jour7

#ACTIONS
def associer_interface_bd_semaine():
    global jour_en_cours
    ajd = datetime.date.today()
    if jour_en_cours < jours_semaine(ajd)[0] :
        if jour_en_cours < jours_semaine(ajd - datetime.timedelta(weeks = 1))[0]:
            fichier_semaines = open('semaine-2','r')
            print("-2")
        else :
            fichier_semaines = open('semaine-1','r')
            print("-1")
    elif jour_en_cours > jours_semaine(ajd)[1] :
        if jour_en_cours > jours_semaine(ajd + datetime.timedelta(weeks = 1))[1]:
            fichier_semaines = open('semaine+2','r')
            print("+2")
        else:
            fichier_semaines = open('semaine+1','r')
            print("+1")
    else:
        fichier_semaines = open('semaine0','r')
        print("0")
    global jour1_midi
    liste_groupes = extraire_groupes()
    liste_recettes = extraire_recettes()
    liste_noms_recettes = titres_toutes_recettes(liste_recettes)
    
    liste_semaines = fichier_semaines.read()
    liste_semaines = liste_semaines.split('\n')
    for i in range(len(liste_semaines)-1):
        liste_semaines[i] = liste_semaines[i].split(";")
    fichier_semaines.close()
    #associer nom de chaque menu à son numero dans la liste des titres de recettes
    #associer chaque catégorie à son numéro dans la liste des groupes
    liste_semaines_num = [[],[],[],[],[],[],[]]
    liste_categories_num = [[],[],[],[],[],[],[]]
    for i in range(7):
        for j in range(2):
            jour = liste_semaines[i]
            indice = liste_noms_recettes.index(jour[j])
            liste_semaines_num[i].append(indice)
            liste_categories_num[i].append(liste_groupes.index(liste_recettes[indice].groupe))
    #midi
    jour1_midi.current(liste_semaines_num[0][0])
    jour1_midi_categorie.current(liste_categories_num[0][0])
    jour2_midi.current(liste_semaines_num[1][0])
    jour2_midi_categorie.current(liste_categories_num[1][0])
    jour3_midi.current(liste_semaines_num[2][0])
    jour3_midi_categorie.current(liste_categories_num[2][0])
    jour4_midi.current(liste_semaines_num[3][0])
    jour4_midi_categorie.current(liste_categories_num[3][0])
    jour5_midi.current(liste_semaines_num[4][0])
    jour5_midi_categorie.current(liste_categories_num[4][0])
    jour6_midi.current(liste_semaines_num[5][0])
    jour6_midi_categorie.current(liste_categories_num[5][0])
    jour7_midi.current(liste_semaines_num[6][0])
    jour7_midi_categorie.current(liste_categories_num[6][0])
    #soir
    jour1_soir.current(liste_semaines_num[0][1])
    jour1_soir_categorie.current(liste_categories_num[0][1])
    jour2_soir.current(liste_semaines_num[1][1])
    jour2_soir_categorie.current(liste_categories_num[1][1])
    jour3_soir.current(liste_semaines_num[2][1])
    jour3_soir_categorie.current(liste_categories_num[2][1])
    jour4_soir.current(liste_semaines_num[3][1])
    jour4_soir_categorie.current(liste_categories_num[3][1])
    jour5_soir.current(liste_semaines_num[4][1])
    jour5_soir_categorie.current(liste_categories_num[4][1])
    jour6_soir.current(liste_semaines_num[5][1])
    jour6_soir_categorie.current(liste_categories_num[5][1])
    jour7_soir.current(liste_semaines_num[6][1])
    jour7_soir_categorie.current(liste_categories_num[6][1])



def generer_semaine():
    #recuperer saison
    #liste_repas liste des recettes de cette saison
    #recuperer liste des repas deux semaines dernieres
    #enlever repas de la semaine derniere dans liste_repas
    for i in range(7):
        for j in range(2):
            #recuperer categorie du repas
            # si repas categorie(repas actuel)
            pass

def semaine_prec():
    global jour_en_cours
    jour_en_cours = jour_en_cours - datetime.timedelta(days= 7)
    print(f"jour = {jour_en_cours.day}/{jour_en_cours.month}")
    associer_interface_bd_semaine()

def semaine_suiv():
    global jour_en_cours
    jour_en_cours = jour_en_cours + datetime.timedelta(days=7)
    print(f"jour = {jour_en_cours.day}/{jour_en_cours.month}")
    associer_interface_bd_semaine()

#-----------------------------------------FONCTIONS D'AFFICHAGE----------------------------------


def aller_vers_ajout():
    ajout.pack(padx=10,pady=10)
    accueil.pack_forget()

def aller_vers_agenda():
    global liste_menus, jour1_midi, jour2_midi,jour3_midi,jour4_midi,jour5_midi,jour6_midi,jour7_midi, jour1_midi_categorie,jour2_midi_categorie,jour3_midi_categorie,jour4_midi_categorie,jour5_midi_categorie,jour6_midi_categorie,jour7_midi_categorie, jour1_soir, jour2_soir,jour3_soir,jour4_soir,jour5_soir,jour6_soir,jour7_soir, jour1_soir_categorie,jour2_soir_categorie,jour3_soir_categorie,jour4_soir_categorie,jour5_soir_categorie,jour6_soir_categorie,jour7_soir_categorie
    liste_menus = titres_toutes_recettes(extraire_recettes())
    jour1_midi.destroy()
    jour2_midi.destroy()
    jour3_midi.destroy()
    jour4_midi.destroy()
    jour5_midi.destroy()
    jour6_midi.destroy()
    jour7_midi.destroy()
    jour1_midi = Combobox(jour1_frame, values=liste_menus)
    jour1_midi.pack()
    jour2_midi = Combobox(jour2_frame, values=liste_menus)
    jour2_midi.pack()
    jour3_midi = Combobox(jour3_frame, values=liste_menus)
    jour3_midi.pack()
    jour4_midi = Combobox(jour4_frame, values=liste_menus)
    jour4_midi.pack()
    jour5_midi = Combobox(jour5_frame, values=liste_menus)
    jour5_midi.pack()
    jour6_midi = Combobox(jour6_frame, values=liste_menus)
    jour6_midi.pack()
    jour7_midi = Combobox(jour7_frame, values=liste_menus)
    jour7_midi.pack()
    jour1_midi_categorie.destroy()
    jour2_midi_categorie.destroy()
    jour3_midi_categorie.destroy()
    jour4_midi_categorie.destroy()
    jour5_midi_categorie.destroy()
    jour6_midi_categorie.destroy()
    jour7_midi_categorie.destroy()
    jour1_midi_categorie = Combobox(jour1_frame, values=liste_categories)
    jour1_midi_categorie.pack()
    jour2_midi_categorie = Combobox(jour2_frame, values=liste_categories)
    jour2_midi_categorie.pack()
    jour3_midi_categorie = Combobox(jour3_frame, values=liste_categories)
    jour3_midi_categorie.pack()
    jour4_midi_categorie = Combobox(jour4_frame, values=liste_categories)
    jour4_midi_categorie.pack()
    jour5_midi_categorie = Combobox(jour5_frame, values=liste_categories)
    jour5_midi_categorie.pack()
    jour6_midi_categorie = Combobox(jour6_frame, values=liste_categories)
    jour6_midi_categorie.pack()
    jour7_midi_categorie = Combobox(jour7_frame, values=liste_categories)
    jour7_midi_categorie.pack()
    jour1_soir.destroy()
    jour2_soir.destroy()
    jour3_soir.destroy()
    jour4_soir.destroy()
    jour5_soir.destroy()
    jour6_soir.destroy()
    jour7_soir.destroy()
    jour1_soir = Combobox(jour1_frame, values=liste_menus)
    jour1_soir.pack()
    jour2_soir = Combobox(jour2_frame, values=liste_menus)
    jour2_soir.pack()
    jour3_soir = Combobox(jour3_frame, values=liste_menus)
    jour3_soir.pack()
    jour4_soir = Combobox(jour4_frame, values=liste_menus)
    jour4_soir.pack()
    jour5_soir = Combobox(jour5_frame, values=liste_menus)
    jour5_soir.pack()
    jour6_soir = Combobox(jour6_frame, values=liste_menus)
    jour6_soir.pack()
    jour7_soir = Combobox(jour7_frame, values=liste_menus)
    jour7_soir.pack()
    jour1_soir_categorie.destroy()
    jour2_soir_categorie.destroy()
    jour3_soir_categorie.destroy()
    jour4_soir_categorie.destroy()
    jour5_soir_categorie.destroy()
    jour6_soir_categorie.destroy()
    jour7_soir_categorie.destroy()
    jour1_soir_categorie = Combobox(jour1_frame, values=liste_categories)
    jour1_soir_categorie.pack()
    jour2_soir_categorie = Combobox(jour2_frame, values=liste_categories)
    jour2_soir_categorie.pack()
    jour3_soir_categorie = Combobox(jour3_frame, values=liste_categories)
    jour3_soir_categorie.pack()
    jour4_soir_categorie = Combobox(jour4_frame, values=liste_categories)
    jour4_soir_categorie.pack()
    jour5_soir_categorie = Combobox(jour5_frame, values=liste_categories)
    jour5_soir_categorie.pack()
    jour6_soir_categorie = Combobox(jour6_frame, values=liste_categories)
    jour6_soir_categorie.pack()
    jour7_soir_categorie = Combobox(jour7_frame, values=liste_categories)
    jour7_soir_categorie.pack()
    agenda.pack(padx=10,pady=10)
    accueil.pack_forget()
    associer_interface_bd_semaine()

def retour_accueil_from_ajout():
    global liste_ingredients_frame, name, ingredient, choix_groupe, choix_saison, notes
    #name
    name.destroy()
    name = Entry(name_frame)
    name.pack()
    #ingredients
    liste_ingredients_frame.destroy()
    liste_ingredients_frame = Frame(ingredients_frame,borderwidth=2,relief=GROOVE)
    liste_ingredients_frame.pack()
    ingredient.destroy()
    ingredient = Entry(ingredients_frame)
    ingredient.pack()
    #groupes
    choix_groupe.destroy()
    choix_groupe = Combobox(groupe_frame, values=extraire_groupes())
    choix_groupe.current(0)
    choix_groupe.pack()
    ajout.pack_forget()
    accueil.pack()
    #saison
    choix_saison.current(0)
    #notes
    notes.destroy()
    notes = Entry(notes_frame)
    notes.pack()
    #big frames
    ajout.pack_forget()
    accueil.pack()

def retour_accueil_from_agenda():
    agenda.pack_forget()
    accueil.pack()



    
window = Tk()
window.geometry("1470x600")
window.title("MENUS")
window.configure(bg = "lightyellow")

label = Label(window, text="Hello Tk")
label.pack()

#page d'accueil
accueil = Frame(window,borderwidth=2,relief=GROOVE)
accueil.pack(padx=10,pady=10)

ajouter = Button(accueil, text="Ajouter nouvelle recette", command = lambda : aller_vers_ajout())
ajouter.pack()

vers_semaine = Button(accueil, text="Accès à l'agenda", command= lambda : aller_vers_agenda())
vers_semaine.pack()

#PAGE D'AJOUT
ajout = Frame(window,borderwidth=2,relief=GROOVE)

#nom
name_frame = Frame(ajout,borderwidth=2,relief=GROOVE, bg='#500')
name_frame.pack()
label_nom = Label(name_frame,text = "Nom de la recette :", bg='#500', foreground='white')
label_nom.pack()
name = Entry(name_frame)
name.pack()

#ingredients
ingredients_frame = Frame(ajout)
ingredients_frame.pack()
ingredients_label = Label(ingredients_frame, text = "Ingredients :")
ingredients_label.pack()
liste_ingredients_frame = Frame(ingredients_frame,borderwidth=2,relief=GROOVE )
liste_ingredients_frame.pack()
ingredient= Entry(ingredients_frame)
ingredient.pack()
ajout_ingredients = Button(ingredients_frame, text = "Ajouter ingrédient", command = lambda : ajouter_ingredients_ajout())
ajout_ingredients.pack(side = "bottom")

#groupe
groupe_frame = Frame(ajout)
groupe_frame.pack()
groupe_label = Label(groupe_frame, text = "Moment de la semaine préféré :")
groupe_label.pack()
choix_groupe = Combobox(groupe_frame, values=extraire_groupes())
choix_groupe.current(0)
choix_groupe.pack()

#saison
saison_frame = Frame(ajout)
saison_frame.pack()
saison_label = Label(saison_frame, text = "Moment de l'année préféré :")
saison_label.pack()
choix_saison = Combobox(saison_frame, values=liste_saison)
choix_saison.current(0)
choix_saison.pack()

#notes
notes_frame = Frame(ajout)
notes_frame.pack()
label_notes = Label(notes_frame,text = "Commentaires : ")
label_notes.pack()
notes = Entry(notes_frame)
notes.pack(ipady=100)

#footer
valider_recette = Button(ajout,text = "Valider", command = lambda : ajouter_recette_from_champ())
valider_recette.pack(side = "bottom")

retour_ajout = Button(ajout,text="Retour a l'accueil", command = lambda : retour_accueil_from_ajout())
retour_ajout.pack(side = "bottom")

#PAGE D'AGENDA
jours = ["Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche","Lundi"]
agenda = Frame(window,borderwidth=2,relief=GROOVE)
liste_menus = titres_toutes_recettes(extraire_recettes())
liste_categories = extraire_groupes()
photo_droite = PhotoImage(file = r"droite.png") 
photo_droite = photo_droite.subsample(15,15)
photo_gauche = PhotoImage(file = r"gauche.png")
photo_gauche = photo_gauche.subsample(15,15)

#header
header = Frame(agenda)
header.pack()
jour_en_cours = datetime.date.today()
fleche_gauche = Button(header, image = photo_gauche, command = lambda: semaine_prec())
fleche_droite = Button(header, image = photo_droite, command = lambda: semaine_suiv())
fleche_droite.pack(side="right")
fleche_gauche.pack(side="left")



titre_agenda = Label(header, text = "Menus de la semaine du")
titre_agenda.pack(side="top")
choix_saison_label = Label(header, text = "Choix de la saison")
choix_saison_label.pack(side = "left")
choix_saison = Combobox(header,values = liste_saison )
choix_saison.pack(side = "left")


#calendrier
semaine_frame = Frame(agenda)
semaine_frame.pack(pady=20)
#creation frames jours
heure = Frame(semaine_frame, borderwidth=1, relief=SOLID)
heure.pack(side = 'left', ipadx = "20")
jour1_frame = Frame(semaine_frame, borderwidth=1, relief=SOLID)
jour1_frame.pack(side = "left", ipadx="20")
jour2_frame = Frame(semaine_frame, borderwidth=1, relief=SOLID)
jour2_frame.pack(side = "left", ipadx="20")
jour3_frame = Frame(semaine_frame, borderwidth=1, relief=SOLID)
jour3_frame.pack(side = "left", ipadx = "20")
jour4_frame = Frame(semaine_frame, borderwidth=1, relief=SOLID)
jour4_frame.pack(side = "left", ipadx = "20")
jour5_frame = Frame(semaine_frame, borderwidth=1, relief=SOLID)
jour5_frame.pack(side = "left", ipadx = "20")
jour6_frame = Frame(semaine_frame, borderwidth=1, relief=SOLID)
jour6_frame.pack(side = "left", ipadx = "20")
jour7_frame = Frame(semaine_frame, borderwidth=1, relief=SOLID)
jour7_frame.pack(side = "left", ipadx = "20")
# ligne noms des jours
titre_heure = Label(heure, text="Repas", fg="#eee")
titre_heure.pack()
jour1_nom = Label(jour1_frame, text=jours[0])
jour1_nom.pack()
jour2_nom = Label(jour2_frame, text=jours[1])
jour2_nom.pack()
jour3_nom = Label(jour3_frame, text=jours[2])
jour3_nom.pack()
jour4_nom = Label(jour4_frame, text=jours[3])
jour4_nom.pack()
jour5_nom = Label(jour5_frame, text=jours[4])
jour5_nom.pack()
jour6_nom = Label(jour6_frame, text=jours[5])
jour6_nom.pack()
jour7_nom = Label(jour7_frame, text=jours[6])
jour7_nom.pack()
#ligne midi a la maison
heure_midi = Label(heure, text="Midi")
heure_midi.pack()
jour1_midi = Combobox(jour1_frame, values=liste_menus)
jour1_midi.pack()
jour2_midi = Combobox(jour2_frame, values=liste_menus)
jour2_midi.pack()
jour3_midi = Combobox(jour3_frame, values=liste_menus)
jour3_midi.pack()
jour4_midi = Combobox(jour4_frame, values=liste_menus)
jour4_midi.pack()
jour5_midi = Combobox(jour5_frame, values=liste_menus)
jour5_midi.pack()
jour6_midi = Combobox(jour6_frame, values=liste_menus)
jour6_midi.pack()
jour7_midi = Combobox(jour7_frame, values=liste_menus)
jour7_midi.pack()
#categorie midi
categorie_midi = Label(heure, text="Catégorie du midi")
categorie_midi.pack()
jour1_midi_categorie = Combobox(jour1_frame, values=liste_categories)
jour1_midi_categorie.pack()
jour2_midi_categorie = Combobox(jour2_frame, values=liste_categories)
jour2_midi_categorie.pack()
jour3_midi_categorie = Combobox(jour3_frame, values=liste_categories)
jour3_midi_categorie.pack()
jour4_midi_categorie = Combobox(jour4_frame, values=liste_categories)
jour4_midi_categorie.pack()
jour5_midi_categorie = Combobox(jour5_frame, values=liste_categories)
jour5_midi_categorie.pack()
jour6_midi_categorie = Combobox(jour6_frame, values=liste_categories)
jour6_midi_categorie.pack()
jour7_midi_categorie = Combobox(jour7_frame, values=liste_categories)
jour7_midi_categorie.pack()

#ligne soir
heure_soir = Label(heure, text="Soir")
heure_soir.pack()
jour1_soir = Combobox(jour1_frame, values=liste_menus)
jour1_soir.pack()
jour2_soir = Combobox(jour2_frame, values=liste_menus)
jour2_soir.pack()
jour3_soir = Combobox(jour3_frame, values=liste_menus)
jour3_soir.pack()
jour4_soir = Combobox(jour4_frame, values=liste_menus)
jour4_soir.pack()
jour5_soir = Combobox(jour5_frame, values=liste_menus)
jour5_soir.pack()
jour6_soir = Combobox(jour6_frame, values=liste_menus)
jour6_soir.pack()
jour7_soir = Combobox(jour7_frame, values=liste_menus)
jour7_soir.pack()
#categorie soir
categorie_soir = Label(heure, text="Catégorie du midi")
categorie_soir.pack()
jour1_soir_categorie = Combobox(jour1_frame, values=liste_categories)
jour1_soir_categorie.pack()
jour2_soir_categorie = Combobox(jour2_frame, values=liste_categories)
jour2_soir_categorie.pack()
jour3_soir_categorie = Combobox(jour3_frame, values=liste_categories)
jour3_soir_categorie.pack()
jour4_soir_categorie = Combobox(jour4_frame, values=liste_categories)
jour4_soir_categorie.pack()
jour5_soir_categorie = Combobox(jour5_frame, values=liste_categories)
jour5_soir_categorie.pack()
jour6_soir_categorie = Combobox(jour6_frame, values=liste_categories)
jour6_soir_categorie.pack()
jour7_soir_categorie = Combobox(jour7_frame, values=liste_categories)
jour7_soir_categorie.pack()

associer_interface_bd_semaine()

#footer
associer = Button(agenda, text = "Associer",command = lambda : associer_interface_bd_semaine())
associer.pack()
generer = Button(agenda, text="Générer une semaine de menus", command=lambda:generer_semaine())
generer.pack()
retour_agenda = Button(agenda,text="Retour a l'accueil", command = lambda : retour_accueil_from_agenda())
retour_agenda.pack(side = "bottom")


window.mainloop()