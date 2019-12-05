# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-', 'Agender', inplace=True)
gender_count = data.Gender.value_counts()
# bar chart
gender_count.plot(kind = 'bar')
# label the axes
plt.xlabel("Sex")
plt.ylabel("No. of Super Heroes")
# Rotate X-axes labels
plt.xticks(rotation=45)
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data.Alignment.value_counts()
alignment.plot.pie()
plt.title('Alignment Distribution')
plt.legend()
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.cov()
sc_covariance = sc_covariance.iloc[0,1]
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print("sc_pearson: ",sc_pearson)
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov()
ic_covariance = ic_covariance.iloc[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print("ic_pearson: ",ic_pearson)


# --------------
#Code starts here
total_high = data.Total.quantile(0.99)
super_best = data[data.Total > total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3, ncols=1, figsize=(20,10))
ax_1.boxplot(x=data.Intelligence)
ax_1.set_title('Intelligence')
ax_2.boxplot(x=data.Speed)
ax_2.set_title('Speed')
ax_3.boxplot(x=data.Power)
ax_3.set_title('Power')
plt.show()


