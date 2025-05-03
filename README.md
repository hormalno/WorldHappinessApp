# World Happiness App

A simple Python app that loads and cleans the data from the csv and shows information with simple filtering and exploration

## 🌦 Features

- Visualize happiness scores across countries, regions, and time
- Select a year (if using multi-year data)
- Filter by region or country
- View happiness rankings
- Display top N happiest countries
- Display bottom N countries
- Plot correlations between score components and happiness score
- Bonus:
[//]: # (Time trend visualizations &#40;if using multi-year&#41;)

[//]: # (Display &#40;your&#41; statistical insights &#40;e.g., "most influential factor"&#41;)

[//]: # (Add explanations or hover-tooltips for variables)

[//]: # (Change the default color scheme to something that you like.)

[//]: # (Do a multi-page app.)


## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/hormalno/WorldHappinessApp
cd WorldHappinessApp
cd src

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

## Usage
To run the app from the command line:
streamlit run main.py