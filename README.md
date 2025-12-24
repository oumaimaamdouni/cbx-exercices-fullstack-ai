# Extracteur de CV Full Stack AI

Ce projet est un outil complet permettant l'extraction de données clés (Nom, Prénom, Email, Téléphone, Diplôme) à partir de CV au format PDF et DOCX. 

## 🛠️ Stack Technique
- **Backend** : FastAPI (Python)
- **Frontend** : Streamlit (UI interactive)
- **Extraction** : Algorithmes basés sur les Expressions Régulières (Regex)
- **Conteneurisation** : Docker & Docker Compose


## 📦 Installation

1. **Prérequis** : 
   - Python 3.12 (pour le lancement local)
   - Docker Desktop (pour le lancement conteneurisé)

2. **Extraction du projet** :
   Décompressez l'archive `cv-extractor.zip` dans votre répertoire de travail.


## 🚀 Lancement Docker

C'est la méthode la plus rapide pour tester l'application dans un environnement isolé.

1. Ouvrez un terminal à la racine du projet.
2. Exécutez la commande suivante :
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
3. Accédez à l'application : 
            http://localhost:8501


## Lancement Local (Sans Docker)
Si vous souhaitez lancer les services manuellement sur votre machine :
1. Lancer le Backend (FastAPI)

cd backend
pip install -r requirements.txt
python main.py

2. Lancer le Frontend (Streamlit)

cd frontend
pip install -r requirements.txt
streamlit run app.py

📝 Exemples d'API (Endpoints)
La documentation complète de l'API (Swagger) est disponible sur : http://localhost:8000/docs

1. Analyse de CV (POST)

Endpoint : /api/v1/upload-cv

Description : Analyse un fichier binaire (PDF ou DOCX) et retourne les données extraites au format JSON.

2. Vérification d'état (GET)

Endpoint : /

Description : Point de vérification (Healthcheck) pour confirmer que l'API est opérationnelle.

Structure du JSON extrait :
{
    "first_name": "Oumaima",
    "last_name": "Amdouni",
    "email": "oumaima.amdouni@esprit.tn",
    "phone": "27229906",
    "degree": "Ingénieur"
}