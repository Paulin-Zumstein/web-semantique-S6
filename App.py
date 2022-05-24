from rdflib import Graph
import webbrowser


# Fonctions générales :
def getPrefix():
    return """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX onto: <http://www.semanticweb.org/fromages#>"""


def verificationFilter(inputKeyboard):
    if inputKeyboard == 'type':
        return 'Type'
    elif inputKeyboard == 'animal':
        return 'Animal'
    elif inputKeyboard == 'region':
        return 'Region'
    elif inputKeyboard == 'conception':
        return 'Conception'
    else:
        inputFilter = input("Choissisez entre type/animal/region/conception : ")
        return verificationFilter(inputFilter)


def verificationAnimal(inputKeyboard):
    if inputKeyboard == 'chevre':
        return 'Chevre'
    elif inputKeyboard == 'brebis':
        return 'Brebis'
    elif inputKeyboard == 'vache':
        return 'Vache'
    elif inputKeyboard == 'bufflone':
        return 'Bufflone'
    else:
        inputFilter = input("Choissisez entre chevre/brebis/vache/bufflone : ")
        return verificationAnimal(inputFilter)


def verificationType(inputKeyboard):
    if inputKeyboard == 'frais':
        return 'NosFrais'

    elif inputKeyboard == 'gras':
        return 'NosGras'

    elif inputKeyboard == 'pate molle croute fleurie':
        return 'NosPateMolleCrouteFleurie'

    elif inputKeyboard == 'pate molle croute lavee':
        return 'NosPateMolleCrouteLavee'

    elif inputKeyboard == 'pate persille':
        return 'NosPatePersille'

    elif inputKeyboard == 'pate presse et cuite':
        return 'NosPatePresseEtCuite'

    elif inputKeyboard == 'pate presse et non cuite':
        return 'NosPatePresseEtNonCuite'

    else:
        inputFilter = input(
            "Choissisez entre : \n-frais\n-gras\n-pate molle croute fleurie\n-pate molle croute lavee\n-pate persille"
            "\n-pate presse et cuite\n-pate presse et non cuite\n")
        return verificationType(inputFilter)


def verificationRegion(inputKeyboard):
    if inputKeyboard == 'AuvergneRhoneAlpes':
        return 'AuvergneRhoneAlpes'

    elif inputKeyboard == 'BourgogneFrancheComte':
        return 'BourgogneFrancheComte'

    elif inputKeyboard == 'Bretagne':
        return 'Bretagne'

    elif inputKeyboard == 'Corse':
        return 'Corse'

    elif inputKeyboard == 'GrandEst':
        return 'GrandEst'

    elif inputKeyboard == 'HautDeFrance':
        return 'HautDeFrance'

    elif inputKeyboard == 'Italie':
        return 'Italie'

    elif inputKeyboard == 'Nord':
        return 'Nord'

    elif inputKeyboard == 'Normandie':
        return 'Normandie'

    elif inputKeyboard == 'Occitanie':
        return 'Occitanie'

    elif inputKeyboard == 'PaysDeLaLoire':
        return 'PaysDeLaLoire'

    elif inputKeyboard == 'Pyrenees':
        return 'Pyrenees'

    elif inputKeyboard == 'Suisse':
        return 'Suisse'

    else:
        inputFilter = input(
            "Choissisez entre  :\n-AuvergneRhoneAlpes\n-BourgogneFrancheComte\n-Bretagne\n-Corse\n-GrandEst\n-HautDeFrance\n-Italie\n-Nord\n-Normandie\n-Occitanie\n-PaysDeLaLoire\n-Pyrenees\n-Suisse\n ")
        return verificationRegion(inputFilter)


def verificationConceptionFilter(inputKeyboard):
    if inputKeyboard == 'affinage':
        return 'hasForAffinage'
    elif inputKeyboard == 'pasteurisation':
        return 'hasForPasteurisation'
    elif inputKeyboard == 'salage':
        return 'hasForSalage'
    else:
        inputFilter = input("Choissisez entre affinage/pasteurisation/salage : ")
        return verificationConceptionFilter(inputFilter)


def verificationConceptionAffinage(inputKeyboard):
    if inputKeyboard == '1JourEtPlus':
        return '1JourEtPlus'
    elif inputKeyboard == '1MoisEtPlus':
        return '1MoisEtPlus'
    elif inputKeyboard == '5MoisEtPlus':
        return '5MoisEtPlus'
    elif inputKeyboard == 'SansAffinage':
        return 'SansAffinage'
    else:
        inputFilter = input("Choissisez entre : \n- 1JourEtPlus\n- 1MoisEtPlus\n- 5MoisEtPlus\n- SansAffinage\n")
        return verificationConceptionAffinage(inputFilter)


