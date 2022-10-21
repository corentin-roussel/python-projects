def length(b):
    a=0
    for i in b:
        a+=1
    return a
    
#import fonction random
import random

#ouvrir le dictionnaire et trouver un mot aléatoire dans la liste
with open("dico_france.txt", "r", encoding="iso8859_15") as dico:
     dicoList = dico.read()


#établissement variable 
dicoSplit= dicoList.split()
mots = random.choice(dicoSplit)
longueurMot =len(mots)
listeMots=list(mots)

#création d'une liste de vide pour les inputs
emptyInput=[]

#création d'une liste vide qui remplace les lettres sélectionnées en underscore
underscoreList =[]
for letters in mots:
    underscoreList += '_'

#input la difficulté choisis le nombre de vies
difficulté = input("Quelle difficulté voulez vous choisir (Débutant, Intermédiaire, Expert) ? ")

#if elif pour choisir le nombre d'hp
if difficulté == "Débutant":
    hp = 10
    print("Vous avez",hp ,"de vies")
elif difficulté == "Intermédiaire":
    hp = 7
    print("Vous avez",hp ,"de vies")
elif difficulté == "Expert":
    hp = 4
    print("Vous avez",hp ,"de vies")
elif difficulté != "Débutant" or "Expert" or "Intermédiaire":
    difficulté = input(("Vérifier la syntaxe de votre difficulté choisissez (Débutant, Intermédiaire, Expert)"))
    exit()
#boucle while tant que true continue
end_game = True
while end_game:
    
#print le mot en underscore et implémentation de l'input
    print(' '.join(underscoreList))
    m = input("Entrer une lettre : ")
#si input dans liste de mots do else
    if m in listeMots:     
        #boucle for variable x qui récupere l'index de la variabel longueurMot
        for x in range(longueurMot):
            #if listeMots index == m (input)
            if listeMots[x] == m:
                #underscoreList remplace l'underscore par l'input
                underscoreList[x] = m
                #récupére les lettres déja utilisé 
                emptyInput.append(m)
                print(' '.join(underscoreList))
                print("Voici les lettres déjâ utilisé : ",emptyInput)
                
    #décrementation des hp et ajout des lettres déja utilisés
    else:
        emptyInput.append(m)
        print("Voici les lettres déjâ utilisé : ",emptyInput)
        hp -=1
        print("Il vous reste",hp, "vie")
        
    #if le mot est complété finit le jeu
    if underscoreList == listeMots:
        end_game = False
        print("Félicitations vous avez gagné le mot était", mots)
    
#tant que les hp sont inférieur ou = a 0 termine le jeu
    if hp <= 0:
        end_game = False
        print("Désolé vous avez perdu le mot était", mots)