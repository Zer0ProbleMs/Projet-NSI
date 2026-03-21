from nicegui import *
from Layout import *

@ui.page('/aidegénéral')

def aidegénéral(): # Des aides générales pour tout débutant ou juste n'importe qui.
    designaide("Aide", 300)
    titre("Général")
    synops("Bienvenue sur notre site web! Si vous vous retrouvez sur cette page, cela veut dire que vous avez besoin d\'une aide de tel sorte. Ainsi, voici une général :")
    with idéequestion(text='Comment est-je accéder à la page aide ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idéesynops("Il est possible que vous n\'ayez pas accéder à la page aide par accident, ou bien si. Cependant, qu\'importe si cela était un accident, voici les différentes manières d'atteindre la page dans laquelle vous vous situez :")
        idée("Il est possible que vous ayez rentrer le lien vers cette page qui se termine par \"xxx/aidegénéral\".")
        idée("La deuxième possibilité est que vous avez appuyé sur le bouton qui se situe dans le coin en bas à droite de la page du site web. Si vous recliquer dessus sur cette même page, le bouton ne fera que rafraichîr la page, cependant, sur n\'importe quelle autre page, elle vous rammèneras de nouveau ici !")       
    with idéequestion(text='Comment puis-je accéder à d\'autres pages ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idéesynops("Le système d\'accès à d\'autres pages est très intuitifs. Egalement, les autres \"aides\", pour les pages spécifiques, vous indiquerons également comment accéder à ces mêmes pages. Cependant, voici comment accéder aux pages principales :")
        idée("Page Aide : Pour accéder à la page aide, il vous faut simplement appuyer sur le point d\'interrogation dans le coin en bas à droite de la page.")
        idée("Page Paramètre : Vous pouvez accéder à vos paramètres en allant dans le menu qui se situe dans le coin en haut à droite de la page, vous y trouverez le bouton \"paramètres\" qui vous mènera directement aux paramètres.")

@ui.page('/aideprofile')
def aideprofile(): # Explication de comment la page pour le profile et le profile en général fonctionne
    designaide("Aide", 300)
    titre("Profile")
    synops("Vous vous demandez comment accéder à votre profil? Comment vous pouviez changer de pseudonyme ou de photo de profile ? Voici tout ce que vous devez savoir :")
    with idéequestion(text='Comment puis-je accéder à mon propre profile ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idéesynops("La partie la plus importante d\'un site en ligne avec compte personnel, c'est de pouvoir au moins accéder à son propre profile, ainsi, voici les moyens principaux pour y accéder :")
        idée("La meilleure manière mais également la plus facile pour pouvoir accéder à votre profile, c\'est en appuyant sur l\'icone de profile dans le coin en haut à droite de votre écran, ce qui vous mèneras directement à votre page de profile.")
        idée("Une autre manière de faire qui est moyen efficace et selon moi, un peu inutile, est de rentrer le lien directement dans la barre de recherche.")
    with idéequestion(text='Quelles sont les modifications que je peux faire à mon profil et comment ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idéesynops("Sur votre profile, il est commun de pouvoir changer de bannière, biographie, pseudonyme, et tant d\'autres choses ! Cela est également possible sur notre site des ces manières :")
        idée("Pour changer votre pseudonyme ou de biographie, diriger vous sur la section profile et appuyer sur le bouton \"Modifier Profile\". Cela vous mènera à une page qui vous laissera mettre le pseudonyme que vous souhaitez tant de mettre !")
        idée("Pour changer de photo de profil, il ne faut qu\'aller sur la page de profile et appuyer sur la grande icon de profile. Poursuivez ensuite par insérer l\'image que vous souhaite comme photo de profile et recharger la page.")
        idée("Pour changer de bannière, l\'idée est très similaire à la manière de changer une photo de profile, cependant, au lieu d\'appuyer sur l\'icon de profile, appuyer sur la bannière qui se situe au-dessus d\'elle et faites le même processus que pour la photo de profile.")

@ui.page('/quinoussommes')
def quinoussommes(): # Explication de qui on est, ce qu'on fait, et pourquoi le site, etc...
    designaide("Aide", 300)
    titre("Qui sommes nous ?")
    synops("Si vous êtes ici, c\'est que vous vous demandiez qui nous étions et quelle importance nous avons dans ce monde, donc voici les réponses à vos questions :")
    with idéequestion(text='Qui sommes nous ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idée("Nous sommes un groupes de trois élève de terminale au lycée Louis Armand. Le groupe est composé de moi (Daris), Anfel, et Paul.")
        idée("Notre professeur de la spécialité Numérique Science de l\'Informatique, celui qui s\'occupera de noter notre projet de dimensions HORS-NORME, Monsieur Bourlier.")
        idée("Une classe entière d\'élève de terminale rempli à rabord. La moitié d\'entre eux n\'ayant pris la spécialité que pour des raisons qui n\'ont rien à voir avec ce qu\'ils veulent faire dans le futur, soit dû à leur notes, ou dû à d'autres obligations. (Je vous vois)")
    with idéequestion(text='Pourquoi un site? Et pourquoi local ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idéesynops("Si seulement héberger un site web était plus simple, cependant, ça ne l'est pas, voici pourquoi :")
        idée("Nous avons fait ce site, non pas pour le public (désolé), mais pour accomplir notre projet de Numérique Science de l\'Informatique annuel. Cependant, qui sait, peut-être un jour, le site se pourra t-il être développé plus loin encore et pourra réellement être distribué au public ! (Un grand rêve qui n\'arrivera sûrement pas)")
        idée("En plus de cela, ce site est un moyen pour nous d\'apprendre à utiliser des bibliothèques python qui nous sont complètement inconnus, dans notre cas, NiceGui. Mais cela nous apprends également à nous adapter et à en apprendre plus sur le code en général, ce qui n\'est que gagnant-gagnant")
        idée("Le fait d'héberger le site sur un serveur était une idée qui nous était venu que quand notre professeur nous l'avait recommandé, de plus, il existe quelques moyens d'héberger gratuitement un site web. Cependant, le soucis vient du fait que notre site web est créé en python à l'aide de NiceGui puis est converti en HTML, JavaScript, etc... Les serveurs ne peuvent pas prendre en compte cette conversion, donc le site ne fonctionnnerait pas.")
    with idéequestion(text='D\'ou vient cette idée du site ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idée("L\'idée de notre projet, avoir des calendriers qui peuvent être partagé entre personnes, nous est venu par hasard après plusieurs heures de réflections. Cependant, ce site n\'était pas la seule idée que nous avions, ça n\'est seulement celle qu\'on a décidé d\'utiliser! Nous avions l\'idée par exemple de faire une application qui permettrais d\'écouter n\'importe quelle musique facilement et rapidement, comme un iPod, ou un jeu vidéo, cependant, ces deux idées on rapidement été rejetés.")
    with idéequestion(text='Quelles étaient vos inspirations ?', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px; {police3}').classes('w-full text-2xl'):
        idéesynops("Nous nous sommes inspiré d\'un grand nombre de site que je pourrais lister pendant un bon bout de temps, mais je pense que j\'essayerais de ne pas aller trop loin, pour votre plaisir ainsi que celui de mes mains :")
        idée("NiceGui : Nous nous sommes inspiré du site de documentation de la bibliothèques NiceGui elle même. Par exemple, l\'idée des pages aides avec les boutons qui peuvent s\'étendrent m\'est venu grâce à la documentation NiceGui, c\'était l\'une des premières idée que nous avions eu !")
        idée("Discord : Une grande plateforme avec plusieurs centaines de millions d\'utilisateurs, leur application est complète, c\'est pourquoi on a pris inspiration de leur page de paramètres mais aussi en majorité de leur page de profile.")
        idée("Riot App : Bizarre de même le mentionner, cependant, il nous fallait une idée pour l\'apparence de la boîte des contacts, et c\'était la première application qui m\'étais venue en tête.")
        idée("Instagram : Presque pour les mêmes raisons que discord, nous nous sommes inspiré principalement des paramètres d'instagram qui sont très fluide. ")

@ui.page('/départ')
def départ(): # Le déroulement du développement de notre site
    designaide("Aide", 300)
    ui.label("Profile").classes('text-4xl font-bold')
    ui.separator()
    ui.label("Vous vous demandez comment accéder à votre profil? Comment vous pouviez changer de pseudonyme ou de photo de profil? Voici ce que vous devez savoir :").classes('text-2xl font-light text-center')
    ui.separator()
    ui.label("> La toute première chose à savoir est que vous pouvez facilement accéder à votre profile en appuyant sur l'icone de profile dans le coin en haut à droite de votre écran.").classes('text-xl font-light')
    ui.label("> Pour changer de pseudonyme, diriger vous sur la section profile et appuyer sur le bouton \"Modifier Profile\", ce qui vous laissera insérer le pseudonyme que vous souhaiter.").classes('text-xl font-light')

@ui.page('/eastereggpoème')
def eastereggpoème(): #La page d'un easter que j'ai envie de placer (poèmes ou autres?)
    designaide("Aide", 300)
    ui.label("Poème").classes('text-4xl font-bold')
    ui.separator()
    ui.label("Vous vous demandez comment accéder à votre profil? Comment vous pouviez changer de pseudonyme ou de photo de profil? Voici ce que vous devez savoir :").classes('text-2xl font-light text-center')
    ui.separator()
    ui.label("> La toute première chose à savoir est que vous pouvez facilement accéder à votre profile en appuyant sur l'icone de profile dans le coin en haut à droite de votre écran.").classes('text-xl font-light')
    ui.label("> Pour changer de pseudonyme, diriger vous sur la section profile et appuyer sur le bouton \"Modifier Profile\", ce qui vous laissera insérer le pseudonyme que vous souhaiter.").classes('text-xl font-light')

def titre(texte): # Le titre de la page dans laquelle l'utilisateur se trouve
    ui.label(texte).classes('text-4xl font-bold self-center').style(f'{police3}')
    ui.separator()
    
def synops(texte): # Un résumé de pourquoi l'utilisateur se trouverais sur cette page et ce qu'il y a
    ui.label(texte).classes('text-2xl text-center').style(f'{police5}')
    ui.separator()

idéequestion = ui.expansion # Une manière plus facile d'utiliser la commande qui fait des boutons qui s'étendent, 
                            # et utilisé pour poser une question que pourrait se poser l'utilisateur

def idéesynops(texte): # Pas obligatoire, mais pareil que le synops principal, mais se trouve cependant dans "l'idée question"
    ui.label(texte).classes('text-xl text-center font-bold').style(f'{police1}')
    ui.separator()

def idée(texte): # Explication compréhensible des réponses au questions
    ui.label("> " + texte).classes('text-xl font-light').style(f'{police1}')

ui.run()