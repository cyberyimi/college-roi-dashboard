# College ROI Dashboard

**Interactive dashboard analyzing the return on investment of different college majors**

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Dash](https://img.shields.io/badge/Dash-2.14-purple)
![Plotly](https://img.shields.io/badge/Plotly-5.18-green)

---

## 🎯 Project Overview

This interactive dashboard helps students make data-driven decisions about college majors by analyzing:
- **Historical tuition trends** (1985-2016)
- **Salary outcomes** for 763 different majors
- **Return on investment** calculations
- **Break-even analysis** comparing college graduates vs. high school graduates

Built with Python, Dash, and Plotly, featuring a neon magenta color scheme and fully interactive visualizations.

---

## 📊 Key Features

### 1. Tuition Trends Analysis
- Visualizes college cost increases over 30+ years
- Shows inflation-adjusted (constant dollar) trends
- Reveals the rising cost of higher education

### 2. Salary Comparison by Major
- Early career pay (0-5 years experience)
- Mid-career pay (10+ years experience)
- 763 different majors analyzed
- Categorized into 8 major fields

### 3. ROI Calculator
- Interactive major category selector
- Shows top 15 highest-paying majors per category
- Calculates average break-even time
- Compares college graduates vs. high school graduates

### 4. Best Value Analysis
- Identifies fastest break-even majors
- Color-coded visualization by ROI timeline
- Helps identify high-value educational investments

---

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **Dash** - Interactive web dashboard framework
- **Plotly** - Data visualization library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations

---

## 📁 Project Structure

```
college-roi-dashboard/
├── app.py                          # Main Dash application
├── prepare_data.py                 # Data cleaning and processing
├── data/
│   ├── historical_tuition.csv      # Tuition trends 1985-2016
│   ├── final-post-college-salaries.csv  # Salary data by major
│   ├── processed_salary_data.csv   # Cleaned salary data
│   └── processed_tuition_trend.csv # Cleaned tuition data
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/cyberyimi/college-roi-dashboard.git
cd college-roi-dashboard
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Prepare the data:**
```bash
python prepare_data.py
```

4. **Run the dashboard:**
```bash
python app.py
```

5. **Open your browser:**
Navigate to `http://localhost:8050` to view the dashboard

---

## 📈 Data Sources

### Tuition Data
- **Source:** TidyTuesday College Tuition Dataset
- **Coverage:** 1985-2016
- **Type:** Inflation-adjusted (constant dollars)
- **Scope:** Average 4-year institutions

### Salary Data
- **Source:** PayScale College Salary Report
- **Majors:** 763 different undergraduate majors
- **Metrics:** Early career pay, mid-career pay, job meaning percentage
- **Degree Type:** Bachelor's degrees

---

## 🧮 Methodology

### ROI Calculation

**Assumptions:**
- Total 4-year degree cost: $106,372 (2016 average annual tuition × 4)
- High school graduate baseline salary: $40,000/year
- Break-even formula: `Total Cost / (College Salary - HS Salary)`

**Categories:**
Majors are automatically categorized into 8 fields:
1. Engineering & Technology
2. Business & Economics
3. Sciences & Mathematics
4. Health & Medicine
5. Arts & Communications
6. Humanities & Social Sciences
7. Education
8. Other

---

## 📊 Key Findings

### Fastest Break-Even Majors:
1. **Electrical Engineering & Computer Science (EECS)** - 1.2 years
2. **Operations Research & Industrial Engineering** - 1.7 years
3. **Petroleum Engineering** - 1.8 years

### Average Break-Even by Category:
- **Engineering & Technology:** 3 years
- **Business & Economics:** 5 years
- **Sciences & Mathematics:** 6 years
- **Education:** 12 years *(still valuable for job meaning!)*

### Tuition Growth:
- **1985:** $12,274/year
- **2016:** $26,593/year
- **Increase:** 117% over 31 years

---

## 🎨 Design Features

- **Neon Magenta Color Scheme** (#ff00ff) - Project 2 signature color
- **Dark Mode Interface** - Easy on the eyes
- **Responsive Layout** - Works on desktop and mobile
- **Interactive Charts** - Hover for details, click to filter
- **Category Selector** - Explore different major fields

---

## 🔮 Future Enhancements

Potential additions to the dashboard:
- [ ] Add regional salary variations
- [ ] Include student loan debt scenarios
- [ ] Show employment rates by major
- [ ] Add "total lifetime earnings" calculator
- [ ] Incorporate cost of living adjustments
- [ ] Compare public vs. private schools

---

## ⚠️ Limitations

**Data Considerations:**
- Tuition data ends in 2016 (costs have likely increased)
- Salary data represents national averages (regional variation exists)
- ROI calculations use simplified assumptions
- Does not account for scholarships/financial aid
- High school graduate baseline may vary by region

**Use this tool as a starting point for research, not as financial advice.**

---

## 👤 Author

**Monse Rojo**
- Portfolio: [monserojo.com](https://monserojo.com)
- GitHub: [@cyberyimi](https://github.com/cyberyimi)
- LinkedIn: [Monse Rojo](https://www.linkedin.com/in/monse-rojo-6b70b3397/)

---

## 📝 License

This project is open source and available for educational purposes.

---

## 🙏 Acknowledgments

- Data from TidyTuesday and PayScale
- Built with Dash and Plotly
- Inspired by the need for data-driven college decisions

---

**Built with ❤️ and data by Monse Rojo**
