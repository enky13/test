#!/usr/bin/env python3

import numpy as np

def create_3d_matrix(x, y, z, fill_method='sequential'):
    """
    Crée une matrice 3D de dimensions (x, y, z)
    avec différentes méthodes de remplissage
    """
    if fill_method == 'sequential':
        # Crée une matrice avec des nombres séquentiels
        return np.arange(x * y * z).reshape((x, y, z))
    elif fill_method == 'random':
        # Crée une matrice avec des nombres aléatoires entre 0 et 100
        return np.random.randint(0, 100, size=(x, y, z))
    else:
        # Par défaut, crée une matrice de zéros
        return np.zeros((x, y, z))

def main():
    # Dimensions de la matrice
    x, y, z = 3, 4, 5
    
    # Création d'une matrice avec des nombres séquentiels
    matrix_seq = create_3d_matrix(x, y, z, 'sequential')
    print("1. Matrice avec des nombres séquentiels:")
    print(matrix_seq)
    print("\nForme de la matrice:", matrix_seq.shape)
    
    # Création d'une matrice avec des nombres aléatoires
    matrix_rand = create_3d_matrix(x, y, z, 'random')
    print("\n2. Matrice avec des nombres aléatoires:")
    print(matrix_rand)
    
    # Démonstration des opérations sur les matrices
    print("\n3. Opérations sur la matrice séquentielle:")
    print("- Somme de tous les éléments:", matrix_seq.sum())
    print("- Moyenne des éléments:", matrix_seq.mean())
    print("- Valeur maximale:", matrix_seq.max())
    print("- Valeur minimale:", matrix_seq.min())
    
    # Accès aux tranches (slices)
    print("\n4. Tranches de la matrice:")
    print("- Première tranche (plan x-y à z=0):")
    print(matrix_seq[:, :, 0])
    print("\n- Tranche centrale (plan y-z à x=1):")
    print(matrix_seq[1, :, :])
    
    # Opérations mathématiques
    print("\n5. Opérations mathématiques:")
    print("- Multiplication par 2:")
    print(matrix_seq * 2)
    
    # Recherche d'éléments
    print("\n6. Recherche d'éléments:")
    print("- Position des éléments > 30:", np.where(matrix_seq > 30))
    
if __name__ == "__main__":
    main() 