def verificationConceptionPasteurisation(inputKeyboard):
    if inputKeyboard == 'NonPasteurise':
        return 'NonPasteurise'
    elif inputKeyboard == 'PasteurisationVariable':
        return 'PasteurisationVariable'
    elif inputKeyboard == 'Pasteurise':
        return 'Pasteurise'
    else:
        inputFilter = input("Choissisez entre : \n -NonPasteurise\n -PasteurisationVariable\n -Pasteurise\n")
        return verificationConceptionPasteurisation(inputFilter)


def verificationConceptionSalage(inputKeyboard):
    if inputKeyboard == 'SalageASec':
        return 'SalageASec'
    elif inputKeyboard == 'SalageEnBainDeSaumure':
        return 'SalageEnBainDeSaumure'
    elif inputKeyboard == 'SalageParBrossage':
        return 'SalageParBrossage'
    else:
        inputFilter = input("Choissisez entre : \n- SalageASec\n- SalageEnBainDeSaumure\n- SalageParBrossage\n")
        return verificationConceptionSalage(inputFilter)


# Différentes requetes :
def getAllFromage():
    return getPrefix() + """
        SELECT ?fromage
        WHERE { ?fromage a onto:NosFromages}
    """


def getAllFromageFromAnimal(animal):
    return getPrefix() + """
        SELECT ?fromage
        WHERE { ?fromage a onto:NosFromages. ?fromage onto:hasForAnimal onto:""" + animal + """}
    """


def getAllFromageFromConception(hasFor, equal):
    return getPrefix() + """
        SELECT ?fromage
        WHERE { ?fromage a onto:NosFromages. ?fromage onto:""" + hasFor + """ onto:""" + equal + """}
    """


def getAllFromageFromRegion(region):
    return getPrefix() + """
        SELECT ?fromage
        WHERE { ?fromage a onto:NosFromages. ?fromage onto:hasForRegion onto:""" + region + """}
    """


def getAllFromageFromType(type):
    return getPrefix() + """
        SELECT ?fromage
        WHERE { ?fromage a onto:""" + type + """}
    """


# Main
if __name__ == '__main__':
    filteringOption = input("Avec quelle option souhaitez-vous trier les fromages ? (type/animal/region/conception) : ")
    filteringOption = verificationFilter(filteringOption)
    print("Vous avez décidé de filter par " + filteringOption)

    q = getAllFromage()

    if filteringOption == 'Type':
        type = input(
            "Veillez choisir entre : \n-frais\n-gras\n-pate molle croute fleurie\n-pate molle croute lavee"
            "\n-pate persille\n-pate presse et cuite\n-pate presse et non cuite\n")
        type = verificationType(type)
        q = getAllFromageFromType(type)

    elif filteringOption == 'Animal':
        animal = input("Veillez choisir entre brebis/vache/chevre/bufflone :")
        animal = verificationAnimal(animal)
        q = getAllFromageFromAnimal(animal)

    elif filteringOption == 'Conception':
        print("Vous avez décidé de filter par Conception\n")

        conceptionFilter = input("Veillez choisir entre affinage/pasteurisation/salage :")
        conceptionFilter = verificationConceptionFilter(conceptionFilter)

        if conceptionFilter == "hasForAffinage":
            conception = input(
                "Veillez choisir entre : \n- 1JourEtPlus\n- 1MoisEtPlus\n- 5MoisEtPlus\n- SansAffinage\n :")
            conception = verificationConceptionAffinage(conception)

        elif conceptionFilter == "hasForPasteurisation":
            conception = input("Veillez choisir entre : \n -NonPasteurise\n -PasteurisationVariable\n -Pasteurise\n")
            conception = verificationConceptionPasteurisation(conception)

        elif conceptionFilter == "hasForSalage":
            conception = input("Veillez choisir entre : \n- SalageASec\n- SalageEnBainDeSaumure\n- SalageParBrossage\n")
            conception = verificationConceptionSalage(conception)

        q = getAllFromageFromConception(conceptionFilter, conception)
    elif filteringOption == 'Region':
        region = input(
            "Veillez choisir entre :\n-AuvergneRhoneAlpes\n-BourgogneFrancheComte\n-Bretagne\n-Corse\n-GrandEst"
            "\n-HautDeFrance\n-Italie\n-Nord\n-Normandie\n-Occitanie\n-PaysDeLaLoire\n-Pyrenees\n-Suisse\n")
        region = verificationRegion(region)
        q = getAllFromageFromRegion(region)

    g = Graph()
    g.parse("./fromage.owl")
    response = g.query(q)
    if len(response):
        for x in response:
            print(x.fromage.split("#")[1])
            webbrowser.open('https://www.google.com/search?q=' + x.fromage.split("#")[1] + '+fromage')
    else:
        print("Aucun fromage correspond.")
