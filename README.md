# EPL Stats Web App

This web app displays English Premier League (EPL) statistics, including scores, teams, players, coaches, and standings. The data is obtained from the EPL API and stored in a MySQL database using SQLAlchemy ORM. The web app is built using Python Flask and utilizes jQuery and JavaScript for dynamic updates on the HTML pages.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- jQuery

### Installation

Clone the repository to your local machine
Install the required Python libraries using pip: pip install -r requirements.txt
Create a MySQL database and define the required tables. You can find the SQL script in the db folder.
Set the database URI in the config.py file.
Start the Flask application: flask run
Access the web app in your web browser at [*here*](http://localhost:5000/)

## Usage

The web app allows users to view EPL scores, standings, teams, players, coaches, and other soccer statistics. Users can browse the data on the HTML pages and dynamically update the content using the search and filter functions.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This project was created by [Dominic Sengo](https://github.com/Domengo). Special thanks to the EPL API for providing the data used in this web app.
