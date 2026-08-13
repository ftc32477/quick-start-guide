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

**Passer l'interface en chinois (optionnel) :**

1. Ouvrez le [pack de langue chinoise d'Android Studio](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. Téléchargez la dernière extension de langue (fichier .jar)
3. Dans la liste des onglets à gauche de l'écran d'accueil, sélectionnez « Plugins », puis « Install Plugin from Disk »
4. Sélectionnez le fichier .jar téléchargé et ouvrez-le ; une fois le plugin chargé, assurez-vous qu'il est activé
5. Dans la liste des onglets à gauche, sélectionnez « Customize », ouvrez « Language and Region », choisissez « Chinese (Simplified) » sous « Language » et « Americas » sous « Region », puis redémarrez

**Clonage du dépôt :**

1. Cliquez sur « GitHub » dans la liste des onglets à gauche, puis connectez-vous via « Log in with GitHub » pour autoriser l'accès.
2. Sélectionnez le dépôt de code de la saison en cours (par exemple : `ftc32477/FTC-32477-Decode-Program`)
3. Choisissez un dossier vide situé sur un chemin qui ne changera pas, puis cliquez sur « Clone »
4. Attendez la fin du téléchargement ; suivez la progression via l'onglet « Build » dans la barre latérale gauche ou via la barre de progression en bas à droite de la fenêtre

> [!warning] En cas de problème, consultez un administrateur.

### Visual Studio Code

Visual Studio Code est l'outil adopté par notre équipe pour l'édition du code et la consultation de l'historique.

**Installation du logiciel et configuration de l'environnement :**

1. Ouvrez [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Téléchargez la version correspondante, puis installez-la
3. Ouvrez le [pack de langue chinoise](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans) et installez-le pour passer l'interface en chinois.

---

## 3. Présentation des outils

### Android Studio

Documentation officielle : [https://developer.android.com/studio/intro?hl=zh-cn](https://developer.android.com/studio/intro?hl=zh-cn)

Dans ce projet, nous nous appuyons sur le framework d'application officiel fourni par la FTC et écrivons le programme de contrôle du robot en Java dans le dossier `TeamCode`, afin d'appeler les différentes bibliothèques nécessaires au fonctionnement du robot.

Pour les connaissances de base à maîtriser sur Android Studio, reportez-vous au guide rapide de l'interface proposé dans la documentation officielle.

### Visual Studio Code

Documentation officielle : [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

La logique d'utilisation de Visual Studio Code étant similaire à celle d'Android Studio et son usage étant moins fréquent dans ce projet, reportez-vous à la section Android Studio pour les indications d'interface ; nous n'y reviendrons pas ici.

### Robot Dashboard

- Connectez-vous au réseau Wi-Fi « `32477-RC` ». Mot de passe Wi-Fi : demandez-le à un administrateur ou récupérez-le via le Driver Hub.
- L'adresse est la suivante : [http://192.168.43.1:8080/](http://192.168.43.1:8080/)
- Il s'agit de la page web du module Wi-Fi intégré au Control Hub (désignée officiellement sous le nom de Robot Controller Console), qui fournit une interface graphique d'administration du Control Hub.

Pour les connaissances de base à maîtriser sur le Robot Dashboard, reportez-vous au guide rapide de l'interface proposé dans la documentation officielle.

---

## 4. Flux de travail

Le travail principal de l'équipe Programmation se divise en trois volets :

- **Programmes autonomes** : la logique de contrôle de la phase autonome (Auto) de la saison
- **Programmes de téléopération (TeleOp)** : la logique de commande de la phase télécommandée (TeleOp)
- **Configuration des capteurs** : la configuration des différents capteurs et systèmes de vision

### Le débogage est au cœur du travail

> [!info] La véritable difficulté du développement de programmes réside dans le débogage. Trajectoires autonomes, commandes manuelles, paramètres PID, configuration de la vision : la plupart des capteurs disposent de packages prêts à l'emploi que vous pouvez réutiliser directement ; votre véritable travail consiste à « régler ».

Le débogage traverse l'ensemble du flux de développement :

1. **Analyse des besoins** : clarifier les règles et les exigences des tâches de la saison en cours
2. **Conception de l'architecture** : concevoir l'architecture globale du programme et la découpe en modules
3. **Écriture du code** : écrire le code Java dans Android Studio
4. **Gestion de versions** : gérer les versions du code avec Git
5. **Débogage** : régler les trajectoires autonomes, les commandes manuelles, les paramètres PID et la configuration de la vision
6. **Tests et validation** : vérifier le fonctionnement du programme sur le robot
7. **Revue de code** : effectuer la revue et la fusion du code via GitHub
8. **Déploiement** : déployer la version finale sur le Robot Controller
