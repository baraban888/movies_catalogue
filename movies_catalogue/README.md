# 🎬 Katalog filmów

Aplikacja stworzona w ramach kursu **Kodilla Bootcamp – Python Developer**, służąca do przeglądania filmów i seriali z bazy **The Movie Database (TMDb)**.  
Umożliwia wyszukiwanie, wyświetlanie szczegółów filmów, przeglądanie aktualnie emitowanych seriali oraz dodawanie pozycji do listy ulubionych.

---

## 🚀 Funkcjonalności

✅ Wyszukiwanie filmów po tytule  
✅ Przeglądanie list: „Popularne”, „Top Rated”, „Upcoming”, „Now Playing”  
✅ Sekcja **„TV Today”** – seriale emitowane dzisiaj  
✅ Możliwość dodania filmu do **ulubionych (⭐ Favorites)**  
✅ Responsywny interfejs oparty o **Bootstrap 5**  
✅ Integracja z API **TheMovieDB**  

---

## 🛠️ Technologie

- **Python 3.12**  
- **Flask**  
- **HTML + Jinja2**  
- **Bootstrap 5**  
- **TMDb API**  
- **dotenv**  

---

## ⚙️ Konfiguracja lokalna

1. Sklonuj repozytorium:
git clone https://github.com/baraban888/movies_catalogue.git

Wejdź do katalogu projektu:
cd movies_catalogue

Utwórz i aktywuj środowisko wirtualne:
python -m venv venv
source venv/Scripts/activate   # Windows

Zainstaluj wymagane biblioteki:
pip install -r requirements.txt

Utwórz plik .env i wklej swoje klucze API:
TMDB_API_TOKEN=your_api_token
TMDB_API_KEY=your_api_key

Uruchom aplikację:
python main.py

Otwórz w przeglądarce:
http://127.0.0.1:5000

📸 Zrzuty ekranu
Strona główna

Ulubione filmy

TV Today

👨‍💻 Autor
Projekt opracowany przez Dmytro Bahatiuk (Alex) w ramach kursu Kodilla.
📧 Email: 1975bahat@gmail.com
🌍 GitHub: baraban888

