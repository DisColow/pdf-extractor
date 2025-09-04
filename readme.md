Bien sûr 🙂 Je vais te rédiger un **README** clair et structuré pour ton script Python `extract_first_pages.py`.
Je vais l’écrire en **Markdown** pour qu’il soit compatible avec GitHub, GitLab ou tout éditeur moderne.

---

## **README.md**

# 📄 Extract First Page from PDFs

Ce script Python permet d'extraire **la première page** de **tous les fichiers PDF** présents dans un répertoire et d'enregistrer chaque page extraite dans un nouveau fichier PDF.  
Les fichiers générés sont stockés dans un dossier `out` créé automatiquement à côté du script.

---

## 🚀 Fonctionnalités

- Parcourt automatiquement tous les fichiers **.pdf** du répertoire courant.
- Extrait **uniquement la première page** de chaque PDF.
- Crée un dossier `out` pour stocker les fichiers extraits.
- Conserve le **nom d'origine** de chaque fichier.
- Gère les erreurs et ignore les fichiers vides.

---

## 📦 Installation

### 1. Cloner ou télécharger le projet
Télécharge le fichier `extract_first_pages.py` et place-le dans un dossier contenant les PDF à traiter.

### 2. Installer les dépendances
Le script utilise la bibliothèque **PyPDF2**. Installe-la via pip :

```bash
pip install PyPDF2
````

---

## 🛠️ Utilisation

### 1. Placer les fichiers PDF

Mets tous les fichiers `.pdf` que tu veux traiter dans le **même dossier** que `extract_first_pages.py`.

### 2. Lancer le script

Exécute le script depuis un terminal :

```bash
python extract_first_pages.py
```

### 3. Récupérer les fichiers extraits

Les fichiers PDF contenant la première page seront créés dans un dossier `out` situé à côté du script.

---

## 📂 Exemple d'arborescence

Avant exécution :

```
📂 mon_dossier
 ├── extract_first_pages.py
 ├── fichier1.pdf
 ├── fichier2.pdf
 ├── fichier3.pdf
```

Après exécution :

```
📂 mon_dossier
 ├── extract_first_pages.py
 ├── fichier1.pdf
 ├── fichier2.pdf
 ├── fichier3.pdf
 └── 📂 out
      ├── fichier1.pdf
      ├── fichier2.pdf
      ├── fichier3.pdf
```

---

## ⚠️ Limitations

* Seule **la première page** de chaque fichier PDF est extraite.
* Les fichiers PDF vides sont ignorés.
* Si un fichier PDF est corrompu, il sera signalé mais non traité.

---

## 🧩 Améliorations possibles

* [ ] Permettre de choisir le dossier source et le dossier de sortie.
* [ ] Extraire plusieurs pages au lieu d'une seule.
* [ ] Ajouter une interface graphique simple.
* [ ] Gérer les fichiers PDF protégés par mot de passe.