import pandas as pd 
import matplotlib.pyplot as plt
#Load weather data
weather_data = pd.read_csv('weather2019.csv')
#print(weather_data.describe())

# ~ SUBMISSION FOR LAB 1 - ASHRAF ALI - 19315281
# ~ UNCOMMENT THE CODE UNDER EACH QUESTION TO TRY IT OUT

#Q1 ~ What was the minimum temperature on 21-Aug-19 (to 1 decimal place)?
#print(weather_data.loc[weather_data['date'] == '21-Aug-19'])

#Q2 ~ Find the mean maximum daily temperature (round your answer to 2 decimal places).
#print(weather_data['maxtemp'].mean())

#Q3 ~ What was the highest maximum daily temperature (round your answer to 1 decimal places)?
#print(weather_data['maxtemp'].max())

#Q4 ~ Find the median of the daily rainfall (round your answer to 1 decimal places).
#print(weather_data['rain'].median())

#Q5 ~ Find the standard deviation of the hours of sun per day (round your answer to 2 decimal places).
#print(weather_data['sun'].std())

#Q6 ~ On what date was the lowest daily windspeed recorded (state your answer in day-month-year format, e.g. 21-Apr-97)?
#print(weather_data.loc[weather_data['wind'] == weather_data['wind'].min(), 'date'])

#Q7 ~ Create a scatter plot of the maximum daily temperature against the daily rainfall. Which of the following best describes the plot?
#plt.figure()
#plt.scatter(weather_data['maxtemp'],weather_data['rain'])
#plt.xlabel('Maximum Daily Temperature')
#plt.ylabel('Daily Rain Fall')
#plt.show()

#Q8 & Q9 ~ Create a histogram for the daily rainfall measurement. Which of the following best describes the plot?
#plt.figure()
#plt.hist(weather_data['rain'], bins = 10, color='k')
#plt.xlabel('Daily Rainfall')
#plt.show()

#Q10 ~ The command below will create a histogram with 9 equally spaced bins.
#plt.figure()
#plt.hist(weather_data.sun,bins=[0,2,4,6,8,10,12,14,16])
#plt.xlabel('Daily Sun Level')
#plt.show()