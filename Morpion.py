# Programme pour calculatrice casio graph math+ lycée
# Il reproduit le jeu du morpion ou tic-tac toe

from casioplot import *

#Fonction qui fait un carré
def draw_square(x, y):
    taille = 30
    for i in range(taille+1):
        set_pixel(x + i, y, (0, 0, 0))          # Ligne du haut
        set_pixel(x + i, y + taille, (0, 0, 0))  # Ligne du bas
        set_pixel(x, y + i, (0, 0, 0))          # Ligne de gauche
        set_pixel(x + taille, y + i, (0, 0, 0))  # Ligne de droite

#Fonction qui fait une croix
def draw_cross(x, y):
    taille = 30
    for i in range(taille+1):
        # Première diagonale (haut-gauche vers bas-droit)
        set_pixel(x + i, y + i, (0, 0, 0))
        # Deuxième diagonale (bas-gauche vers haut-droit)
        set_pixel(x + i, y + taille - i, (0, 0, 0))

#Foncion qui fait la ligne horizontale
def horizontal_line(x_debut, x_fin, y):
    for x in range(x_debut, x_fin):
        set_pixel(x, y, (0, 0, 0))

#Fonction qui fait la ligne verticale
def vertical_line(y_debut, y_fin, x):
    for y in range(y_debut, y_fin):
        set_pixel(x, y, (0, 0, 0))

#Fonction qui supprime l'ancien plus (+)
def clear_plus(x, y):
    # Efface la zone du + en blanc (9x12 pixels)
    for px in range(9):
        for py in range(12):
            set_pixel(x + px, y + py, (255, 255, 255))

#Fonction qui vérifie si il y a une victoire
def verifier_victoire(grille):
    # 1. Vérifier les lignes
    for l in range(3):
        if grille[l][0] == grille[l][1] == grille[l][2] and grille[l][0] != "":
            return grille[l][0]

    # 2. Vérifier les colonnes
    for c in range(3):
        if grille[0][c] == grille[1][c] == grille[2][c] and grille[0][c] != "":
            return grille[0][c]

    # 3. Vérifier la diagonale haut-gauche vers bas-droit
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != "":
        return grille[0][0]

    # 4. Vérifier la diagonale haut-droit vers bas-gauche
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != "":
        return grille[0][2]

    return None

#Fonction qui vérifie si il y a une égalité
def grille_pleine(grille):
    for l in range(3):
        for c in range(3):
            if grille[l][c] == "":
                return False  # Il reste au moins une case vide
    return True  # Tout est rempli

# --- FONCTION DU MORPION ---
def morpion():
    # 1. Point d'apparition du curseur (+)
    ligne = 1
    colonne = 1

    # 2. Mémoire et tour
    grille = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    tour = 0

    # 3. Mise en place de la grille
    clear_screen()
    horizontal_line(117, 267, 70)
    horizontal_line(117, 267, 120)
    vertical_line(20, 170, 167)
    vertical_line(20, 170, 217)

    # 4. Apparition du curseur
    x = 137 + (colonne * 50)
    y = 37 + (ligne * 50)
    draw_string(x, y, "+")
    show_screen()


    while True:
        # 5. Attendre la pressio d'une touche
        t = getkey()

        # 6. Mise en mémoire de l'ancienne position du curseur
        old_ligne = ligne
        old_colonne = colonne

        # 7. Action à faire en fonction de la touche préssée
        if t == 14 and ligne > 0:      # Haut
            ligne -= 1
        elif t == 34 and ligne < 2:    # Bas
            ligne += 1
        elif t == 23 and colonne > 0:  # Gauche
            colonne -= 1
        elif t == 25 and colonne < 2:  # Droite
            colonne += 1            
        elif t == 95:                  # Touche EXE pour poser un pion
            if grille[ligne][colonne] == "":
                if tour % 2 == 0:
                    grille[ligne][colonne] = "square"
                else:
                    grille[ligne][colonne] = "cross"                
                tour += 1

                pos_x = 127 + (colonne * 50)
                pos_y = 30 + (ligne * 50)
                
                if grille[ligne][colonne] == "square":
                    draw_square(pos_x, pos_y)
                else:
                    draw_cross(pos_x, pos_y)
                show_screen()
        
                # 8. Vérification fin de partie
                gagnant = verifier_victoire(grille)
                if gagnant or grille_pleine(grille):
                    choix = 0  # 0 = Rejouer, 1 = Quitter                    
                    while True:
                        clear_screen()
                        
                        if gagnant == "square":
                            draw_string(110, 80, "Carres gagnent!")
                        elif gagnant == "cross":
                            draw_string(110, 80, "Croix gagnent!")
                        else:
                            draw_string(130, 80, "Egalite !")

                        if choix == 0:
                            couleur_rejouer = (0, 255, 0)
                            couleur_quitter = (0, 0, 0)
                        else:
                            couleur_rejouer = (0, 0, 0)
                            couleur_quitter = (0, 255, 0)
                            
                        draw_string(80, 150, "Rejouer", couleur_rejouer)
                        draw_string(250, 150, "Quitter", couleur_quitter)
                        show_screen()
                        
                        t_menu = getkey()
                            
                        if t_menu == 23:
                            choix = 0
                        elif t_menu == 25:
                            choix = 1
                        elif t_menu == 95:
                            if choix == 0:
                                return True   # Renvoie "True" pour dire relancer
                            else:
                                return False  # Renvoie "False" pour dire quitter
        # 9. Effacer l'ancien curseur (+)
        if ligne != old_ligne or colonne != old_colonne:
            old_x = 137 + (old_colonne * 50)
            old_y = 37 + (old_ligne * 50)
            
            clear_plus(old_x, old_y)
            if grille[old_ligne][old_colonne] == "square":
                draw_square(old_x-10, old_y-7)
            elif grille[old_ligne][old_colonne] == "cross":
                draw_cross(old_x-10, old_y-7)

            new_x = 137 + (colonne * 50)
            new_y = 37 + (ligne * 50)
            draw_string(new_x, new_y, "+")

            show_screen()

# --- BOUCLE PRINCIPALE DU JEU ---
# Permet la gestion de rejouer et quitter
while True:
    continuer = morpion() # Relance une partie
    if not continuer: # Affiche ensuite l'écran de fin
        break 

# Ecran de fin
clear_screen()
draw_string(115, 90, "Appuyer sur : AC")
show_screen()