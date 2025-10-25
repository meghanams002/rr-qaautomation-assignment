# rr-qaautomation-assignment

## 📖 Overview
Automated UI and API test suite for the TMDB Discover demo site.

## 🧱 Tech Stack
- **Python 3.10+**
- **Selenium 4**
- **Pytest + pytest-html**
- **Requests**
- **webdriver-manager**

## Create virtual environment
python -m venv venv
source venv/bin/activate  # on mac/linux
venv\Scripts\activate     # on windows

## ⚙️ Setup

```bash
git clone https://github.com/meghanams002/rr-qaautomation-assignment.git
cd rr-qaautomation-assignment
pip install -r requirements.txt

# Run tests
pytest --html=reports/report.html --self-contained-html -v

