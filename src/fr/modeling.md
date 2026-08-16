# Modélisation & Conception

## 1. Informations de base

Voici les éléments complémentaires requis pour la Modélisation et conception.

### Applications

- Navigateur web (Chrome, Edge ou Safari)
- LocalSend
- Bibliothèque de pièces FTC Onshape — [https://ftconshape.com/](https://ftconshape.com/) (maintenue par FIRST et PTC ; envoyez un e-mail à FIRST@ptc.com pour rejoindre le dossier partagé)
- Plugin de bibliothèque de pièces FTC Insert Tool — [https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba](https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba) (installation depuis l'App Store Onshape : Subscribe → Get for Free)

### Comptes en ligne

- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/) (gratuit, inscription requise)

---

## 2. Configuration de l'environnement

L'environnement de travail suivant doit être configuré avant de commencer ; suivez les instructions ci-dessous. En cas de question, consultez un administrateur.

### Navigateur web

Voici les sites supplémentaires à ajouter à vos favoris :

| Nom | Adresse |
|------|------|
| goBILDA | https://www.gobilda.com/ |
| REV Robotics | https://www.revrobotics.com/ |
| CycleZLab | https://www.cyclezlab.com/ |
| Onshape Éducation | https://www.onshape.com/en/education/ |

### Inscription à un compte Onshape

Onshape est la plateforme de modélisation dans le cloud adoptée par notre équipe. Par rapport aux logiciels de modélisation industriels tels que SolidWorks, Onshape ne sollicite pas la configuration matérielle, facilite le partage de projets entre appareils, est simple à prendre en main et bénéficie du soutien officiel de FIRST : tout en restant complet, il est idéal pour apprendre la modélisation CAO et réaliser des projets.

**Procédure d'inscription :**

1. Ouvrez [https://www.onshape.com/en/education/](https://www.onshape.com/en/education/) et inscrivez-vous à un compte Éducation
2. Saisissez votre prénom (First name), votre nom (Last name) et votre adresse e-mail

> [!warning] N'utilisez pas QQ ni d'autres services de messagerie chinois : le code de vérification risque de ne jamais arriver. Utilisez plutôt @gmail.com ou @outlook.com.

3. Sur l'écran suivant, sélectionnez dans l'ordre votre statut « Student », le niveau scolaire « Grade School / K-12 (Ages <18) » et votre date de naissance, puis cliquez sur Suivant
4. Renseignez les informations suivantes :
   - Nom de l'établissement : BEIJING NATIONAL DAY EXPERIMENTAL SCHOOL
   - Site web de l'établissement : [https://sysyzx.bjhdedu.cn/](https://sysyzx.bjhdedu.cn/)
   - Année de fin d'études prévue
   - Raison de l'inscription : I am a member of FTC Team 32477, and I registered this account to use the team's modeling tools. (si vous ne savez pas quoi écrire, recopiez cette phrase)
   - Cochez les trois clauses d'accord ci-dessous pour terminer l'inscription
5. Consultez votre boîte e-mail pour confirmer l'inscription

> [!info] Une fois inscrit, communiquez votre compte à un administrateur afin qu'il vous ajoute au dossier partagé de l'équipe.

**Questions fréquentes :**

- Si la dernière étape signale un problème avec reCAPTCHA : le service de vérification humaine n'a pas répondu ; essayez de changer de réseau et assurez-vous de pouvoir joindre reCAPTCHA
- Si vous ne recevez pas le code de vérification par e-mail : après avoir attendu plus de 3 minutes, essayez une autre adresse e-mail (Outlook ou Gmail, pas QQ)

### Configuration d'Onshape

1. Entrez dans l'espace de travail, cliquez sur l'icône de compte en haut à droite et sélectionnez « Mon compte », la première option du menu déroulant
2. Sélectionnez « Préférences », la troisième option du menu en partant du haut, passez la première option de langue sur « Chinois simplifié », puis cliquez sur Enregistrer
3. Dans le même menu, passez les unités en système métrique (le millimètre est l'unité de longueur par défaut dans l'environnement de travail de l'équipe)

> [!info] Ces modifications ne s'appliquent qu'aux documents créés après le changement ; les documents existants conservent leurs unités.

4. Modifiez votre profil selon vos préférences

### Plugins Onshape

Grâce à sa nature cloud, Onshape dispose d'un riche écosystème de plugins partagés, disponibles via l'App Store Onshape, des sites tiers de plugins ou le partage entre utilisateurs.

Les plugins couramment utilisés par l'équipe sont (exemples uniquement) :

- **Bibliothèque de pièces FTC Onshape** (essentiel ; voir « 1. Informations de base »)
- **Lighten** (fonction personnalisée qui allège la structure des pièces)
- **Spur gear** (fonction personnalisée, générateur d'engrenages)
- **HTD Pulley Generator** (dérivé d'un autre document, générateur de poulies de courroie crantée)

---

## 3. Principes essentiels de modélisation

### Conception et assemblage de pièces

Lors de la modélisation 3D dans Onshape, portez une attention particulière aux points suivants :

- **Précision dimensionnelle** : assurez-vous que toutes les cotes du modèle correspondent aux pièces réelles
- **Relations d'assemblage** : configurez correctement les contraintes d'assemblage entre les pièces (Mates et Mate Connectors)
- **Vérification des interférences** : effectuez une vérification des interférences une fois l'assemblage terminé
- **Dénomination des pièces** : nommez les pièces et les assemblages selon des conventions uniformes

### Documents de projet et espace de travail

Lorsque vous travaillez sur un projet d'équipe, créez vos documents dans le dossier partagé de l'équipe afin que les autres membres puissent y accéder. Si vous n'y avez pas encore été ajouté, contactez un administrateur.

1. Dans votre espace de travail personnel, sélectionnez « Partagés avec moi » dans le menu de gauche et ouvrez le dossier « 32477 ». Vous pouvez y créer un nouveau document ou ouvrir un document existant de l'équipe (un document est un projet)
2. Pour créer un nouveau projet : cliquez sur le bouton bleu Créer en haut à gauche, choisissez « Document », puis attendez que le document soit créé et ouvert

Une fois dans l'espace de travail, vous verrez les onglets « Studio de pièces » et « Assemblage » en bas (cliquez sur le signe plus à droite des onglets pour en créer de nouveaux) :

- **Studio de pièces** : la zone de modélisation d'une pièce individuelle (correspondant aux étapes d'esquisse et de pièce d'un flux de travail CAO) ; les pièces y sont réalisées à l'aide de contraintes d'esquisse
- **Assemblage** : la zone d'assemblage des pièces réalisées dans les studios de pièces ou de pièces prêtes à l'emploi issues de bibliothèques (correspondant à l'étape d'assemblage d'un flux de travail CAO)

Un document peut contenir un nombre quelconque d'assemblages et de studios de pièces. Pour faciliter la modification et la gestion, veillez à ne modéliser qu'une seule pièce par studio de pièces dans la mesure du possible ; assemblez le robot par sous-systèmes, puis réunissez le tout dans un assemblage général.

### Flux de travail de base de la modélisation

Ce guide d'initiation ne présente que les opérations et flux de travail les plus fondamentaux d'Onshape.

#### Tracé d'esquisses

Dans un studio de pièces, créez une esquisse, choisissez un plan, dessinez le contour à l'aide des outils d'esquisse (lignes, rectangles, cercles…), puis fixez la géométrie grâce aux cotes et aux contraintes géométriques (horizontale, verticale, tangente…). Visez une esquisse entièrement contrainte afin que les fonctions suivantes soient fiables.

#### Création de pièces

Une fois l'esquisse terminée, utilisez des fonctions telles que l'extrusion, la révolution et le balayage pour transformer le profil 2D en solide 3D, puis affinez la pièce avec des perçages, des chanfreins et des congés. Toutes les fonctions sont enregistrées dans l'ordre dans la liste des fonctions et peuvent être annulées ou modifiées à tout moment.

#### Assemblage de pièces

Dans un assemblage, insérez les pièces réalisées dans les studios de pièces ou des pièces prêtes à l'emploi issues de bibliothèques, et reliez-les à l'aide de Mates et de Mate Connectors. Une fois l'assemblage terminé, vérifiez que les mouvements sont fluides et qu'il n'y a pas d'interférences.

#### Utilisation des outils

Onshape propose des outils d'analyse tels que la mesure, la vue en coupe et les propriétés de masse, qui permettent de vérifier à tout moment les cotes et le poids pendant la modélisation ; le menu contextuel (clic droit) offre également des raccourcis tels que masquer, isoler et renommer.

### Résistance du modèle et conseils de conception

La résistance d'une pièce imprimée en 3D dépend du matériau et de la structure. Voici quelques concepts de conception structurelle couramment utilisés :

- **Pièces structurelles essentielles** (poutres, plaques structurelles, etc.) : imprimez-les de préférence en PETG-CF (paramètres dans le chapitre « Matériel & Construction »), avec une épaisseur d'au moins 4 mm
- **Pièces de guidage** (rails à billes, butées de structure, etc.) : le PLA convient, avec une épaisseur de paroi d'au moins 2 mm
- **Pièces décoratives protectrices** (panneaux latéraux, etc.) : épaisseur de paroi d'au moins 1,5 mm
- Pour les plaques ou structures fragiles telles que l'acrylique, évitez les perçages denses (espacement entre trous inférieur à 3 mm) ; les liaisons porteuses entre structures doivent avoir une largeur d'au moins 7 mm
- Évitez autant que possible les arêtes vives : arrondissez-les en congés afin d'éviter les concentrations de contraintes qui provoquent des ruptures

> [!info] Les valeurs ci-dessus sont données à titre indicatif ; les paramètres réels doivent être ajustés et validés sur des pièces physiques.

### Stratégie de conception et calendrier de saison

- Lors de la conception du robot, découpez les tâches du jeu en petits éléments, concevez séparément les structures de chaque élément, puis combinez-les
- Avant la modélisation formelle, consultez les autres membres de l'équipe sur le projet et concevez en fonction de la stratégie de score de l'équipe
- Une fois la modélisation complète du robot terminée, pensez au processus d'assemblage réel : prévoyez des accès d'assemblage pour les vis difficiles à installer et réservez de l'espace pour le passage des câbles
- Envisagez des structures modulaires pour faciliter les réparations et les optimisations ultérieures
- Pour la version finale, privilégiez une structure unifiée et réduisez les petites pièces superflues afin d'améliorer la résistance globale et la légèreté

**Calendrier de saison :**

- Sur le planning : la première conception peut être sommaire, mais elle doit être terminée et construite le plus vite possible afin de laisser du temps au débogage des programmes et à l'entraînement des Drivers, et de tester la structure pour l'optimiser par itérations ; avant les matchs de qualification, un robot qualifiable doit subir au moins 3 itérations (référence)
- Suivez l'actualité des équipes étrangères : la communauté FTC organise des événements comme « Robot in 30 Hours Reveal | FTC » au cours desquels les équipes peuvent partager à tout moment leurs nouveaux projets de saison ; vous pouvez aussi vous inspirer des projets des équipes FRC et VEX

### Ressources d'apprentissage Onshape

Plateforme de modélisation professionnelle, Onshape propose des ressources d'apprentissage officielles complètes : [https://learn.onshape.com/](https://learn.onshape.com/) ; de nombreux tutoriels sont également disponibles sur des plateformes vidéo comme Bilibili (哔哩哔哩) et YouTube.

- Les logiciels de CAO suivant des flux de travail similaires (esquisse, pièce, assemblage), les tutoriels d'autres logiciels comme SolidWorks ou Autodesk Fusion ont tout autant de valeur : ils aident à développer la perception des volumes des pièces et la familiarité avec les flux de travail de modélisation
- Gardez à l'esprit que la pratique prime sur la théorie : trouvez des modèles à reproduire sur Bilibili (哔哩哔哩), essayez d'abord de modéliser par vous-même et ne consultez le tutoriel qu'en cas de blocage. Dans la vie quotidienne, observez et réfléchissez à la façon dont les petites structures sont modélisées
- Pour la FTC, étudiez les excellentes solutions des autres équipes : la plupart des grandes équipes ont leur propre site web et publient leurs solutions en open source. Recherchez un numéro d'équipe FTC sur YouTube ou Google pour trouver leur site officiel, ou consultez les modèles d'autres équipes sur des sites comme CycleZLab

> [!info] En cas de question, demandez conseil à un ancien de la modélisation ou recherchez directement sur Internet.

### Bibliothèques de pièces FTC courantes

Fournisseurs de pièces FTC et plateformes de ressources couramment utilisés :

- **goBILDA** : fournit une gamme complète de pièces structurelles FTC
- **REV Robotics** : fournit des modules de commande électronique et des pièces structurelles
- **CycleZLab** : plateforme communautaire de robotique FIRST (archives de CAO, de code et de journaux de construction)

### Normes de conception

- Utilisez les unités métriques (mm)
- Prévoyez un jeu approprié pour toutes les pièces imprimées en 3D (0.2-0.3mm recommandé)
- Formats d'export : fichiers STEP pour l'usinage, fichiers STL pour l'impression 3D et fichiers 3MF pour le tranchage
