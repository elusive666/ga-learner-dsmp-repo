# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=',', skip_header=1)
print(data)
print(type(data))
print(data.size)
print(np.shape(data))
print(np.ndim(data))
print(data.dtype)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.asarray(new_record)#new_record.astype('float64')
census = np.concatenate((data, new_record))
print(census)
#Code starts here



# --------------
#Code starts here
age = census[:, 0]
print(age)
max_age = max(age)
print(max_age)
min_age = min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race = census[:, 2]
#print(race)
#print(race.dtype)
#race_0 = race[census[:, 2] == 0]
#race_1 = race[census[:, 2] == 1]
#race_2 = race[census[:, 2] == 2]
#race_3 = race[census[:, 2] == 3]
#race_4 = race[census[:, 2] == 4]
#print(race_4)
#len_0 = race_0.size
#len_1 = race_1.size
#len_2 = race_2.size
#len_3 = race_3.size
#len_4 = race_4.size
#lstTemp = [len_0, len_1, len_2, len_3, len_4]
#print(lstTemp)
#minT = min(lstTemp)
#print(minT)
#minority_race = lstTemp.index(minT)
#print(minority_race)

#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here


# --------------
#Code starts here
senior_citizens = np.array(census[census[:, 0] > 60]).astype('int64')
#print(senior_citizens)
working_hours_sum = np.sum(senior_citizens[:, 6])
#print(working_hours_sum)
#print(senior_citizens.size)
#print(senior_citizens.shape)
#print(np.ndim(senior_citizens))
#tempArr = senior_citizens[:, 6]
#senior_citizens_len = len(tempArr)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1] > 10].astype('int64')
low = census[census[:,1] <= 10].astype('int64')
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high, avg_pay_low)


