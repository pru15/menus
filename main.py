# utf 8
import unidecode


class recette:
    """
    une recette consiste en un nom 'name', une liste d'ingrédients, un groupe ("midi_famille", "midi_semaine", "soir_famille", 
    "accompagnement_barbecue",...), une saison et d'éventuels commentaires.
    """
    def __init__(self, name, ingredients = [], groupe = "midi_semaine", saison = [], notes = None, ):
        self.name = name
        self.ingredients = ingredients
        self.groupe = groupe
        self.saison = saison
        self.notes = notes

    def afficher(self):
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
        s = input("Cette recette est-elle adaptée pour une saison en particulier ? Si oui, laquelle ? écrivez 'non' ou seulement la saison concernée, en minuscule et sans accent(s): ")
        while s != 'non':
            while s != 'non' and s != 'ete' and s != 'hiver' and s != 'automne' and s !='printemps':
                s = input("Il y a eu une erreur. S'il vous plaît, vérifiez l'orthographe, les minuscules et les accents. Ré-écrivez votre réponse : ")        
            if s != 'non':
                self.saison.append(s)
                s = input("Cette recette est-elle adaptée pour une saison en particulier ? Si oui, laquelle ? écrivez 'non' ou seulement la saison concernée, en minuscule et sans accent(s): ")

    def modifier_groupe(self):
        groupe = input("A quelle occasion dégustez-vous ce plat ? (midi_famille, midi_semaine, soir, soir_wk, )")
        

    def ajouter_notes(self):
        notes = input("Souhaitez vous ajouter des commentaires ? Sinon, faites simplement entrée. \n")
        self.notes = notes

    def supprimer_ingredients(self):
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
        liste_recettes = extraire_recettes()
        if self.name in liste_recettes :
            print("Cette recette existe déjà ou alors une autre recette porte le même. Elle ne sera pas ajoutée.")
        else :
            fichier_recettes = open('recettes','a')
            fichier_recettes.write(f"{self.name};{self.ingredients};{self.saison};{self.notes}\n")
            fichier_recettes.close()
        
def extraire_recettes():
    fichier_recettes = open('recettes','r')
    liste_recettes = fichier_recettes.read()
    liste_recettes = liste_recettes.split('\n')
    liste_recettes_objets = []
    for i in range(len(liste_recettes)-1):
        liste_recettes[i] = liste_recettes[i].split(";")
        liste_recettes_objets.append(recette(liste_recettes[i][0],eval(liste_recettes[i][1]),liste_recettes[i][2],liste_recettes[i][3]))
    fichier_recettes.close()
    return liste_recettes_objets

def trier_recettes_saison(liste_recettes, saison):
    liste_recettes_saison = []
    for recette in liste_recettes:
        if saison in recette.saison :
            liste_recettes_saison.append(recette)
    return liste_recettes_saison

def cherche_recette(nom, liste):
    for recette in liste:
        if recette.name.upper() == unidecode.unidecode(nom.upper()):
            return recette
    
def titres_toutes_recettes(liste):
    titres = ""
    for recette in liste:
        titres += '\n -' + recette.name
    return titres





def main():
    while True :
        rep = input("Pour ajouter une nouvelle recette, tapez 'A'.\nPour modifier une recette, tapez 'M'.\nPour générer une semaine de menus, tapez 'S'.\n")
        rep = rep.upper()
        if rep == 'A':
            #NOUVELLE RECETTE
            name = input("Quel est le nom de la recette ? ")
            nouvelle_recette = recette(unidecode.unidecode(name))
            nouvelle_recette.ajouter_ingredients()
            nouvelle_recette.modifier_saison()
            nouvelle_recette.ajouter_notes()
            print("Voici votre nouvelle recette :")
            nouvelle_recette.afficher()
            nouvelle_recette.ajouter()
        if rep == 'M':
            #TROUVER LA RECETTE
            recettes = extraire_recettes()
            question = "Voici la liste de toutes vos recettes : (bon courage)"  + titres_toutes_recettes(recettes) + "\nQuelle recette voulez-vous modifier ?"
            recette_modif = input(question)
            recette_modif = cherche_recette(recette_modif, recettes)
            recette_modif.afficher()
            #MODIFIER
            modif = input("Tapez 'A' pour ajouter un ingrédient, 'S' pour en supprimer un, 'N' pour modifier le nom de la recette. Sinon, faites entrée : ")
            modif = modif.upper()
            while modif != 'A' and modif != 'S' and modif != 'N' and modif != 'D' and modif != '':
                modif = input("Il y a eu une erreur. Tapez à nouveau la lettre :  ")
            if modif == 'A':
                recette_modif.ajouter_ingredients()
            elif modif == 'S':
                recette_modif.supprimer_ingredients()
            elif modif == 'N':
                name = input("Quel est le nom de la recette ? ")
                recette_modif.name = name
            else :
                pass
        elif rep == 'S':
            pass

main()



        
    