from selenium import webdriver
import csv
import time

# On récupère le prénom de la personne qui veut générer l'attestation
prenom = input ('qui es tu ? ')
prenom = prenom.lower()
# On récupère le motif de déplacement voulu
motif = input('Motif de déplacement ? : travail/courses/santé/famille/sport/judiciaire/missions : ')
prenom_trouve = 'a'
x = 0

#récupération du motif de déplacement
xpath_motif = ''

if motif.lower() == 'travail' : 
    xpath_motif = '//*[@id="checkbox-travail"]'
if motif.lower() == 'courses' : 
    xpath_motif = '//*[@id="checkbox-courses"]'
if motif.lower() == 'santé' : 
    xpath_motif = '//*[@id="checkbox-sante"]'
if motif.lower() == 'famille' : 
    xpath_motif = '//*[@id="checkbox-famille"]'
if motif.lower() == 'sport' : 
    xpath_motif = '//*[@id="checkbox-sport"]'
if motif.lower() == 'judiciaire' : 
    xpath_motif = '//*[@id="checkbox-judiciaire"]'
if motif.lower() == 'missions' : 
    xpath_motif = '//*[@id="checkbox-missions"]'
if motif.lower() == 'travail' :
    xpath_motif = '//*[@id="checkbox-travail"]'

if xpath_motif == '':
    print( "un tel motif n'est pas valable. Veuillez en choisir un dans la liste proposée .")

# Récupération de toutes les infos utilisateur. Si le nom n'est pas enregistré dans le fichier csv Base_attestation.csv alors il ne peut y avoir d'attestation
with open('Base_attestation.csv', 'r') as csvfile :
    
    while prenom.lower() != prenom_trouve.lower() : 
        ligne = csvfile.readline()
        prenom_trouve = ligne.split(',')[0]
        nom_trouve = ligne.split(',')[1]
        naissance_trouve = ligne.split(',')[2]
        lieu_naissance_trouve = ligne.split(',')[3]
        adresse_trouve = ligne.split(',')[4]
        ville_trouve = ligne.split(',')[5]
        code_postal_trouve = ligne.split(',')[6]
        x = x + 1
        if x == 12 : 
            print('Aucun utilisateur ne s appelle comme ça')
            break

# On met toutes les infos dans des variables
prenom = prenom_trouve
nom = nom_trouve
naissance = naissance_trouve
lieu_naissance = lieu_naissance_trouve
adresse = adresse_trouve
ville = ville_trouve
code_postal = code_postal_trouve

# Traitement de la demande d'attestation...
browser = webdriver.Chrome()
browser.get('https://media.interieur.gouv.fr/deplacement-covid-19/')

# recherche de toutes les zones à remplir
zone_prenom = browser.find_element_by_xpath('//*[@id="field-firstname"]')
zone_nom = browser.find_element_by_xpath('//*[@id="field-lastname"]')
zone_naissance = browser.find_element_by_xpath('//*[@id="field-birthday"]')
zone_lieu_naissance = browser.find_element_by_xpath('//*[@id="field-lieunaissance"]')
zone_adresse = browser.find_element_by_xpath('//*[@id="field-address"]')
zone_ville = browser.find_element_by_xpath('//*[@id="field-town"]')
zone_code_postal =browser.find_element_by_xpath('//*[@id="field-zipcode"]')
bouton_generer = browser.find_element_by_xpath('//*[@id="generate-btn"]')

# Rempli les champs avec les infos utilisateur
zone_prenom.send_keys(prenom)
zone_nom.send_keys(nom)
zone_naissance.send_keys(naissance)
zone_lieu_naissance.send_keys(lieu_naissance)
zone_adresse.send_keys(adresse)
zone_ville.send_keys(ville)
zone_code_postal.send_keys(code_postal)
browser.find_element_by_xpath(xpath_motif).click()
bouton_generer.click()

# Pour ouvrir le PDF téléchargé
time.sleep(2)
browser.get('file:///C:/Users/Downloads/')

# On trie l'affichage par odre de date
trier_date_modif = browser.find_element_by_xpath('//*[@id="dateColumnHeader"]')
trier_date_modif.click()

#On clique sur l'attestation
attestation = browser.find_element_by_partial_link_text('attestation')
attestation.click()

# L'attestation s'affiche !