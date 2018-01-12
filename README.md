# Seam Carving

## Introduction
Le but de ce projet est de redimensionner l’image sans perte du contenu significatif lors du redimensionnement. On applique le filter gradient (déterminée avec le filtre sobel) sur l'image pour déterminer le chemin le moins important.

## Description détaillée de l'algorithme 

**1. Appliquer le filtre gradient:** <br>
Dans un premier lieu on a essayer de calculer l'energie de l'image en utilisant des differents methodes de calcule notament celle qu'on a dans l'énoncé du projet, mais ces methodes sont tres couteuses en temps d'excutions du coups on a decide de chercher d'autres methodes qui font le meme travaille mais en moins du temps, on a trouver qu'on peut utiliser le filtre gradient(sobel) qu'on a vu dans le cours du tritemant d'image qui nous a permis d'economiser un tiers du temps d'excutions.

![sobel image](/images/seamCC.png)

**2. Trouver le chemin minimale:** <br>
Pour chaque pixel dans l'image d'energie(image apres le filtre sobel) on prend le pixel avec l'energie minimal entre les pixels (en bas à gauche, en bas au centre et en bas à droite) dans le cas du seam carving vertical

**3. Enlever le chemin minimale:** <br>
La suppression du chemin minimal.

**4. Répétez les étapes 1 à 3 jusqu'à atteindre la taille souhaitée**


## Les libraries à installer :
Les bibliothèques utilisées PIL, scipy, numpy, tkinter.

## Les méthodes utilisées :
**filter_gradient (img)** : renvoie l'opérateur Sobel appliqué à l'image img (implémentation rapide)<br>
**img_transpose (im)** : renvoie la transposition d'un objet image im<br>
**chercher_chemin_horizontal (im)** : trouve le chemin horizontal d'énergie le plus bas dans une image en niveaux de gris<br>
**chercher_chemin_vertical (im)** : trouve le chemin vertical d'énergie le plus bas dans une image en niveaux de gris<br>
**supp_chemin_horizontal (img, path)** : supprime tous les pixels d'un chemin horizontal depuis l'image img<br>
**supp_chemin_vertical (img, path)** : supprime tous les pixels d'un chemin vertical depuis l'image img<br>
**Run (input, resolution)** : est la méthode principales du programme<br>

## Comment lancer le projet :
Il suffit de choisir une image en cliquant sur le menu item "Ouvrir une image" :

![interface](/images/lancerApp-1.jpg)

Après le chargement de l'image, pour appliquer le seamcarving il faut redimensionner la fenêtre.


## Résultat 1
### Image Originale
![Image Originale](/images/ski.jpg)

### Après seam carving vertical
![Après seam carving vertical](/images/Capture.JPG)

## Résultat 2
### Image Originale
![Image Originale](/images/loutres.jpg)

### Après seam carving horizental
![Après seam carving horizental](/images/Capture2.JPG)


## Résultat 3
### Image Originale
![Image Originale](/images/pont.jpg)

###  Après seam carving hybride
![Après seam carving hybride](/images/Capture3.JPG)

## Sources :
- https://fr.wikipedia.org/wiki/Seam_carving
- https://stackoverflow.com/questions/tagged/seam-carving
- https://openclassrooms.com/courses/apprenez-a-programmer-en-python/des-interfaces-graphiques-avec-tkinter
- https://fr.wikipedia.org/wiki/Filtre_de_Sobel

