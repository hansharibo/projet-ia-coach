# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import gestionutilisateur as gu
import lecturefichier as lf
import programmecreator as pc
import analyseur as an

def recognise_emotion(user):
     
     dicomal ="dico/dicotestmal.dico"
     dicosupmal ="dico/dicomalnew.dico"
     dicobien = "dico/dicotestbien.dico"
     dicosupbien = "dico/dicobiennew.dico"
     choix = -1
     while(1):
          
          print("comment allez vous ?")
          text = input("réponse :")
          if text == "quit":
               break
          elif text =="!":
               if choix == 1 :
                    with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                         with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                              for i in reponse:
                                   save.write(i)
                                   save.write(" ")
               elif choix == 2 :
                    with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                         with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                              for i in reponse:
                                   save.write(i)
                                   save.write(" ")
               elif choix == -1 :
                    print("nous ne pouvons traitez une requète sans l'avoir traite")
               else:
                    while choix != 'n' and choix != 'N' and choix != 'P' and choix != 'p':
                         print("la réponse et (n)égative ou (p)ositive ?")
                         choix = input(":>")
                    if choix == 'n' or choix == 'N':
                         print("nous sommes désolé pour la gène occasionnée")
                         with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                              with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                                   for i in reponse:
                                        save.write(i)
                                        save.write(" ")
                         print("essayons de comprendre ce qu'il n'allait pas...")
                    else:
                         with open('dossierteste/dossier bien.txt', 'a',encoding='utf-8') as save:
                              with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                                   for i in reponse:
                                        save.write(i)
                                        save.write(" ")
               choix = -1
          else :     
               if choix == 2 :
                    with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                         with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                              for i in reponse:
                                   save.write(i)
                                   save.write(" ")
               elif choix == 1 :
                    with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                         with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                              for i in reponse:
                                   save.write(i)
                                   save.write(" ")         
               with open("buffer/reponseutilisateur.rp", "w", encoding='utf-8') as fichier :
                    fichier.write(text)
               print(lf.classeur("buffer/reponseutilisateur.rp", dicomal))
               print(lf.classeur("buffer/reponseutilisateur.rp", dicosupmal))
               print(lf.classeur("buffer/reponseutilisateur.rp", dicobien))
               print(lf.classeur("buffer/reponseutilisateur.rp", dicosupbien))
               if lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal)> lf.classeur("buffer/reponseutilisateur.rp", dicobien) + lf.classeur("buffer/reponseutilisateur.rp", dicosupbien):
                    print("ne vous inquiétez pas, " + str(user) + " je suis la pour vous écouter... n'hesitez pas je ne suis peut-être pas le meilleur mais je peux vous écouter")
                    choix = 2
               elif lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal) < lf.classeur("buffer/reponseutilisateur.rp", dicobien) + lf.classeur("buffer/reponseutilisateur.rp", dicosupbien):
                    print("c'est une bonne nouvelle " + str(user) + " je suis heureux de l'apprendre qu'avez d'autres a me dire ?")
                    choix = 1
               else:
                    choix = 3
                    print("mmmh...interressant avez vous d'autres chose ?")

def doweneedtorecalculateeverything(): #programme pour savoir combien de fois le programme a été lancé
     nb_ouverture = 0
     try:
          with open("buffer/numberoftimethisprogramwasopen.txt", "r",encoding='utf-8') as file:
               for number in file:
                    nb_ouverture = int(number)
     except:
          with open("buffer/numberoftimethisprogramwasopen.txt", "w", encoding='utf-8') as number:
               number.write("1")
     if nb_ouverture == 0 :
          return
     print(nb_ouverture)
     if nb_ouverture == 10:
          nb_ouverture = 0
          an.newmoy()
          an.dicocreate("dossierteste/dossier bien.txt","dicotestbien")
          an.dicocreate("dossierteste/dossier pas bien.txt", "dicotestmal")
          an.comparateurdedico("dico/dicotestbien.dico", "dico/dicotestmal.dico","dicomal")
          an.comparateurdedico("dico/dicotestmal.dico", "dico/dicotestbien.dico","dicobien")
          an.dicocreate("dossierteste/dossiertestniveaudebutant.txt","dicotestniveaudebutant")
          an.dicocreate("dossierteste/dossiertestniveauintermédiaire.txt","dicotestIAIntermediaire")
          an.dicocreate("dossierteste/dossiertesteniveauavancé.txt","dicotestIAAvancé")
     else:     
          nb_ouverture+= 1
     with open("buffer/numberoftimethisprogramwasopen.txt", "w", encoding='utf-8') as file_writer:
          file_writer.write(str(nb_ouverture))
     return
     

