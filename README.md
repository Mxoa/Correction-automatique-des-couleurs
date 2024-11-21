
# Description des Commandes

Ces commandes permettent d'appliquer deux méthodes de traitement d'image : **`interpolation`** et **`ace`**. Chaque méthode utilise des arguments spécifiques pour ajuster ses paramètres.

---

## Format Général

1. **Fichier_source** : Chemin vers l'image d'entrée.
2. **Fichier_cible** : Chemin où enregistrer l'image traitée.
3. **Alpha** : Paramètre de pondération.
4. **Scaling_fonction** : Booléen (`True` ou `False`) pour appliquer une mise à l'échelle des résultats selon gw_wp.
5. **Lab** : Booléen (`True` ou `False`) pour indiquer si l'image est traitée dans l'espace Lab (au lieu de RGB).
6. **Omega** : Fonction de distance utilisée :
   - `Ed` : Distance Euclidienne.
   - `Ed2` : Distance Euclidienne quadratique.
   - `Manhattan` : Distance de Manhattan.

---

## Méthode : `interpolation`

Cette méthode applique une interpolation des couleurs pour améliorer l'image.

### Format

ace Fichier_source Fichier_cible Alpha Scaling_fonction Lab Omega Randomly{True|False} Nb_points{int}
ace images/article/fenetre_color.png images/resultats/interpolation/fenetre_color_alpha4_ed.png 4 False False Ed True 50
