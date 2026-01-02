# College ROI Dashboard

**Is your degree worth it? Find out which majors pay off fastest.**

---

## What This Does

This dashboard answers one simple question: How long until your college degree pays for itself?

I analyzed 763 different college majors to show you:
- Which majors lead to the highest salaries
- How long it takes to break even on your tuition
- How college costs have increased since 1985
- The best value majors for your money

---

## Key Findings

**Fastest payback:**
- Computer Science & Engineering: 1.2 years to break even
- Engineering majors: 3 years average
- Education majors: 12 years (but people love their jobs!)

**Cost reality:**
- 1985: $12,274/year
- 2016: $26,593/year
- 117% increase

**Top earners:**
- Engineering grads start at $78K average
- Business grads start at $64K average
- The top 20 highest-ROI majors are almost all STEM

---

## How to Run It

Install dependencies:
```bash
pip install -r requirements.txt
```

Prep the data:
```bash
python prepare_data.py
```

Launch dashboard:
```bash
python app.py
```

Then open http://localhost:8050 in your browser.

---

## What's Inside

- `app.py` - The interactive dashboard
- `prepare_data.py` - Cleans the data and calculates ROI
- `data/` - Tuition costs (1985-2016) and salary info for 763 majors
- `index.html` - Static version you can view without running Python

---

## The Math

How I calculate "break even":
- Average college grad pays: $106,372 (4 years of tuition)
- High school grads earn: ~$40,000/year
- Break even = Total cost / (Your salary - $40K)

Example:
- Computer Science grad earns $93K
- Difference: $93K - $40K = $53K/year
- Break even: $106K / $53K = 2 years

---

## Data Sources

- Tuition: College Scorecard (1985-2016)
- Salaries: PayScale College Salary Report
- 763 majors analyzed across 8 categories

---

## Built With

- Python - Data analysis
- Dash - Interactive web app
- Plotly - Charts and graphs
- Pandas - Data manipulation

---

## Limitations

Heads up:
- Uses 2016 tuition (it's higher now)
- National averages (your area might be different)
- Doesn't include scholarships or financial aid
- Assumes you graduate in 4 years

This is a starting point for research, not financial advice.

---

## Author

Monse Rojo
- Portfolio: monserojo.com
- GitHub: @cyberyimi
- LinkedIn: linkedin.com/in/monse-rojo-6b70b3397/

---

Built with data and Python.
