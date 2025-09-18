# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from io import StringIO

# --- Data Loading and Preparation ---
data = """
Region,Date,Frequency,Estimated Unemployment Rate,Estimated Employed,Estimated Labour Participation Rate,Region.1
Andhra Pradesh,31-01-2020,M,5.48,16635535,41.02,South
Andhra Pradesh,29-02-2020,M,5.83,16545652,40.90,South
Andhra Pradesh,31-03-2020,M,5.79,15881197,39.18,South
Andhra Pradesh,30-04-2020,M,20.51,11336911,33.10,South
Andhra Pradesh,31-05-2020,M,17.43,12988845,36.46,South
Andhra Pradesh,30-06-2020,M,3.31,19805400,47.41,South
Andhra Pradesh,31-07-2020,M,8.34,15431615,38.91,South
Andhra Pradesh,31-08-2020,M,6.96,15251772,37.83,South
Andhra Pradesh,30-09-2020,M,6.40,15220312,37.47,South
Andhra Pradesh,31-10-2020,M,6.59,15157557,37.34,South
Assam,31-01-2020,M,4.66,10271088,43.33,Northeast
Assam,29-02-2020,M,4.41,10338933,43.27,Northeast
Assam,31-03-2020,M,4.74,10113833,42.27,Northeast
Assam,30-04-2020,M,11.06,7899827,34.85,Northeast
Assam,31-05-2020,M,9.55,9034948,39.22,Northeast
Assam,30-06-2020,M,0.59,11559424,46.19,Northeast
Assam,31-07-2020,M,4.22,9933544,41.20,Northeast
Assam,31-08-2020,M,5.78,9858716,40.71,Northeast
Assam,30-09-2020,M,2.37,10511639,42.84,Northeast
Assam,31-10-2020,M,3.22,10373853,42.50,Northeast
Bihar,31-01-2020,M,11.11,23793393,36.52,East
Bihar,29-02-2020,M,12.36,23362378,36.10,East
Bihar,31-03-2020,M,15.43,21448373,33.24,East
Bihar,30-04-2020,M,46.64,13730799,30.36,East
Bihar,31-05-2020,M,35.10,17299778,33.26,East
Bihar,30-06-2020,M,20.73,20972304,38.12,East
Bihar,31-07-2020,M,12.83,23485323,38.54,East
Bihar,31-08-2020,M,13.23,23214532,38.30,East
Bihar,30-09-2020,M,11.95,23671337,38.57,East
Bihar,31-10-2020,M,9.82,24841961,40.10,East
Chhattisgarh,31-01-2020,M,7.24,8446543,41.11,Central
Chhattisgarh,29-02-2020,M,7.54,8403222,41.05,Central
Chhattisgarh,31-03-2020,M,8.46,8258381,40.37,Central
Chhattisgarh,30-04-2020,M,9.26,7623636,37.33,Central
Chhattisgarh,31-05-2020,M,13.78,7407000,38.46,Central
Chhattisgarh,30-06-2020,M,8.60,8409386,41.27,Central
Chhattisgarh,31-07-2020,M,5.92,8643936,41.92,Central
Chhattisgarh,31-08-2020,M,9.03,8289432,40.95,Central
Chhattisgarh,30-09-2020,M,3.58,9133243,43.26,Central
Chhattisgarh,31-10-2020,M,5.43,8923152,42.85,Central
Delhi,31-01-2020,M,11.83,4301912,35.19,North
Delhi,29-02-2020,M,21.65,4143439,37.28,North
Delhi,31-03-2020,M,18.42,4213759,36.47,North
Delhi,30-04-2020,M,29.85,3489524,35.08,North
Delhi,31-05-2020,M,17.70,4199923,36.14,North
Delhi,30-06-2020,M,10.23,4916053,38.93,North
Delhi,31-07-2020,M,12.18,4603611,36.98,North
Delhi,31-08-2020,M,16.28,4545381,38.25,North
Delhi,30-09-2020,M,12.22,4883344,39.38,North
Delhi,31-10-2020,M,12.11,4892557,39.42,North
Goa,31-01-2020,M,4.24,424729,40.38,West
Goa,29-02-2020,M,3.29,431115,40.36,West
Goa,31-03-2020,M,5.43,411986,39.48,West
Goa,30-04-2020,M,12.26,357879,36.33,West
Goa,31-05-2020,M,15.38,369963,38.90,West
Goa,30-06-2020,M,5.77,433436,41.36,West
Goa,31-07-2020,M,14.65,373853,39.19,West
Goa,31-08-2020,M,9.25,404692,39.73,West
Goa,30-09-2020,M,11.37,392823,39.63,West
Goa,31-10-2020,M,11.00,396783,39.74,West
Gujarat,31-01-2020,M,5.49,21987083,45.21,West
Gujarat,29-02-2020,M,6.29,21685497,45.24,West
Gujarat,31-03-2020,M,5.63,21789643,44.75,West
Gujarat,30-04-2020,M,12.92,19483100,43.51,West
Gujarat,31-05-2020,M,9.24,20963339,44.91,West
Gujarat,30-06-2020,M,5.92,22306714,46.50,West
Gujarat,31-07-2020,M,2.39,23081126,46.47,West
Gujarat,31-08-2020,M,2.83,23062386,46.52,West
Gujarat,30-09-2020,M,1.71,23677939,47.16,West
Gujarat,31-10-2020,M,3.29,23157876,46.51,West
Haryana,31-01-2020,M,20.91,6916968,43.49,North
Haryana,29-02-2020,M,24.13,6709841,43.43,North
Haryana,31-03-2020,M,23.71,6739486,42.84,North
Haryana,30-04-2020,M,43.22,4976712,42.06,North
Haryana,31-05-2020,M,33.56,5987723,43.19,North
Haryana,30-06-2020,M,22.25,6998492,44.72,North
Haryana,31-07-2020,M,27.10,6541539,44.07,North
Haryana,31-08-2020,M,33.55,6035904,44.20,North
Haryana,30-09-2020,M,30.29,6318335,44.47,North
Haryana,31-10-2020,M,27.34,6682703,45.10,North
Himachal Pradesh,31-01-2020,M,13.82,2367812,45.92,North
Himachal Pradesh,29-02-2020,M,18.06,2258872,45.69,North
Himachal Pradesh,31-03-2020,M,16.48,2291587,45.15,North
Himachal Pradesh,30-04-2020,M,11.83,2385108,44.88,North
Himachal Pradesh,31-05-2020,M,23.47,2048039,44.37,North
Himachal Pradesh,30-06-2020,M,11.14,2499248,46.88,North
Himachal Pradesh,31-07-2020,M,11.75,2420953,45.75,North
Himachal Pradesh,31-08-2020,M,17.75,2240993,45.14,North
Himachal Pradesh,30-09-2020,M,14.65,2364720,45.94,North
Himachal Pradesh,31-10-2020,M,11.77,2435728,46.12,North
Jammu & Kashmir,31-01-2020,M,13.11,3352729,38.11,North
Jammu & Kashmir,29-02-2020,M,14.47,3260971,37.89,North
Jammu & Kashmir,31-03-2020,M,15.86,3160731,37.42,North
Jammu & Kashmir,30-04-2020,M,17.18,2997030,36.03,North
Jammu & Kashmir,31-05-2020,M,21.88,2841973,36.43,North
Jammu & Kashmir,30-06-2020,M,17.91,3044431,37.06,North
Jammu & Kashmir,31-07-2020,M,11.24,3424623,38.64,North
Jammu & Kashmir,31-08-2020,M,16.24,3194095,38.10,North
Jammu & Kashmir,30-09-2020,M,16.19,3206467,38.22,North
Jammu & Kashmir,31-10-2020,M,16.15,3212130,38.29,North
"""
# Use StringIO to read the string data into a pandas DataFrame
df = pd.read_csv(StringIO(data))
# --- Data Cleaning ---
# Clean column names for easier access
df.columns = ['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate',
              'Estimated Employed', 'Estimated Labour Participation Rate', 'Region_Area']

# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Set the date as the index
df.set_index('Date', inplace=True)

print("--- First 5 rows of the loaded dataset ---")
print(df.head())


# --- National Level Unemployment Analysis ---
# Plot the national average unemployment rate over time
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(14, 7))
national_avg_rate = df.groupby(['Date'])['Estimated Unemployment Rate'].mean()
plt.plot(national_avg_rate.index, national_avg_rate.values, label='National Avg. Unemployment Rate', color='purple')
plt.title('National Average Unemployment Rate in India Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Estimated Unemployment Rate (%)', fontsize=12)
plt.legend()
plt.show()

# --- Analyzing the Impact of Covid-19 Lockdown ---
# Use Plotly for an interactive plot to show the sudden spike
fig = px.line(national_avg_rate,
              x=national_avg_rate.index,
              y=national_avg_rate.values,
              title='Impact of COVID-19 Lockdown on Unemployment in India',
              labels={'y': 'Unemployment Rate (%)', 'x': 'Date'})

# Add a vertical line to mark the start of the lockdown
fig.add_vline(x=pd.to_datetime('2020-03-25'), line_width=2, line_dash="dash", line_color="red",
              annotation_text="Start of National Lockdown")
fig.show()

# --- State-wise Unemployment Analysis ---
# Calculate and plot the average unemployment rate for each state
plt.figure(figsize=(12, 10))
state_avg_unemployment = df.groupby('Region')['Estimated Unemployment Rate'].mean().sort_values(ascending=True)
sns.barplot(x=state_avg_unemployment.values, y=state_avg_unemployment.index, palette='plasma')
plt.title('Average Unemployment Rate by State/Region in India', fontsize=16)
plt.xlabel('Average Estimated Unemployment Rate (%)', fontsize=12)
plt.ylabel('State / Region', fontsize=12)
plt.show()