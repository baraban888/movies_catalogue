# 🎬 Movies Catalogue

A simple web application built with Flask and TMDb API which allows users to browse, search and view movie details. The project was created as part of the Kodilla Bootcamp. The application displays movie lists (Popular, Top Rated, Upcoming, Now Playing), allows searching by title, and shows detailed information for each film including poster or random backdrop, title, tagline, overview, budget, genres and cast list (if available). Missing data such as empty cast or undefined budget are handled gracefully. The interface is fully responsive and based on Bootstrap 5.

## Installation and Run
Clone the repository using `git clone https://github.com/yourusername/movies_catalogue.git` and open the folder `movies_catalogue`. Create and activate a virtual environment using `python -m venv venv` and then `venv\Scripts\activate` (on Windows) or `source venv/bin/activate` (on Linux/Mac). Install dependencies with `pip install -r requirements.txt`. Create a `.env` file in the project root and add your TMDb API key in the form `TMDB_API_TOKEN=your_api_token_here`. Run the application using `python main.py` and open `http://127.0.0.1:5000` in your browser.

## Technologies
Python 3.12, Flask, Jinja2 Templates, TMDb API, Bootstrap 5, HTML, CSS.

## Author
Created by **Dmytro Bahatiuk (Alex)** — Nowa Sól, Poland.  
📧 1975bahat@gmail.com

## License
This project was created for educational purposes as part of the Kodilla Bootcamp.
