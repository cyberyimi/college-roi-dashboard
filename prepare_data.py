"""
College ROI Dashboard - Data Preparation
Cleans and prepares data for the interactive dashboard
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("COLLEGE ROI DASHBOARD - DATA PREPARATION")
print("=" * 70)

# ============================================================================
# 1. LOAD SALARY DATA BY MAJOR
# ============================================================================
print("\n📊 Loading salary data by major...")
salary_df = pd.read_csv('data/final-post-college-salaries.csv')

# Clean salary columns (remove $ and , then convert to numeric)
salary_df['Early Career Pay'] = salary_df['Early Career Pay'].str.replace('$', '').str.replace(',', '').replace('-', np.nan).astype(float)
salary_df['Mid-Career Pay'] = salary_df['Mid-Career Pay'].str.replace('$', '').str.replace(',', '').replace('-', np.nan).astype(float)
salary_df['% High Meaning'] = salary_df['% High Meaning'].str.replace('%', '').replace('-', np.nan).astype(float)

# Drop rows with missing salary data
salary_df = salary_df.dropna(subset=['Early Career Pay', 'Mid-Career Pay'])

# Rename columns for easier use
salary_df.columns = ['rank', 'major', 'degree_type', 'early_career_pay', 'mid_career_pay', 'high_meaning_pct']

print(f"✅ Loaded {len(salary_df)} majors")
print(f"   Salary range: ${salary_df['early_career_pay'].min():,.0f} - ${salary_df['early_career_pay'].max():,.0f}")

# ============================================================================
# 2. LOAD HISTORICAL TUITION DATA
# ============================================================================
print("\n📊 Loading historical tuition data...")
tuition_hist = pd.read_csv('data/historical_tuition.csv')

# Filter for "All Constant" (inflation-adjusted) dollars for 4-year schools
tuition_trend = tuition_hist[
    (tuition_hist['tuition_type'] == '4 Year Constant') & 
    (tuition_hist['type'] == 'All Institutions')
].copy()

# Extract year from "1985-86" format
tuition_trend['year_numeric'] = tuition_trend['year'].str[:4].astype(int)

print(f"✅ Loaded tuition data from {tuition_trend['year_numeric'].min()} to {tuition_trend['year_numeric'].max()}")
print(f"   Tuition in 1985: ${tuition_trend[tuition_trend['year_numeric']==1985]['tuition_cost'].values[0]:,.0f}")
print(f"   Tuition in 2016: ${tuition_trend[tuition_trend['year_numeric']==2016]['tuition_cost'].values[0]:,.0f}")

# ============================================================================
# 3. CALCULATE AVERAGE TUITION FOR ROI CALCULATIONS
# ============================================================================
# Use most recent year's average tuition as baseline
latest_year = tuition_trend['year_numeric'].max()
avg_annual_tuition = tuition_trend[tuition_trend['year_numeric'] == latest_year]['tuition_cost'].values[0]
total_4year_cost = avg_annual_tuition * 4

print(f"\n💰 Using average 4-year degree cost: ${total_4year_cost:,.0f}")
print(f"   (Based on {latest_year} average annual tuition of ${avg_annual_tuition:,.0f})")

# ============================================================================
# 4. CALCULATE ROI METRICS
# ============================================================================
print("\n📈 Calculating ROI metrics...")

# Add total cost and ROI calculations to salary data
salary_df['total_tuition_cost'] = total_4year_cost

# Calculate years to break even
# Assumptions: 
# - Comparing college grad vs high school grad
# - Median high school grad salary: ~$40,000/year
# - Years to break even = Total Cost / (College Salary - HS Salary)
hs_grad_salary = 40000

salary_df['salary_advantage'] = salary_df['early_career_pay'] - hs_grad_salary
salary_df['years_to_break_even'] = np.where(
    salary_df['salary_advantage'] > 0,
    salary_df['total_tuition_cost'] / salary_df['salary_advantage'],
    999  # If salary is less than HS grad, mark as not breaking even
)

# Calculate lifetime earnings advantage (assuming 40 year career)
salary_df['lifetime_advantage'] = (
    (salary_df['early_career_pay'] * 10) +  # First 10 years at early career pay
    (salary_df['mid_career_pay'] * 30)      # Next 30 years at mid career pay
) - (hs_grad_salary * 40) - total_4year_cost

print("✅ ROI metrics calculated")

# ============================================================================
# 5. CATEGORIZE MAJORS
# ============================================================================
print("\n🏷️  Categorizing majors...")

def categorize_major(major):
    """Categorize majors into broad fields"""
    major_lower = major.lower()
    
    if any(word in major_lower for word in ['engineering', 'computer', 'information technology', 'software']):
        return 'Engineering & Technology'
    elif any(word in major_lower for word in ['business', 'economics', 'finance', 'accounting', 'management', 'marketing']):
        return 'Business & Economics'
    elif any(word in major_lower for word in ['biology', 'chemistry', 'physics', 'science', 'mathematics', 'statistics']):
        return 'Sciences & Mathematics'
    elif any(word in major_lower for word in ['nursing', 'health', 'medicine', 'pharmacy', 'therapy']):
        return 'Health & Medicine'
    elif any(word in major_lower for word in ['education', 'teaching']):
        return 'Education'
    elif any(word in major_lower for word in ['art', 'design', 'music', 'film', 'media', 'communication']):
        return 'Arts & Communications'
    elif any(word in major_lower for word in ['history', 'english', 'literature', 'language', 'philosophy', 'social']):
        return 'Humanities & Social Sciences'
    else:
        return 'Other'

salary_df['category'] = salary_df['major'].apply(categorize_major)

print(f"✅ Categorized into {salary_df['category'].nunique()} major categories:")
for cat in salary_df['category'].value_counts().index[:10]:
    count = len(salary_df[salary_df['category'] == cat])
    print(f"   {cat}: {count} majors")

# ============================================================================
# 6. SAVE PROCESSED DATA
# ============================================================================
print("\n💾 Saving processed data...")

salary_df.to_csv('data/processed_salary_data.csv', index=False)
tuition_trend.to_csv('data/processed_tuition_trend.csv', index=False)

print("✅ Saved processed_salary_data.csv")
print("✅ Saved processed_tuition_trend.csv")

# ============================================================================
# 7. SUMMARY STATISTICS
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY STATISTICS")
print("=" * 70)

print(f"\n📊 Top 10 Highest Paying Majors:")
print(salary_df.nlargest(10, 'early_career_pay')[['major', 'early_career_pay', 'mid_career_pay']].to_string(index=False))

print(f"\n📊 Best ROI Majors (Fastest Break Even):")
best_roi = salary_df[salary_df['years_to_break_even'] < 999].nsmallest(10, 'years_to_break_even')
print(best_roi[['major', 'early_career_pay', 'years_to_break_even']].to_string(index=False))

print(f"\n📊 Average Stats by Category:")
category_stats = salary_df.groupby('category').agg({
    'early_career_pay': 'mean',
    'mid_career_pay': 'mean',
    'years_to_break_even': lambda x: x[x < 999].mean() if len(x[x < 999]) > 0 else 0
}).round(0)
print(category_stats.to_string())

print("\n" + "=" * 70)
print("DATA PREPARATION COMPLETE!")
print("=" * 70)
print("\nReady to build the dashboard! 🚀")
