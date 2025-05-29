# 📰📈 NewsSentimentPricePredictor

**NewsSentimentPricePredictor** is a data-driven project that analyzes financial news sentiment and correlates it with stock market movements to uncover actionable investment strategies. This project is developed as part of a challenge at **Nova Financial Insights**, focusing on the intersection of Data Engineering, Financial Analytics, and Machine Learning Engineering.

---

## 📌 Business Objective

To enhance the predictive analytics capabilities at Nova Financial Insights by:

- Performing **sentiment analysis** on financial news headlines.
- Discovering **correlations** between sentiment scores and corresponding **stock price movements**.
- Designing **data-backed investment strategies** using insights from news sentiment.

---

## 🧠 Project Scope

This project is divided into three main phases:

### Task 1: Git, GitHub, and Exploratory Data Analysis (EDA)
- Set up Python virtual environment and GitHub repository.
- Analyze news headline statistics (length, frequency, source).
- Perform text analytics and topic modeling.
- Conduct temporal trends and publisher analysis.

### Task 2: Quantitative Analysis using TA-Lib and PyNance
- Load and prepare financial time-series data.
- Calculate key technical indicators (e.g., RSI, MACD).
- Visualize stock trends and volume.
- Compare indicators with market movements.

### Task 3: Correlation between News Sentiment and Stock Movements
- Apply sentiment analysis to headlines.
- Align news and stock prices by date.
- Calculate daily returns and correlate with average sentiment scores.
- Recommend actionable investment signals.

---

## 🗂️ Folder Structure
```
NewsSentimentPricePredictor/
├── .vscode/ # VS Code settings
├── .github/workflows/ # CI/CD with GitHub Actions
│ └── unittests.yml # Unit testing workflow
├── notebooks/ # Jupyter notebooks and exploratory work
│ ├── init.py
│ └── README.md
├── scripts/ # Utility scripts (data loading, cleaning, etc.)
│ ├── init.py
│ └── README.md
├── src/ # Source code for sentiment and correlation modules
│ ├── init.py
├── tests/ # Unit and integration tests
│ ├── init.py
├── .gitignore
├── requirements.txt
├── README.md
```

---

## 🛠️ Tech Stack

| Component      | Technology                      |
|----------------|----------------------------------|
| Language       | Python 3.11                      |
| Environment    | `venv` virtual environment       |
| IDE            | Visual Studio Code + PowerShell  |
| Libraries      | `pandas`, `nltk`, `TextBlob`, `matplotlib`, `TA-Lib`, `PyNance` |
| Version Control| Git + GitHub                     |
| CI/CD          | GitHub Actions                   |
| Notebooks      | Jupyter via VS Code Extension    |

---

## 📊 Key Features

- 📚 **NLP & Sentiment Scoring:** Quantify tone of financial headlines.
- 📈 **Stock Analysis:** Calculate and visualize technical indicators.
- 🔗 **Correlation Modeling:** Discover links between news tone and price changes.
- 🤖 **Automation Ready:** Designed with modularity for CI/CD integration.
- 🧪 **Testable & Scalable:** Unit tests and modular folder structure ready for production.

---

## 🚀 Getting Started

### 1. Clone the Repo

```
git clone https://github.com/Shegaw-21hub/NewsSentimentPricePredictor.git
cd NewsSentimentPricePredictor
```

### 2. Set Up the Environment
```
python -m venv venv
.\venv\Scripts\Activate  # Windows
pip install -r requirements.txt
```
### 3. Run Notebooks or Scripts
Launch Jupyter in VS Code and start with the notebooks in /notebooks.
## 🧪 Testing
Unit tests are located in the /tests folder. Run them using:
pytest tests/
### 📈 CI/CD
This project uses GitHub Actions for:

Automatic testing on push/pull request

Linting and formatting (optional)

Deployment steps (future scope)

Workflow defined in .github/workflows/unittests.yml

### 📅 Milestones & Deliverables

| Date          | Deliverable                                 |
| ------------- | ------------------------------------------- |
| 30 May, 2025  | GitHub repo link + Interim report (3 pages) |
| 03 June, 2025 | GitHub repo link + Final report (10 pages)  |

### 📚 References
NLTK Documentation

TA-Lib Python Wrapper

PyNance

TextBlob

Yahoo Finance API (yfinance)

### 🧠 Author 
Nova Financial Insights - Challenge Submission

Maintained by: Shegaw Adugna Melaku
GitHub: https://github.com/Shegaw-21hub/NewsSentimentPricePredictor

### 📌 License
This project is open for review and educational purposes as part of a professional analytics challenge. Not intended for commercial use.

---

Let me know if you'd like me to generate:

- `.vscode/settings.json` (for Python linting/formatting),
- a `requirements.txt` with common libraries preloaded,
- or the GitHub Actions `.yml` file.


