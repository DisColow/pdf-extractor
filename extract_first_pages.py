import os
import PyPDF2

# Récupère le chemin du dossier où se trouve le script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Dossier où chercher les PDF
pdf_dir = base_dir
# Dossier de sortie
out_dir = os.path.join(base_dir, "out")

# Crée le dossier "out" s'il n'existe pas
os.makedirs(out_dir, exist_ok=True)

# Liste tous les fichiers PDF dans le répertoire courant
pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("Aucun fichier PDF trouvé dans le répertoire :", pdf_dir)
else:
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        output_path = os.path.join(out_dir, pdf_file)

        try:
            # Ouvre le fichier PDF en lecture binaire
            with open(pdf_path, "rb") as infile:
                reader = PyPDF2.PdfReader(infile)
                
                if len(reader.pages) == 0:
                    print(f"[⚠️] {pdf_file} est vide, ignoré.")
                    continue

                # Récupère la première page
                first_page = reader.pages[0]

                # Crée un nouveau writer pour le PDF de sortie
                writer = PyPDF2.PdfWriter()
                writer.add_page(first_page)

                # Écrit le fichier dans le dossier "out"
                with open(output_path, "wb") as outfile:
                    writer.write(outfile)

                print(f"[✅] Première page extraite : {output_path}")

        except Exception as e:
            print(f"[❌] Erreur avec {pdf_file} : {e}")

print("\nExtraction terminée ! Les fichiers sont dans :", out_dir)
