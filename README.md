# Correction-automatique-des-couleurs
Mise en place d'un algorithme de Correction automatique des couleurs.

# Définitions article 1

- **Color consistency** : Capacité de notre cerveau à reconnaître les couleurs malgré la fluctuation de la lumière
- **White Patch Mechanism** : Pour atteindre la consistence des couleurs, *dans certains cas*, le cerveau humain peut vouloir normaliser les couleurs pour que la zone la plus claire de l'image devienne blanche.
- **Gray World Mechanism** : Parfois les images peuvent être légèrement orientées vers une couleur particulière. Ce mécanisme va rendre chaque couleur aussi puissante que ses sœurs.
- **Dynamic Range** : Dynamique de l'image, c'est à dire la capacité de représentation de différentes luminosités. La Dynamique oculaire est très performante comparée à la dynamique mécanique.
- **Lateral inhibition** : Capacité humaine à contraster. Les neurones inhibent leurs voisines.
- **$R_c$ scaling et WP/GW scaling** : Le scaling permet de profiter de l'intégralité de la dynamique de l'image, il y a le scaling normal $min R_c \rightarrow 0$  et $max R_c \rightarrow 255$ et le scaling WP/GW, plus efficace $max R_c \rightarrow 255$ et $0 \rightarrow 127.5$.


# Définitions article 2

- **Histogram Equalization** : Méthode d'uniformisation de l'histogramme.
- **Circular convolution** : Le fait d'avoir périodisé l'image permet de définir une nouvelle distance, périodique, qui va permettre de faire apparaître une convolution dans la formule de $R(x)$.
- **Polynomial Approximation** : Technique selon laquelle nous approchons $s_\alpha$ par un polynôme pour faire apparaître une convolution
- **Interpolation** : Approche pour faire apparaître une formule de convolution dans $R(x)$, qui consiste à séparer le domaine de $x \rightarrow I(x)$ en $J$ étages $L_1, L_2, ...$, ainsi, pour l'étage $j$, $I$ est constant et donc apparaît naturellement une convolution dans la formule de $R_c$.

# Implémentation

- Coder une fonction qui calcule la moyenne des couleurs pour vérifier l'hypothèse Gray World.
- Coder une fonction qui permet de détecter le code RGB de la zone la plus lumineuse
- Coder une fonction $R_c(p, r, d)$ suivant : avec $\alpha_p$ une constante de normalisation $$ R_c(p) = \alpha_p \sum_{j \in S} \omega(p-j) \cdot r(I_c(p) - I_c(j))$$
- Implémenter $O_c(p)$
- Tester les deux méthodes d'amélioration de l'algorithme (Approximation polynomiale et Interpolation)
- Chercher les bibliothèques python pour manipuler les polynômes
# Remarques

- La fonction $r$ testée la plus efficace pour le white patch est la fonction signe.
- Si une couleur est naturellement dominante sur l'image, alors nous aurons des problèmes avec la méthode ACE qui va avoir tendance à se rapprocher du Gray World.

# Questions
- Saturation de $r$ ?
- Pourquoi $r(\cdot)$ doit être impaire ?
- Comment calculer $\Delta E$ ?
- La méthode *LLL*
- Produit tensoriel ?
- C'est quoi $k$ ?
- Pourquoi la pente infinie est équivalente à l'égalisation de l'histogramme ?