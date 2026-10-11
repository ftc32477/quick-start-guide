# Programmation

## 1. Informations de base

Voici les éléments complémentaires requis pour la Programmation.

### Applications

- Git
- Visual Studio Code
- Android Studio

---

## 2. Configuration de l'environnement

L'environnement de travail suivant doit être configuré avant de commencer ; suivez les instructions ci-dessous. En cas de question, consultez un administrateur.

### Navigateur web

Voici les sites à ajouter à vos favoris :

| Nom | Adresse |
|------|------|
| Programming Resources | https://www.firstinspires.org/resources/library/ftc/programming-resources |
| REV Robotics Documentation | https://docs.revrobotics.com/duo-control/hello-robot-java/welcome |
| Pedro Pathing | https://pedropathing.com/ |
| Robot Dashboard | http://192.168.43.1:8080/ |

### Git

Git est l'outil de gestion de versions des fichiers de code adopté par notre équipe. Android Studio ne l'intègre pas nativement : vous devez l'installer et le configurer, en choisissant l'une des deux méthodes suivantes.

**Méthode 1 (télécharger et installer Git dans Android Studio) :**

1. Ouvrez Android Studio et accédez à la page des paramètres : File → Settings sous Windows/Linux, Android Studio → Settings (ou Preferences) sous macOS
2. Dans le menu de gauche, dépliez Version Control, puis cliquez sur Git
3. Si Git n'est pas détecté, l'interface propose une entrée de téléchargement : cliquez dessus pour télécharger et installer Git
4. Une fois l'installation terminée, vérifiez le chemin du programme Git dans Path to Git executable (git.exe sous Windows) ; cliquez sur Test jusqu'à ce que la mention Successful s'affiche, puis cliquez sur Apply et OK pour enregistrer

**Méthode 2 (installer Git séparément, puis configurer le chemin dans Android Studio) :**

