# Matériel & Construction

## 1. Informations de base

Voici les informations supplémentaires requises pour la construction.

### Applications

- Bambu Studio
- RD Works V8

### Comptes en ligne

- Adresse e-mail (nous recommandons une adresse @gmail.com ou @outlook.com)
- Bambu Studio — [https://bambulab.cn/](https://bambulab.cn/)
- Onshape — [https://www.onshape.com/](https://www.onshape.com/)
- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/)

---

## 2. Configuration de l'environnement

Voici l'environnement de travail à configurer avant de commencer. Veuillez suivre les instructions ci-dessous. En cas de question, consultez un administrateur.

### Navigateur web

Voici les sites à ajouter à vos favoris :

| Nom | Adresse |
|------|------|
| goBILDA | https://www.gobilda.com/ |
| REV Robotics | https://www.revrobotics.com/ |
| CycleZLab | https://www.cyclezlab.com/ |

### Bambu Studio

Bambu Studio est la solution d'impression 3D adoptée par notre équipe.

**Procédure d'inscription :**

1. Ouvrez [https://bambulab.cn/](https://bambulab.cn/), cliquez en haut à droite et créez un compte à l'aide d'un numéro de téléphone ou d'un autre moyen.

**Installation du logiciel et configuration de l'environnement :**

1. Ouvrez [https://bambulab.cn/zh-cn/download/studio](https://bambulab.cn/zh-cn/download/studio)
2. Téléchargez et installez la version adaptée à votre système.

**Points d'attention :**

- Sous Windows, vous pouvez modifier le répertoire d'installation, à condition que le chemin se termine par `..\Bambu Studio\`. Lors de l'installation, cochez « Ouvrir les fichiers .3mf avec Bambu Studio », « Ouvrir les fichiers .stl avec Bambu Studio » et « Ouvrir les fichiers .step/.stp avec Bambu Studio ».
- Sous macOS, glissez simplement `BambuStudio.app` dans le dossier Applications.
- Lancez Bambu Studio. Pour la région de connexion, sélectionnez « Chine continentale » ; pour les imprimantes, sélectionnez au moins **Bambu Lab P1S** et **Bambu Lab P2S** ; les matériaux peuvent rester à leur configuration par défaut. Cochez « Installer le plugin réseau Bambu ».
- Connectez-vous à votre compte Bambu à l'aide d'un numéro de téléphone ou d'un autre moyen.

### RD Works V8

> [!danger] **Remarque :** il est fortement déconseillé d'installer ce logiciel sous macOS, faute de quoi vous aurez besoin d'une machine virtuelle telle que Parallels Desktop, VMware Fusion ou CrossOver.

RD Works V8 est le logiciel pilote qui accompagne la découpeuse laser utilisée par notre équipe.

**Installation du logiciel et configuration de l'environnement :**

1. Obtenez le fichier d'installation `RDWorksV8Setup.exe` auprès d'un administrateur ou d'un mentor, ouvrez-le et cliquez sur « Install ».
2. Vous pouvez modifier le chemin d'installation en cochant « Localiser manuellement le chemin d'installation ».
3. Connectez votre ordinateur à la découpeuse laser et cliquez sur « Installer le pilote USB ».
4. Laissez les autres options à leurs valeurs par défaut.

---

## 3. Présentation du matériel

### Outils courants

> [!danger] Avant d'utiliser un quelconque outil à main, vérifiez impérativement son état (manche desserré, mors ébréchés, etc.) et portez, selon les besoins, des gants de protection ou des lunettes de protection.

> [!info] Seuls les outils les plus courants sont répertoriés ici. Les autres outils, moins utilisés, sont regroupés dans l'annexe « Liste des outils », qui sera enrichie au fil du temps.

#### Clé Allen (clé hexagonale)

Outil en forme de L ou de T dont la section est un hexagone régulier, utilisé pour serrer les vis et boulons à six pans creux. Insérez complètement l'une des extrémités (courte ou longue) dans l'empreinte hexagonale de la tête de vis : une rotation dans le sens horaire serre, une rotation dans le sens antihoraire desserre. Les clés à poignée en T offrent généralement un bras de levier plus important ou permettent de travailler dans des alésages profonds.

> [!info] Les tailles que nous utilisons le plus souvent sont les M3 et les M4 : ayez-les toujours à portée de main.

#### Douille

Outil de serrage cylindrique dont la paroi intérieure est hexagonale, capable d'englober un écrou ou une tête de boulon. Placez la douille à la verticale sur l'écrou et entraînez-la en rotation au moyen de la poignée. Son avantage réside dans sa grande surface de contact, qui évite les glissements, et dans son aptitude à travailler dans les zones étroites où une clé ordinaire ne peut pas tourner.

#### Clé à molette

Clé universelle dont l'ouverture est réglable dans une certaine plage, adaptée aux écrous hexagonaux de différentes tailles. Réglez l'ouverture en tournant la vis sans fin (molette) de la clé jusqu'à ce qu'elle épouse les plats de l'écrou. Veillez par ailleurs à ce que la mâchoire fixe supporte l'essentiel de la poussée ou de la traction, c'est-à-dire que la force soit exercée du côté de la mâchoire fixe, afin d'éviter d'endommager la clé ou de la faire glisser.

#### Pince plate

Pince dont les mors sont plats, généralement munie de fines dents à l'intérieur pour augmenter la friction. Elle sert à plier de fines tôles métalliques, à maintenir de petites pièces ou à fournir une traction d'appoint lors de l'assemblage.

#### Pince à bec long

Pince aux mors longs et fins, de forme conique, adaptée aux espaces de travail exigus. Elle sert couramment à saisir de petites pièces, à cintrer de fins fils ou à extraire des corps étrangers de circuits ou de structures denses. La base des mors comporte généralement une arête coupante, ce qui permet aussi de couper des fils.

#### Pince à dénuder

Outil spécialement conçu pour retirer la gaine isolante d'un fil sans endommager l'âme métallique. Choisissez l'encoche correspondant au diamètre du fil, placez le fil dans l'encoche, serrez les poignées, puis tournez légèrement en tirant vers l'extérieur pour retirer la gaine.

#### Marteau de charpentier (marteau à panne fendue)

Outil servant à frapper des objets pour les déplacer ou les déformer. Une extrémité du marteau de charpentier est plate et sert à frapper, l'autre forme un V destiné à arracher les clous. Tenez le manche par son extrémité pour obtenir un couple maximal. Lors de la frappe, veillez à ce que la face plane du marteau soit parallèle à la surface de l'objet visé, afin d'éviter tout glissement latéral.

#### Mètre ruban

Règle métallique flexible munie d'un mécanisme d'enroulement à ressort, utilisée pour mesurer des distances plus longues ou des dimensions non linéaires. Tirez le ruban, accrochez le crochet d'extrémité au bord de l'objet ou appuyez-le contre une surface de référence. Lisez les graduations puis, une fois la mesure terminée, appuyez sur le bouton de blocage ou laissez le rappel automatique enrouler le ruban. Notez que le crochet présente généralement un léger jeu : celui-ci compense son épaisseur afin que les mesures intérieures et extérieures donnent des lectures identiques.

#### Pied à coulisse

Le pied à coulisse se compose principalement d'une règle principale A et d'un vernier B coulissant le long de celle-ci.

- **Principe** : le pied à coulisse exploite la petite différence fixe entre la graduation unitaire de la règle principale (1 mm) et celle du vernier pour améliorer la précision de mesure. Les pieds à coulisse courants existent en trois variantes : 10, 20 et 50 divisions.
- **Lecture** : lisez d'abord la règle principale : repérez la position de la ligne zéro du vernier par rapport aux graduations de la règle principale. Lisez ensuite le vernier : déterminez quelle ligne de graduation du vernier coïncide avec une graduation de la règle principale. Combinez les deux lectures pour obtenir la longueur mesurée.
- **Utilisation** : lorsque les deux lames d'une mâchoire de mesure extérieure (intérieure) sont en contact, la ligne zéro du vernier coïncide exactement avec la ligne zéro de la règle principale. Serrez (ou enfilez) l'objet à mesurer entre ces deux lames : la somme des lectures de la règle principale et du vernier donne la longueur de l'objet.

#### Micromètre (palmer)

Dans un micromètre, l'enclume A et la graduation fixe B sont fixées sur la monture C ; la graduation mobile E, le bouton D et la molette de friction D' sont solidaires de la vis micrométrique F, qui est montée sur B par un filetage de précision.

- **Principe** : lorsque le bouton D effectue un tour complet, la vis F avance ou recule d'un pas le long de l'axe de rotation. Le pas de la graduation fixe B du micromètre est de 0.5 mm, et la graduation mobile E comporte 50 divisions égales sur la circonférence : chaque division de la graduation mobile correspond donc à une avance ou un recul de 0.01 mm de la vis micrométrique F. Le micromètre permet de mesurer avec une précision de 0.01 mm.
- **Lecture** : lisez d'abord la graduation B, en vérifiant si la ligne des demi-millimètres de B est visible ; lisez ensuite la graduation E, chaque division valant 0.01 mm. Combinez les lectures de B et de E pour obtenir la longueur mesurée.
- **Utilisation** : mettez d'abord F en contact avec A et alignez le bord gauche de E sur la ligne zéro de B ; placez l'objet à mesurer entre F et A et tournez D ; lorsque F est presque en contact avec l'objet, cessez d'utiliser D et passez à D' ; arrêtez dès que vous entendez un « clic », puis effectuez la lecture.

### Matériaux courants

#### Matériaux génériques

Disponibles auprès de toutes sortes de canaux :

- Vis et écrous divers
- Entretoises hexagonales
- Poulies de courroie crantée
- Roulements

> [!warning] Les axes ne font pas partie des matériaux génériques : leurs spécifications sont assez particulières ; achetez-les séparément selon les besoins réels du projet.

#### Matériaux spécifiques

Les produits officiels REV et goBILDA, ainsi que Zhou Yu, fournisseur de profilés spécifiques.

#### Caractéristiques des matériaux

| Marque | Caractéristiques |
|------|------|
| **REV** | Relativement ancienne mais essentielle. Les trois grands modules électroniques (Driver Hub, Control Hub, Expansion Hub) sont principalement des produits REV. Les pièces de structure comprennent divers profilés en aluminium (d'un usage relativement rare) ; les profilés peuvent servir de petits supports de butée ou à fixer des structures à déplacement non unitaire. Les profilés correspondent principalement aux vis à tête bombée M3 (uniquement), aux axes REX de 6 mm, aux engrenages et aux chaînes ; les moteurs transversaux 72:1 et les moteurs 40:1 sont les plus utilisables et les plus courants. |
| **goBILDA & Zhou Yu** | Poutres en C, poutres carrées ou minces, axes REX de 8 mm, connecteurs modulaires variés et fonctions de connexion complètes. Utilise principalement des vis M4 (10 mm officiels) ; les moteurs sont majoritairement de la série 5203. Convient aux kits de transmission directe du moteur. |

**Détails du fournisseur REV :**

- **Modules électroniques essentiels** : les trois grands modules Driver Hub, Controller Hub (c'est-à-dire Control Hub) et Expansion Hub sont principalement des produits REV.
- **Pièces de structure** : essentiellement des profilés en aluminium, d'un usage actuellement réduit ; ils peuvent servir de petits supports de butée ou à fixer des structures à déplacement non unitaire.
- **Vis spéciales** : les profilés REV utilisent des vis M3 à tête bombée (six pans creux), qui s'encastrent dans le profilé en aluminium ; presque seuls les profilés REV en font usage.
- **Spécification des axes** : REV correspond aux axes REX de 6 mm, une spécification propre à REV.
- **Moteurs** : REV propose le moteur transversal 72:1 (nom officiel Core Hex, sortie transversale à 90° et sans arbre de sortie intégré) et le moteur standard 40:1 (nom officiel HD Hex). Le moteur transversal 72:1 offre des solutions de montage particulières, mais sa conception est ancienne et il est difficile, dans l'environnement actuel, de lui trouver des pièces adaptées.
- **Engrenages et chaînes** : REV en fournit également, mais les produits goBILDA sont généralement privilégiés.

**Détails du fournisseur goBILDA :**

- **Poutres en C** : elles se divisent en poutres carrées et poutres minces. Les poutres carrées conviennent aux grandes structures d'ossature telles que les châssis ; les poutres minces conviennent aux liaisons en portée.
- **Connecteurs** : une large gamme de connecteurs standardisés, fortement modulaires, avec des fonctions de connexion complètes avec leurs propres matériaux comme avec ceux de REV.
- **Spécification des vis** : principalement des vis M4 ; la version officielle est une vis à tête bombée M4×10 mm.
- **Spécification des axes** : correspond aux axes REX de 8 mm.
- **Moteurs** : la série 5203 est couramment utilisée, adaptée à la transmission directe standard. Grâce à la résistance de l'axe REX de 8 mm et aux caractéristiques de montage des moteurs, goBILDA est le kit adapté à la transmission directe du moteur.

**Détails du fournisseur Zhou Yu :**

> [!warning] Chez Zhou Yu, on trouve la grande majorité des matériaux correspondant à goBILDA, avec toutefois des différences. Utilisez autant que possible les pièces officielles goBILDA ; Zhou Yu est moins cher, mais des problèmes de qualité sont possibles.

- La grande majorité des matériaux trouvent chez Zhou Yu un produit du même type que goBILDA.
- Zhou Yu fabrique également certaines pièces spéciales conçues selon les besoins du marché intérieur ; certaines n'ont pas d'équivalent chez goBILDA. Si vous rencontrez une pièce Zhou Yu ingénieuse, vous pouvez l'acheter pour la tester.
- Côté prix, Zhou Yu est le moins cher des trois fournisseurs, mais la qualité de fabrication est légèrement inférieure à celle de goBILDA.

#### Filaments d'impression 3D

| Type | Température d'impression (approx.) | Description |
|------|------|------|
| PLA | 220°C | Filament plastique standard de base |
| PETG-CF | 240+°C | Filament plastique renforcé de carbone |

Achetez des filaments officiels Bambu Lab ou SUNLU : leur qualité est relativement stable.

**Retrait :**

- En règle générale, le retrait du PLA n'est pas un problème à prendre en compte.
- Lors de l'impression de bagues, un retrait d'environ 5 % du diamètre peut apparaître : il convient de le mesurer en fonction de la forme imprimée.
- Le retrait du PETG-CF fluctue fortement sous l'influence du temps, de la température, du lot et d'autres facteurs ; avant utilisation, il est conseillé de fabriquer une petite pièce de test simple, conforme à la géométrie de la pièce, pour mesurer le retrait.

#### Matériaux de découpe laser

| Matériau | Caractéristiques | Usage |
|------|------|------|
| Plaque acrylique | Résistance élevée | Plaques porteuses à grande portée |
| Plaque PP | Grande ténacité | Pièces de protection ; nécessite davantage de points de fixation ; peut encaisser des chocs directs |
| Bois | Faible coût | Sujet au gauchissement ; à réserver à des cas particuliers |

> [!info] Les propriétés intrinsèques des matériaux sont consignées ici de façon permanente. Les paramètres de procédé de la découpe laser (puissance, vitesse, etc.) figurent dans l'annexe et sont mis à jour en continu.

#### Câblage

**Câbles d'alimentation :**

- Câble de liaison batterie–Hub (selon les besoins de conception, la batterie peut être reliée directement au Control Hub ou à l'Expansion Hub)
- Câble de liaison Con–EXP
- Interrupteurs avec leur propre câblage
- Câbles d'alimentation des moteurs : pour les moteurs goBILDA, le connecteur d'alimentation n'est pas compatible avec le Hub ; il faut couper le connecteur d'origine et refabriquer la prise à l'aide d'un embout de sertissage.

**Câbles de données (câbles d'encodeur de moteur) :**

- Pour goBILDA, le connecteur et l'ordre des fils diffèrent de ceux du Hub (les fils jaune et blanc sont intervertis) : une attention particulière est requise lors de la fabrication.
- Câbles de capteur I2C : aucune exigence particulière.
- Câbles de données Con et EXP.
- Rallonges de servo : attention au sens.

**Câbles pour appareils hôtes :**

- Connexion du Hub à l'ordinateur : le Control Hub utilise un câble USB-A vers USB-C, l'Expansion Hub un câble mini USB.
- Autres : câbles de conversion USB-A vers USB-C, USB-A vers miniUSB, USB-C vers miniUSB, etc.
- Câble réseau (peut servir de connexion réseau auxiliaire ; non indispensable).
- Câble de données de la manette (USB-A vers microUSB).

**Infrastructure (traitée comme consommable) :**

- Le WiFi, la vidéosurveillance, les câbles réseau, les multiprises et autres infrastructures sont gérés comme des consommables ; veillez à les réapprovisionner à temps.
---

## 4. Flux de travail

1. **Achat des pièces**
2. **Fabrication des pièces sur mesure**
   - Fabrication de pièces imprimées en 3D
   - Découpe laser de plaques
3. **Montage du matériel**
4. **Câblage électrique**
5. **Rédaction de la configuration du robot (Robot Configuration)** (en coordination avec la programmation)
6. **Connexion entre la Driver Station et le Robot Controller** (en coordination avec la programmation)

### Montage du matériel

#### Ordre de montage

> [!warning] L'assemblage manuel d'un robot commence habituellement par le châssis, puis s'élève couche par couche. Mais sur un robot de compétition, nous disposons de plans de modélisation : cet ordre entraîne facilement de nombreux retours en arrière, car certaines pièces en masquent d'autres.

- Ajustez l'ordre de montage en fonction des relations de masquage entre les pièces : **montez d'abord les pièces masquées par les moteurs, l'électronique et les autres composants**, puis installez les composants qui les masquent.
- Par exemple : terminez l'installation de toutes les pièces nécessaires autour d'un moteur avant de monter ce moteur.

#### Précautions d'utilisation des pièces

- Sur les axes, évitez de privilégier les modèles équipés de vis de pression (vis sans tête) : ces vis endommagent les axes.
- Ne serrez pas excessivement les vis.
- Les autres règles d'utilisation des pièces seront complétées au fur et à mesure.

#### Prévoir l'accès pour les réparations

- Ne cherchez jamais la facilité lors du montage : ne cachez pas les vis et les écrous dans des endroits difficiles d'accès.
- Respectez toujours le principe de « faciliter la réparation » : si une panne exige le démontage complet du robot, la compétition ne pourra pas continuer.

#### Protection contre l'électricité statique

- Par temps sec, l'électricité statique se forme facilement ; elle peut provoquer la déconnexion du robot et des données de capteurs imprécises.
- Mesures de protection : installez un fil de mise à la terre sur le robot pour évacuer l'électricité statique vers le sol ; enveloppez l'IMU et les autres capteurs dans du papier aluminium pour les protéger de l'électricité statique.

#### Gestion des câbles

- Les structures télescopiques à rails coulissants doivent être équipées de gaines de câbles, afin d'éviter que les fils ne s'envolent, ne bloquent les rails ou ne soient arrachés.
- La gestion des câbles est le travail le plus technique du montage : traitez-la avec le plus grand soin.

### Câblage électrique

#### Connexion entre le Control Hub et l'Expansion Hub

- **Connexion d'alimentation** : branchez le connecteur mâle dans le connecteur femelle.
- **Connexion de données** : utilisez les ports RS-485 avec un câble à 3 broches. Chaque côté possède 2 ports RS-485 : branchez-en un de chaque côté, sans correspondance de position obligatoire.

> [!warning] Les connecteurs officiels sont tous dotés d'un détrompage : ce dispositif évite les mauvais branchements, mais pas l'obstination. Si un connecteur ne s'insère pas, vérifiez immédiatement le sens d'insertion et ne forcez jamais.

#### Connexion entre la Driver Station et le Robot Controller

Pour la connexion réseau, l'équipe structure et l'équipe programmation doivent toutes deux la maîtriser : vous pouvez réutiliser directement le contenu de la partie programmation.

#### Rédaction de la configuration du robot (Robot Configuration)

La rédaction du fichier de configuration relève de la collaboration entre la structure et la programmation : reportez-vous à la partie programmation.

---

## 5. Initiation à la construction

### Installation et configuration de Bambu Studio

Téléchargez puis installez en cliquant sur « Suivant » ; faites attention au choix de l'emplacement d'installation, un dossier est créé automatiquement.

**Remarques :**

- Toutes les cases doivent être cochées
- Au lancement, suivez le guide d'enregistrement et sélectionnez la Chine continentale
- Sélectionnez uniquement la P1S et la P2S
- Conservez la sélection de matériaux par défaut
- Installez le plugin réseau
- Connectez-vous ou inscrivez-vous dans le coin supérieur gauche (numéro de téléphone ou compte tiers)

### Export des modèles depuis Onshape

1. Ouvrez le fichier de modélisation et sélectionnez la pièce cible : le coin inférieur gauche indique la position de cette pièce dans la liste des instances à gauche.
2. Faites un clic droit sur cette pièce, choisissez de basculer vers l'espace de travail correspondant à cette instance, puis entrez dans la zone de construction de la pièce.
3. Dans le coin inférieur gauche, faites un clic droit à l'emplacement de la liste des pièces et choisissez d'exporter.
   - Remarque : l'option d'export n'apparaît qu'après avoir obtenu le droit de modification du document.
4. Changez le format en STEP, modifiez le nom du fichier selon vos besoins et laissez les autres options par défaut.

### Import et disposition dans Bambu Studio

- Créez un nouveau projet dans Bambu Studio, cliquez sur le bouton « Importer » en haut pour importer le fichier STEP, puis confirmez simplement les options d'import par défaut.
- Si la position des pièces ne correspond pas à vos attentes, désélectionnez toutes les pièces, faites un clic droit sur le plateau d'impression et choisissez « Arrangement automatique » ou « Orientation automatique ».
- Ajustement manuel : sélectionnez la pièce, maintenez le bouton gauche enfoncé et faites-la glisser pour la déplacer ; cliquez sur le bouton de rotation pour la faire pivoter en mode relatif ou absolu.
- Différence de logique d'opération : par défaut, Bambu Studio fonctionne comme Onshape — le glisser avec le bouton gauche fait pivoter la vue, et le glisser avec le bouton droit déplace la vue ; si vous n'êtes pas habitué, vous pouvez modifier le mode d'opération de la vue dans les paramètres. Une fois une pièce sélectionnée, le glisser avec le bouton gauche permet de la déplacer directement.

### Paramètres d'impression

**Choix de l'imprimante et du filament :**

| Imprimante | Buse | Filament |
|--------|------|------|
| P1S (buse d'origine) | 0.4 mm | PLA Basic |
| P1S (buse remplacée, dédiée au filament carbone) | 0.6 mm | PETG-CF |
| P1S (les deux unités) | 0.4 mm | PLA Basic |

**Choix des paramètres selon le type de pièce :**

| Type | Paramètres |
|------|------|
| Pièces décoratives | Paramètres par défaut de Bambu Studio |
| Pièces structurelles non porteuses | Configuration courante du groupe de modélisation |
| Pièces structurelles porteuses | Configuration courante du groupe de modélisation (haute résistance) |

> [!info] Les paramètres ci-dessus sont les configurations courantes de notre équipe : vous pouvez les modifier vous-même en cas de besoins particuliers.

**Disposition de plusieurs pièces :**

- Plusieurs pièces identiques sur le même plateau d'impression : sélectionnez la pièce, faites un clic droit et choisissez « Dupliquer ».
- Pour ajouter différentes pièces : cliquez à nouveau sur le bouton « Importer » pour les importer.

### Connexion à l'imprimante 3D

- Rendez-vous dans l'onglet « Appareil » : après avoir activé le mode LAN, le logiciel détecte automatiquement les imprimantes du réseau local (l'activation du mode LAN peut déconnecter le compte actuellement connecté, vous pouvez ignorer ce message).
- Si l'imprimante cible n'est pas détectée : vérifiez d'abord que le mode LAN est activé sur l'imprimante ; si elle reste invisible, liez-la manuellement via IP + code d'accès. L'IP se trouve dans la page WiFi des paramètres de l'imprimante, et le code d'accès s'affiche à l'emplacement de l'avatar de connexion une fois le mode LAN activé.
- Après le tranchage (slicing), vérifiez dans l'onglet « Aperçu » ; avant d'imprimer, il est recommandé d'envoyer l'aperçu du tranchage au responsable actuel de la modélisation ou de la structure pour confirmer que la configuration est correcte, avant de lancer l'impression.

### Réglages d'impression

**Imprimante P2S :**

- Activez le time-lapse avant l'impression.
- Le nivellement automatique du plateau doit impérativement être activé.
- Sélectionnez le filament chargé et l'imprimante cible correspondants.

**Imprimante P1S :**

- Le time-lapse peut rester désactivé par défaut.
- Le nivellement automatique du plateau et la calibration dynamique du débit doivent tous deux être réglés sur automatique.

### Gestion des échecs d'impression

- **P2S** : dotée de la détection de spaghettis par IA. En cas de spaghettis (échec spaghetti), c'est-à-dire lorsque le filament vole dans tous les sens, l'appareil arrête automatiquement l'impression et envoie un rappel au compte connecté à l'appareil. Une fois le fichier défaillant nettoyé, l'appareil redémarre automatiquement.
- **P1S** : ne possède pas de détection automatique des spaghettis : il faut surveiller l'état en temps réel pendant l'impression. Si des spaghettis apparaissent, arrêtez manuellement l'impression ; vous pouvez retrouver le fichier défaillant dans les fichiers d'impression historiques du dossier cache à gauche et le nettoyer.

### Installation et configuration de RD Works V8

**Procédure d'installation :**

1. Obtenez le fichier d'installation exe auprès d'un administrateur ou d'un enseignant référent, puis choisissez Install
2. Cochez le chemin d'installation manuel pour modifier l'emplacement
3. Les autres options peuvent rester par défaut
4. Une fois connecté à la découpeuse laser, choisissez d'installer le pilote USB
5. Fermez puis rouvrez le logiciel pour terminer
