# DevSearch 🔍

DevSearch est un moteur de recherche bilingue (anglais et français) construit avec Flask, Tailwind CSS, et intégré avec l'API Google Custom Search. L'interface utilisateur est conçue pour ressembler au style de Chrome.

## Fonctionnalités ✨
- Recherche alimentée par l'API Google Custom Search 🔎
- Support bilingue (anglais et français) 🌐
- Interface réactive et moderne avec Tailwind CSS 🎨
- Facile à installer et à utiliser 🚀

## Installation 🛠️

1. Clonez le dépôt

```bash
git clone <repository-url>
cd DevSearch
```

2. Créez et activez un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installez les dépendances

```bash
pip install -r requirements.txt
```

4. Configurez les variables d'environnement pour l'API Google

```bash
export GOOGLE_API_KEY=your_google_api_key
export GOOGLE_CX=your_google_custom_search_cx
```

5. Lancez l'application

```bash
python app.py
```

6. Ouvrez votre navigateur à l'adresse `http://127.0.0.1:5000` 🌍

## Packaging 📦

Vous pouvez installer DevSearch en tant que package :

```bash
pip install .
```

Puis lancez :

```bash
devsearch
```

## Licence 📄

Licence MIT