def menu(user):#programme qui permet d'avoir le menu pour les utilisateurs
     user = "utilisateur/" + user +'.ut'
     while (1):
          print ("option possible: (E)ntrainement - (R)etour utilisateur - (Q)uit - (T)utoriel")
          choix = input(":>")
          if choix == 'q' or choix == 'Q':
               break
          elif choix == 'E' or choix == 'e':
               print("étant donné que votre niveau est ", lf.mattostring(lf.chercherinfo("niveau",user)))
               print("nous vous avons concocté le programme suivant pour la semaine:")
               print("nous allons commencer par :", lf.mattostring(lf.chercherinfo("entrainement", user)))
               print("ensuite, vous allez faire :", lf.mattostring(lf.chercherinfo("exercice", user)))
               print("enfin, vous terminerez par:", lf.mattostring(lf.chercherinfo("final", user)))
          elif choix == 'T' or choix == 't':
               pc.tutoriel()
          elif choix == 'r' or choix == 'R':
               gu.avisutilisateur(user)
          else :
               print("commande non reconnue ou non implémantée")


logo = open("logo.logo","r", encoding='utf-8')
print(logo.read())
fileuser ="utilisateur.ut"
dicomal ="dico/dicotestmal.dico"
dicosupmal ="dico/dicomalnew.dico"
dicobien = "dico/dicotestbien.dico"
dicosupbien = "dico/dicobiennew.dico"
print("comment allez vous ?")
text = input("réponse :")
with open("buffer/reponseutilisateur.rp", "w", encoding='utf-8') as fichier :
     fichier.write(text)
print(lf.classeur("buffer/reponseutilisateur.rp", dicomal))
print(lf.classeur("buffer/reponseutilisateur.rp", dicosupmal))
print(lf.classeur("buffer/reponseutilisateur.rp", dicobien))
print(lf.classeur("buffer/reponseutilisateur.rp", dicosupbien))
if lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal)> lf.classeur("buffer/reponseutilisateur.rp", dicobien) + lf.classeur("buffer/reponseutilisateur.rp", dicosupbien):
     print("ne vous inquiétez pas un peu de sport vous fera oublier vos problèmes")
elif lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal) < lf.classeur("buffer/reponseutilisateur.rp", dicobien) + lf.classeur("buffer/reponseutilisateur.rp", dicosupbien):
     print("parfait vous voilà d'attaque pour une merveilleuse séance de sport")
else:
     print("il semblerait que vos émotions ne vous submerge pas, en espérant que vous ressentirez quelque chose au cours cette nouvelle session")
nomutilisateur = input("veuillez rentrer votre nom: ")
isitarealuser = gu.lookingforexistinguser(nomutilisateur)
if isitarealuser == False:
    print("vous n'existez pas dans notre base de données")
    print("nous allons créer votre profil")
    gu.createnewuser()
else :
    print("bienvenu ", nomutilisateur)
    #decommenter la ligne d'après si vous voulez avoir accès au programme d'origine
    #menu(nomutilisateur)
    recognise_emotion(nomutilisateur)
    print("merci d'avoir utilisé le Z.E.U.S. pour manager vos session de sport")
an.newmoy()
an.dicocreate("dossierteste/dossier bien.txt","dicotestbien")
an.dicocreate("dossierteste/dossier pas bien.txt", "dicotestmal")
an.comparateurdedico("dico/dicotestbien.dico", "dico/dicotestmal.dico","dicomal")
an.comparateurdedico("dico/dicotestmal.dico", "dico/dicotestbien.dico","dicobien")
an.dicocreate("dossierteste/dossiertestniveaudebutant.txt","dicotestniveaudebutant")
an.dicocreate("dossierteste/dossiertestniveauintermédiaire.txt","dicotestIAIntermediaire")
an.dicocreate("dossierteste/dossiertesteniveauavancé.txt","dicotestIAAvancé")
doweneedtorecalculateeverything()
