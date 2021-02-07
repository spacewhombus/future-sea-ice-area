# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:54:29 2021

@author: kelli
"""

#Sea Ice Pysics, Observations and Modeling I
#Prof. Dirk Notz
#WS2020/21
#Final Exam: Sea Ice Area Future Scenarios
#In this exercise, we’ll compare CMIP6 simulated sea-ice area for three different
#future scenarios, in 2050, 2075, and 2100, and determine when differences occur.


#import packages

from netCDF4 import Dataset, num2date
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import calendar as cal
import math


#define the month for which the data is being plotted/analyzed

Month = 9

#create pandas dataframe with all three scenarios together
#so it is easier to plot them all together and it is referenced
#by the time, so can see individual months easier

sia_ssp = pd.DataFrame(index = pd.date_range(start = '2015-01-01', end = '2100-12-31', freq = 'M'))

Model_filename3 = 'sia_nh_CMIP6/ssp126/sia_nh_MPI-ESM1-2-LR_r2i1p1f1_ssp126.nc'
sia_netcdf = Dataset(Model_filename3)
sia_values = sia_netcdf.variables['sia_nh'][:]
sia_ssp['SSP1-26'] = sia_values

Model_filename4 = 'sia_nh_CMIP6/ssp245/sia_nh_MPI-ESM1-2-LR_r2i1p1f1_ssp245.nc'
sia_netcdf = Dataset(Model_filename4)
sia_values = sia_netcdf.variables['sia_nh'][:]
sia_ssp['SSP2-45'] = sia_values

Model_filename5 = 'sia_nh_CMIP6/ssp585/sia_nh_MPI-ESM1-2-LR_r2i1p1f1_ssp585.nc'
sia_netcdf = Dataset(Model_filename5)
sia_values = sia_netcdf.variables['sia_nh'][:]
sia_ssp['SSP5-85'] = sia_values

#Test plot future evolution for all months
# sia_ssp.plot()

#Test plot for one specific month
# sia_ssp[sia_ssp.index.month==9].plot()

#count the number of years with September sea ice area less than 1 million km2
#by selecting elements less than 1 and counting them

num_years = sia_ssp[sia_ssp.index.month==9][sia_ssp < 1].count()
print( num_years)

#an alternative way by creating a new dataframe with T/F values
#and then summing those to add "1" for every T value

# num_years_df = (sia_ssp[sia_ssp.index.month==9] < 1).sum()
# print(num_years_df)


#Below is an alternative way to read in the data without using a pandas dataframe


#read sea ice area data for first scenario SSP1-2.6
#and here for selected model MPI-ESMI-2-LR

# Model_filename_1 = 'sia_nh_CMIP6/ssp126/sia_nh_MPI-ESM1-2-LR_r2i1p1f1_ssp126.nc'
# sia_netcdf_1 = Dataset(Model_filename_1)
# sia_values_1 = sia_netcdf_1.variables['sia_nh'][:]

# #this gives you data for a single month, by extracting every 12th value of the file
# #beginning from Month minus 1st value (since Python starts count at 0, September is # 8)

# sia_values_mon_1 = sia_values_1.data[Month-1::12]

# #creates empty panda Dataframe for the time period 2014-2100

# sia_cmip6_1 = pd.DataFrame(index=range(2014,2100))

# #copies values for the month into the dataframe

# sia_cmip6_1['MPI-ESMI_SSP126'] = sia_values_mon_1



#read sea ice area data for second scenario SSP2-4.5
#and here for selected model MPI-ESMI-2-LR

# Model_filename_2 = 'sia_nh_CMIP6/ssp245/sia_nh_MPI-ESM1-2-LR_r2i1p1f1_ssp245.nc'
# sia_netcdf_2 = Dataset(Model_filename_2)
# sia_values_2 = sia_netcdf_2.variables['sia_nh'][:]

# #this gives you data for a single month, by extracting every 12th value of the file
# #beginning from Month minus 1st value (since Python starts count at 0, September is # 8)

# sia_values_mon_2 = sia_values_2.data[Month-1::12]

# #creates empty panda Dataframe for the time period 2014-2100

# sia_cmip6_2 = pd.DataFrame(index=range(2014,2100))

# #copies values for the month into the dataframe

# sia_cmip6_2['MPI-ESMI_SSP245'] = sia_values_mon_2



#read sea ice area data for third scenario SSP5-8.5
#and here for selected model MPI-ESMI-2-LR

# Model_filename_3 = 'sia_nh_CMIP6/ssp585/sia_nh_MPI-ESM1-2-LR_r2i1p1f1_ssp585.nc'
# sia_netcdf_3 = Dataset(Model_filename_3)
# sia_values_3 = sia_netcdf_3.variables['sia_nh'][:]

# #this gives you data for a single month, by extracting every 12th value of the file
# #beginning from Month minus 1st value (since Python starts count at 0, September is # 8)

# sia_values_mon_3 = sia_values_3.data[Month-1::12]

# #creates empty panda Dataframe for the time period 2014-2100

# sia_cmip6_3 = pd.DataFrame(index=range(2014,2100))

# #copies values for the month into the dataframe

# sia_cmip6_3['MPI-ESMI_SSP585'] = sia_values_mon_3



#now time to plot all three scenarios together

plt.figure()

sia_ssp.plot() #plots all together from dataframe
# plt.plot(sia_cmip6_1.loc[2014:2100], label= 'MPI-ESMI_SSP126') # plotting year, sia_cmip6_1 separately 
# plt.plot(sia_cmip6_2.loc[2014:2100], label= 'MPI-ESMI_SSP245') # plotting year, sia_cmip6_2 separately 
# plt.plot(sia_cmip6_3.loc[2014:2100], label= 'MPI-ESMI_SSP585') # plotting year, sia_cmip6_3 separately
 
# style
plt.style.use('seaborn-darkgrid')

# Add titles
plt.title("Yearlong Sea Ice Area Projections in Three Future Emissions Scenarios\n (MPI-ESM1-2-LR)", loc='center', fontsize=12, fontweight=0, color='black')
plt.xlabel("Year")
plt.ylabel("Sea Ice Area [in million km^2]")

#add axis limit to ensure all on same scale as later graphs for easier comparison
plt.ylim([-1, 15])

# Add legend refinements
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))


#add reference lines for 2050, 2075, and 2100

plt.axvline(x = '2025-01-01', color = 'black', linestyle='--')
plt.annotate('2025', xy=('2050-01-01', 14), xytext=('2018-01-01', 14))

plt.axvline(x = '2050-01-01', color = 'black', linestyle='--')
plt.annotate('2050', xy=('2050-01-01', 14), xytext=('2043-01-01', 14))

plt.axvline(x = '2075-01-01', color = 'black', linestyle='--')
plt.annotate('2075', xy=('2075-01-01', 14), xytext=('2068-01-01', 14))

plt.axvline(x = '2100-01-01', color = 'black', linestyle='--')
plt.annotate('2100', xy=('2100-01-01', 14), xytext=('2093-01-01', 14))

# #add color ranges for years 2014-2050, 2050-2075, and 2075-2100
# plt.axvspan(2025, 2050, color=palette2(2), alpha=0.5)
# plt.axvspan(2050, 2075, color=palette2(6), alpha=0.5)
# plt.axvspan(2075, 2100, color=palette2(3), alpha=0.5)

plt.show() 

#now to look at the month of March (greatest sea ice extent)

plt.figure()

sia_ssp[sia_ssp.index.month==3].plot() #plots all together from dataframe
# plt.plot(sia_cmip6_1.loc[2014:2100], label= 'MPI-ESMI_SSP126') # plotting year, sia_cmip6_1 separately 
# plt.plot(sia_cmip6_2.loc[2014:2100], label= 'MPI-ESMI_SSP245') # plotting year, sia_cmip6_2 separately 
# plt.plot(sia_cmip6_3.loc[2014:2100], label= 'MPI-ESMI_SSP585') # plotting year, sia_cmip6_3 separately
 
# style
plt.style.use('seaborn-darkgrid')

# Add titles
plt.title("March Sea Ice Area Projections in Three Future Emissions Scenarios\n (MPI-ESM1-2-LR)", loc='center', fontsize=12, fontweight=0, color='black')
plt.xlabel("Year")
plt.ylabel("Sea Ice Area [in million km^2]")

#add scale to make the graphs more easily comparable
plt.ylim([-1,15])

# Add legend refinements
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

#add reference lines for 2050, 2075, and 2100

plt.axvline(x = '2025-01-01', color = 'black', linestyle='--')
plt.annotate('2025', xy=('2050-01-01', 14), xytext=('2018-01-01', 14))

plt.axvline(x = '2050-01-01', color = 'black', linestyle='--')
plt.annotate('2050', xy=('2050-01-01', 14), xytext=('2043-01-01', 14))

plt.axvline(x = '2075-01-01', color = 'black', linestyle='--')
plt.annotate('2075', xy=('2075-01-01', 14), xytext=('2068-01-01', 14))

plt.axvline(x = '2100-01-01', color = 'black', linestyle='--')
plt.annotate('2100', xy=('2100-01-01', 14), xytext=('2093-01-01', 14))

# #add color ranges for years 2014-2050, 2050-2075, and 2075-2100
# plt.axvspan(2025, 2050, color=palette2(2), alpha=0.5)
# plt.axvspan(2050, 2075, color=palette2(6), alpha=0.5)
# plt.axvspan(2075, 2100, color=palette2(3), alpha=0.5)

plt.show() 


#now to show just the month of September (lowest sea ice extent during the year)

plt.figure()

sia_ssp[sia_ssp.index.month==9].plot() #plots all together from dataframe
# plt.plot(sia_cmip6_1.loc[2014:2100], label= 'MPI-ESMI_SSP126') # plotting year, sia_cmip6_1 separately 
# plt.plot(sia_cmip6_2.loc[2014:2100], label= 'MPI-ESMI_SSP245') # plotting year, sia_cmip6_2 separately 
# plt.plot(sia_cmip6_3.loc[2014:2100], label= 'MPI-ESMI_SSP585') # plotting year, sia_cmip6_3 separately
 
# style
plt.style.use('seaborn-darkgrid')

# Add titles
plt.title("September Sea Ice Area Projections in Three Future Emissions Scenarios\n (MPI-ESM1-2-LR)", loc='center', fontsize=12, fontweight=0, color='black')
plt.xlabel("Year")
plt.ylabel("Sea Ice Area [in million km^2]")

# Add legend refinements
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

#add scale to all graphs so it is easier to compare
plt.ylim([-1,15])

#add reference lines for 2050, 2075, and 2100

plt.axvline(x = '2025-01-01', color = 'black', linestyle='--')
plt.annotate('2025', xy=('2050-01-01', 14), xytext=('2018-01-01', 14))

plt.axvline(x = '2050-01-01', color = 'black', linestyle='--')
plt.annotate('2050', xy=('2050-01-01', 14), xytext=('2043-01-01', 14))

plt.axvline(x = '2075-01-01', color = 'black', linestyle='--')
plt.annotate('2075', xy=('2075-01-01', 14), xytext=('2068-01-01', 14))

plt.axvline(x = '2100-01-01', color = 'black', linestyle='--')
plt.annotate('2100', xy=('2100-01-01', 14), xytext=('2093-01-01', 14))

# #add color ranges for years 2014-2050, 2050-2075, and 2075-2100
# plt.axvspan(2025, 2050, color=palette2(2), alpha=0.5)
# plt.axvspan(2050, 2075, color=palette2(6), alpha=0.5)
# plt.axvspan(2075, 2100, color=palette2(3), alpha=0.5)

plt.show()


#now to show just the month of September ZOOMED to show detail as to when 
#the ice falls below the 1 million km^2 threshold (lowest sea ice extent during the year)

plt.figure()

sia_ssp[sia_ssp.index.month==9].plot() #plots all together from dataframe
# plt.plot(sia_cmip6_1.loc[2014:2100], label= 'MPI-ESMI_SSP126') # plotting year, sia_cmip6_1 separately 
# plt.plot(sia_cmip6_2.loc[2014:2100], label= 'MPI-ESMI_SSP245') # plotting year, sia_cmip6_2 separately 
# plt.plot(sia_cmip6_3.loc[2014:2100], label= 'MPI-ESMI_SSP585') # plotting year, sia_cmip6_3 separately
 
# style
plt.style.use('seaborn-darkgrid')

# Add titles
plt.title("DETAIL: Critical Threshold for September Sea Ice Area Projections\n (MPI-ESM1-2-LR)", loc='center', fontsize=12, fontweight=0, color='black')
plt.xlabel("Year")
plt.ylabel("Sea Ice Area [in million km^2]")

# Add legend refinements
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

#add scale to all graphs so it is easier to compare
plt.ylim([-0.1,2])

#add reference lines for 2050, 2075, and 2100

plt.axvline(x = '2044-01-01', color = 'black', linestyle='--', ymin = -0.1, ymax= 1.0)
plt.annotate('2044', xy=('2044-01-01', 0), xytext=('2038-01-01', 0))

plt.axvline(x = '2052-01-01', color = 'black', linestyle='--')
plt.annotate('2052', xy=('2052-01-01', 0), xytext=('2046-01-01', 0))

#add color range for threshold level of 1 million km^2 of ice
plt.axhspan(-1, 1, color= 'pink', alpha=0.5)

plt.show()