1. Rendez-vous sur le site officiel de Git [https://git-scm.com/downloads](https://git-scm.com/downloads) et téléchargez le programme d'installation adapté à votre système (Windows / macOS / Linux)
2. Lancez le programme d'installation et cliquez sur Next en conservant les options par défaut
3. Ouvrez Android Studio et accédez à Settings → Version Control → Git
4. Saisissez ou sélectionnez le chemin du programme Git dans Path to Git executable (détection automatique si la variable d'environnement PATH est configurée)
5. Cliquez sur Test ; lorsque la mention Successful s'affiche, cliquez sur Apply et OK pour enregistrer

Pour activer la gestion de versions dans le projet actuel : cliquez sur VCS dans le menu supérieur → Enable Version Control Integration..., sélectionnez Git, puis cliquez sur OK.

### Android Studio

Android Studio est l'outil d'écriture des programmes adopté par notre équipe.

**Installation du logiciel et configuration de l'environnement :**

1. Ouvrez [https://developer.android.com/studio](https://developer.android.com/studio)
2. Cliquez sur « Download Android Studio », téléchargez la version correspondante, puis installez-la.

**Points d'attention lors de l'installation sous Windows :**

- Les deux cases à cocher doivent être cochées
- Choisissez un chemin disposant d'un espace suffisant et qui ne sera pas modifié

**Initialisation :**

- Sélectionnez le mode « Standard »
- Cochez « Accept » lors de l'acceptation des licences
- Laissez le reste inchangé et cliquez sur « Next »

**Installation du pack de langue chinoise (optionnel) :**

1. Ouvrez le [pack de langue chinoise d'Android Studio](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. Téléchargez la dernière extension de langue (fichier .jar)
3. Dans la liste des onglets à gauche de l'écran d'accueil, sélectionnez « Plugins », puis « Install Plugin from Disk »
4. Sélectionnez le fichier .jar téléchargé et ouvrez-le ; une fois le plugin chargé, assurez-vous qu'il est activé
5. Dans la liste des onglets à gauche, sélectionnez « Customize », ouvrez « Language and Region », choisissez « Chinese (Simplified) » sous « Language » et « Americas » sous « Region », puis redémarrez

**Clonage du dépôt :**

1. Cliquez sur « GitHub » dans la liste des onglets à gauche, puis connectez-vous via « Log in with GitHub » pour autoriser l'accès.
2. Sélectionnez le dépôt du programme correspondant à la saison en cours (créé séparément pour chaque saison, avec un nom de la forme `FTC-32477-<saison>-Program` ; confirmez auprès d'un administrateur avant la création du dépôt de la nouvelle saison)
3. Choisissez un dossier vide situé sur un chemin qui ne changera pas, puis cliquez sur « Clone »
4. Attendez la fin du téléchargement ; suivez la progression via l'onglet « Build » dans la barre latérale gauche ou via la barre de progression en bas à droite de la fenêtre

> [!warning] En cas de problème, consultez un administrateur.

### Visual Studio Code

Visual Studio Code est l'outil adopté par notre équipe pour l'édition du code et la consultation de l'historique.

**Installation du logiciel et configuration de l'environnement :**

1. Ouvrez [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Téléchargez la version correspondante, puis installez-la
3. Si vous souhaitez l'interface en chinois, installez le [pack de langue chinoise de VS Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans).

---

## 3. Présentation des outils

### Android Studio

Documentation officielle : [https://developer.android.com/studio/intro?hl=fr](https://developer.android.com/studio/intro?hl=fr)

Ce projet s'appuie sur le framework d'application officiel fourni par la FTC : le programme de contrôle du robot est écrit en Java dans le dossier `TeamCode` et appelle les bibliothèques nécessaires à son fonctionnement.

Pour les connaissances de base à maîtriser sur Android Studio, reportez-vous au guide rapide de l'interface proposé dans la documentation officielle.

### Visual Studio Code

Documentation officielle : [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

La logique d'utilisation de Visual Studio Code est similaire à celle d'Android Studio et son usage est moins fréquent ; pour l'interface, reportez-vous à la section Android Studio.

### Robot Dashboard

- Connectez-vous au réseau Wi-Fi « `32477-RC` ». Mot de passe Wi-Fi : demandez-le à un administrateur ou récupérez-le via le Driver Hub.
- L'adresse est la suivante : [http://192.168.43.1:8080/](http://192.168.43.1:8080/) (accessible uniquement depuis le réseau local du robot)
- Il s'agit de la page web du module Wi-Fi intégré au Control Hub (désignée officiellement sous le nom de Robot Controller Console), qui fournit une interface graphique d'administration du Control Hub.

Pour les connaissances de base à maîtriser sur le Robot Dashboard, reportez-vous au guide rapide de l'interface proposé dans la documentation officielle.

---

## 4. Flux de travail

Le travail principal de l'équipe Programmation se divise en trois volets :

- **Programmes autonomes** : la logique de contrôle de la phase autonome (Auto) de la saison
- **Programmes de téléopération (TeleOp)** : la logique de commande de la phase télécommandée (TeleOp)
- **Configuration des capteurs** : la configuration des différents capteurs et systèmes de vision

> [!info] Pilotage (Driver) : le robot est piloté à la manette Xbox ; officiellement, seul le modèle Xbox 360 est autorisé. Les pilotes sont sélectionnés au sein de l'équipe ; les personnes déjà à l'aise avec la manette sont avantagées.

### Le débogage est au cœur du travail

> [!info] La difficulté du développement de programmes tient principalement au débogage. Trajectoires autonomes, commandes manuelles, paramètres PID, configuration de la vision, etc. : la plupart disposent déjà de packages prêts à l'emploi qu'il suffit de réutiliser ; l'essentiel du travail consiste à ajuster et à valider les paramètres.

Le débogage traverse l'ensemble du flux de développement :

1. **Analyse des besoins** : clarifier les règles et les exigences des tâches de la saison en cours
2. **Conception de l'architecture** : concevoir l'architecture globale du programme et la découpe en modules
3. **Écriture du code** : écrire le code Java dans Android Studio
4. **Gestion de versions** : gérer les versions du code avec Git
5. **Débogage** : régler les trajectoires autonomes, les commandes manuelles, les paramètres PID et la configuration de la vision
6. **Tests et validation** : vérifier le fonctionnement du programme sur le robot
7. **Revue de code** : effectuer la revue et la fusion du code via GitHub
8. **Déploiement** : déployer la version finale sur le Robot Controller


### Programmation assistée par IA

> [!info] Le développement de programmes peut s'appuyer sur des outils tels que les agents IA. La compétence essentielle est de **lire le code généré par l'IA, savoir quoi modifier et maîtriser les méthodes de débogage** ; inutile d'écrire tout le code à la main depuis zéro.

- La logique de base de la programmation (boucles for, boucles while, etc.) est universelle d'un langage à l'autre ; seule la syntaxe diffère. Les élèves ayant des bases en C++ s'adaptent rapidement à Java.

---

## 5. Bases de la collaboration sur GitHub

> [!info] Cette section couvre le minimum nécessaire pour utiliser GitHub : consulter les dépôts, télécharger des fichiers, signaler un problème, modifier du contenu, collaborer et rechercher des projets open source. Pour les explications complètes, consultez les liens vers la documentation officielle en fin de section. Les boutons d'interface sont majoritairement en anglais ; dans ce document, les termes sont indiqués sous la forme « français (anglais) ».

### Qu'est-ce que GitHub ?

GitHub est une **plateforme d'hébergement de code et de collaboration** basée sur Git : le code réside dans le cloud (dépôt) et conserve l'historique complet des modifications (commits) ; plusieurs personnes peuvent collaborer sur un même projet (branches, pull requests) ; la plateforme fournit également des outils associés : problèmes, automatisation (Actions), hébergement de sites (Pages).

Principaux usages de GitHub pour l'équipe :

- **Héberger les programmes de saison** : un dépôt public est créé séparément pour chaque saison (par duplication du modèle officiel du SDK), puis archivé en lecture seule à la fin de la saison ; les dépôts des nouvelles saisons sont ajoutés au tableau de cette section après leur création.
- **Maintenir le « Guide de démarrage rapide »** : les fichiers sources et les scripts de compilation se trouvent dans le dépôt public `ftc32477/quick-start-guide`.
- **Publier le site de l'équipe** : le dépôt de publication du site est `ftc32477/ftc32477.github.io` ; chaque rubrique est compilée par GitHub Actions depuis son dépôt source, puis publiée dans son sous-chemin (ce guide → `/docs/`) ; la racine redirige actuellement vers `/docs/`. Par la suite, chaque catégorie de ressources disposera de son propre dépôt source et sera publiée dans son sous-chemin respectif.
- **Rechercher des projets open source** : outils d'ingénierie génériques, ainsi que le code et les solutions partagés par la communauté FTC.

**Comptes et organisation** : utilisez votre compte personnel (procédure d'inscription dans « Essentiels de l'équipe ») ; un administrateur vous invite à rejoindre l'organisation `ftc32477`. Les dépôts appartiennent à l'organisation et les droits d'action sont attribués par les administrateurs selon les rôles :

| Rôle | Actions autorisées (résumé) |
|------|------|
| Read (Lecture) | Consulter et discuter le projet |
| Triage (Tri) | Gérer les problèmes et les pull requests, sans écrire de code |
| Write (Écriture) | Envoyer du contenu vers le dépôt |
| Maintain (Gestion) | Gérer le dépôt, sans actions sensibles ou destructrices |
| Admin (Administration) | Accès complet, y compris la suppression de dépôts |

> [!warning] Sans droit d'écriture, soumettez vos modifications par pull request ou confiez-les à un mainteneur ; en cas de doute sur vos droits, agissez en lecture seule, sans chercher à tester ni à contourner les restrictions d'accès.

### Mémo terminologique

| Terme | Signification (en une phrase) |
|------|------|
| Dépôt (Repository) | Emplacement de stockage des fichiers du projet et de son historique complet |
| Commit | Instantané d'une modification accompagné d'un message, qui constitue l'historique |
| Branche (Branch) | Ligne de développement parallèle au sein du dépôt ; les modifications y sont d'abord appliquées |
| Clonage (Clone) | Téléchargement complet du dépôt sur l'ordinateur local |
| Duplication (fork) | Copie du dépôt d'autrui sur son propre compte ; les modifications n'affectent pas le dépôt d'origine |
| Pull request (PR) | Mécanisme de demande de révision puis de fusion des modifications d'une branche ; cœur de la collaboration |
| Problème (issue) | Fil de discussion pour poser une question, signaler une erreur ou faire une suggestion |
| Version (release) | Publication officielle numérotée, accompagnée de fichiers téléchargeables (comme le PDF du guide) |
| Étoile (Star) | Mise en favori et marque d'intérêt ; sert aussi à évaluer la popularité d'un projet |
| Abonnement (Watch) | Recevoir les notifications d'activité du dépôt |
| Actions | Pipeline d'automatisation de GitHub (utilisé ici pour compiler et publier le site) |
| Pages | Hébergement de sites statiques de GitHub (le site de l'équipe est publié ainsi) |
| README | Document explicatif de la page d'accueil du dépôt, à lire en premier |

### Carte des dépôts de l'équipe

| Dépôt | Description | Mode de modification |
|------|------|------|
| `quick-start-guide` | Fichiers sources du guide, scripts de compilation et site généré (public) | Soumettre une pull request, ou confier la modification à un mainteneur |
| `ftc32477.github.io` | Dépôt de publication du site de l'équipe (public), alimenté automatiquement par les dépôts sources | Ne pas modifier directement |
| `.github` | Ressources de la page d'accueil de l'organisation, comme la présentation (public) | Soumettre une pull request, ou confier la modification à un mainteneur |
| `FTC-32477-<saison>-Program` | Dépôt du programme de saison (public) : créé séparément pour chaque saison, anciennes saisons archivées en lecture seule ; le nom exact sera ajouté après la création du dépôt de la nouvelle saison | Selon la répartition interne du groupe Programmation |

> [!danger] **Zone interdite : le dépôt de publication** : tout le contenu de `ftc32477.github.io` provient de ses dépôts sources respectifs et est publié automatiquement par GitHub Actions ; toute modification directe sera écrasée lors de la prochaine publication. Ne modifiez, ne validez et ne supprimez rien dans ce dépôt ni sur aucun contenu généré. Toute question relative au site se traite dans le dépôt source correspondant (pour ce guide : `quick-start-guide`).

### Navigation et téléchargement

1. Ouvrez la page d'accueil de l'organisation [https://github.com/ftc32477](https://github.com/ftc32477), puis entrez dans un dépôt depuis la liste Repositories
2. Lisez d'abord le **README** sur la page d'accueil du dépôt (objet du projet, mode d'emploi) ; la section About, à droite, contient une présentation et un lien vers le site
3. Onglets en haut de page (leur visibilité dépend de vos droits) :
   - **Code** : liste des fichiers et historique des commits
   - **Issues** : problèmes et suggestions
   - **Pull requests** : modifications en attente de révision
   - **Actions** : historique des compilations et publications automatiques
   - **Releases** : versions officielles et fichiers téléchargeables
4. Télécharger le dépôt complet : Code → **Download ZIP**
5. Télécharger le PDF du guide : ouvrez **Releases**, sélectionnez une version, puis téléchargez la langue voulue dans Assets
6. Consulter l'historique : liste **Commits** de la page Code → ouvrez un commit précis pour voir le détail des modifications (diff)

### Signaler un problème (issue)

En cas de panne, d'erreur dans la documentation ou de suggestion, utilisez une issue :

1. Ouvrez l'onglet **Issues** du dépôt concerné et vérifiez d'abord qu'un problème identique n'existe pas déjà
2. Cliquez sur **New issue** et résumez le problème en un titre d'une phrase
3. Dans le corps du texte, précisez : **ce qui s'est produit**, **le résultat attendu**, **comment reproduire** le problème (étapes), ainsi que les captures d'écran pertinentes (après avoir retiré les informations personnelles)
4. Après l'envoi, suivez les réponses ; une fois le problème résolu, un mainteneur le ferme

> [!info] Canal de signalement dédié pour le guide : [https://github.com/ftc32477/quick-start-guide/issues](https://github.com/ftc32477/quick-start-guide/issues)

### Modification depuis le web (édition → pull request)

Sans droit d'écriture, GitHub transforme automatiquement une modification faite en ligne en « duplication (fork) + pull request (PR) » :

1. Connectez-vous, puis ouvrez le fichier à modifier (par exemple un fichier `.md` de `src/fr/` du guide)
2. Cliquez sur l'icône en forme de crayon en haut à droite du fichier : **Edit this file**
3. Si vous n'avez pas le droit d'écriture, la page vous proposera de créer automatiquement une duplication ; acceptez
4. Modifiez le contenu et rédigez une description claire dans **Commit changes**
5. Sélectionnez **Create a new branch for this commit and start a pull request**, avec un nom de branche tel que `fix/typo-member`
6. Dans le formulaire de pull request qui s'ouvre, expliquez la modification et son motif, puis cliquez sur **Create pull request**
7. Attendez la révision par un mainteneur ; en cas de commentaire, poursuivez les modifications selon les retours ; après la fusion, la modification prend effet

> [!warning] Une pull request ne traite qu'un seul sujet ; ne modifiez pas les fichiers que vous ne maîtrisez pas (scripts de compilation, fichiers générés, etc.) ; ne soumettez aucune modification au dépôt de publication.

### Collaboration en local

Travailler sur un clone local du dépôt est la méthode la plus courante. Elle suppose que Git est installé sur votre machine (voir « 2. Configuration de l'environnement »). Commandes usuelles :

```bash
# Cloner le dépôt en local
git clone https://github.com/ftc32477/quick-start-guide.git
cd quick-start-guide

# Récupérer les dernières modifications avant de commencer
git pull

# Créer une branche pour le travail en cours
git switch -c feat/my-feature

# Après modification : état, indexation, commit
git status
git add <fichier>
git commit -m "description de la modification"

# Envoyer la branche vers GitHub
git push -u origin feat/my-feature
```

Après l'envoi, créez une pull request pour cette branche sur GitHub, puis attendez la révision et la fusion. Android Studio et Visual Studio Code offrent des opérations graphiques équivalentes (voir « 2. Configuration de l'environnement ») : les mêmes étapes peuvent être effectuées dans l'interface.

> [!warning] Trois règles : **faire un pull avant de commencer** ; **un commit ne traite qu'une seule chose, avec un message clair** ; **pousser vers sa propre branche, jamais directement sur main**.

**Synchronisation d'une duplication avec le dépôt amont (pour contribuer à des projets externes)** : une duplication ne se met pas à jour automatiquement. Ajoutez d'abord le dépôt d'origine comme amont : `git remote add upstream <adresse du dépôt d'origine>`, puis synchronisez avec `git fetch upstream` et une opération de fusion (voir la section « Synchronisation d'une duplication » de la documentation officielle).

### Communauté open source (recherche, évaluation et contribution)

**Recherche** (le champ de recherche accepte des qualificateurs combinables) :

- `topic:ftc`, `topic:first-tech-challenge`, `topic:ftc-robot` : point d'entrée principal des projets de la communauté FTC
- `ftc language:Java sort:updated` : projets Java encore maintenus
- `"FIRST Tech Challenge" in:readme` : projets mentionnant la FTC dans leur README

Ressources open source courantes pour la FTC (toutes disponibles sur GitHub) :

| Projet | Usage |
|------|------|
| FIRST-Tech-Challenge/FtcRobotController | SDK officiel de la FTC et exemples |
| FTCLib/FTCLib | Bibliothèque d'outils courante pour la FTC |
| acmerobotics/road-runner | Planification de mouvements et suivi de trajectoire |
| Pedro-Pathing/PedroPathing | Planification de trajectoire |
| acmerobotics/ftc-dashboard | Tableau de bord de débogage |
| OpenFTC/EasyOpenCV | Traitement de vision |
| the-orange-alliance, ftc-scout/ftc-scout | Données et statistiques de compétition |

**Évaluer la fiabilité d'un dépôt (cinq points à vérifier)** : date du dernier commit (projet encore maintenu ou non), qualité du README et de la documentation, licence (License), activité des Issues, existence de versions officielles dans les Releases.

**Aperçu des licences** (à consulter avant toute utilisation du code ou des ressources d'autrui) :

| Licence | Explication en une phrase |
|--------|------------|
| MIT | La plus permissive : utilisation libre, à condition de conserver la mention de copyright |
| Apache-2.0 | Également permissive, avec en plus une concession de brevet et la mention des modifications |
| GPL-3.0 | Virale : toute œuvre dérivée doit également être publiée en open source |
| Sans licence | Par défaut « tous droits réservés » : la copie directe est **interdite**, il faut d'abord contacter l'auteur |

**Contribuer** : lisez d'abord le `CONTRIBUTING.md` (guide de contribution) et le code de conduite à la racine du projet ; pour une modification incertaine, ouvrez d'abord une issue pour en discuter ; pour une correction mineure, suivez la procédure « édition → pull request » ci-dessus.

> [!warning] Sécurité : n'exécutez pas de scripts ou de fichiers exécutables d'origine inconnue ; ne publiez jamais de clé d'API, de mot de passe ou de token dans une issue ou un dépôt ; méfiez-vous des commandes d'installation du type `curl | bash`.

### Opérations dangereuses

> [!danger] Les opérations suivantes peuvent causer des pertes irréversibles : ne les exécutez jamais en tant que membre ordinaire ; si elles sont réellement nécessaires, faites-les d'abord confirmer par un administrateur.
>
> - modifier directement le dépôt de publication `ftc32477.github.io` (la modification sera écrasée et polluera le site officiel)
> - `git push --force` : écrase l'historique distant et peut faire disparaître les commits de vos coéquipiers
> - `git reset --hard` : supprime les modifications locales non envoyées, avec peu de chances de les récupérer par la suite
> - supprimer une branche ou un dépôt, ou modifier la visibilité, le nom ou le propriétaire d'un dépôt
> - envoyer des clés, des mots de passe ou des tokens vers un dépôt (une fois publics, ils restent dans l'historique même après suppression : révoquez-les et recréez-les immédiatement)
> - publier des documents internes ou des informations personnelles (adresse e-mail, domicile, données personnelles dans les captures d'écran) dans une issue, une pull request ou un dépôt public
> - exécuter ou fusionner du code d'origine inconnue

> [!info] Sécurité du compte : ne partagez jamais votre compte ; GitHub impose progressivement l'authentification à deux facteurs (2FA) aux comptes qui contribuent au code ; activez-la lorsque la plateforme le demande ; créez les jetons d'accès personnels (tokens) avec les droits minimaux et ne les inscrivez jamais dans le code ou dans un dépôt.

### Liste d'exercices

1. Ouvrez la page de l'organisation, entrez dans le dépôt `quick-start-guide`, puis expliquez l'objet de ce projet à partir du README
2. Téléchargez le PDF du guide dans la langue de votre choix depuis les Releases
3. Dans l'historique des commits, trouvez la dernière modification et indiquez ce qu'elle a changé
4. Recherchez « PDF » dans les Issues et vérifiez si des problèmes similaires existent
5. Corrigez une faute de frappe selon la procédure « édition → pull request » et soumettez une pull request

### Accès à la documentation officielle

Pour les usages plus avancés, consultez selon vos besoins la documentation officielle :

- Démarrage rapide avec GitHub : [https://docs.github.com/fr/get-started/quickstart](https://docs.github.com/fr/get-started/quickstart)
- Écriture et stockage de votre code (branches/commits/pull requests) : [https://docs.github.com/fr/get-started/start-your-journey/writing-and-storing-your-code](https://docs.github.com/fr/get-started/start-your-journey/writing-and-storing-your-code)
- Aide-mémoire Git : [https://docs.github.com/fr/get-started/git-basics/git-cheatsheet](https://docs.github.com/fr/get-started/git-basics/git-cheatsheet)
- Syntaxe de recherche : [https://docs.github.com/fr/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax](https://docs.github.com/fr/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- Rôles de dépôt pour une organisation : [https://docs.github.com/fr/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization](https://docs.github.com/fr/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
- Cours interactifs (en anglais) : [https://skills.github.com/](https://skills.github.com/)

> [!info] En cas de doute sur une opération, consultez d'abord un administrateur ou posez votre question dans les Issues.
