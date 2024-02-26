# Importing the relevant python libraries for our analysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset
nobel = pd.read_csv(r"Impact of Gender and Geography on Nobel Awards\complete.csv")
nobel.head()

#adding and age colunm
nobel['age'] = (pd.to_datetime(nobel['awardYear'], errors="coerce").dt.year -
                pd.to_datetime(nobel['birth_date'], errors="coerce", format="%Y-%m-%d").dt.year)


#age distribution of the Nobel leareutes
nobel_age=nobel.sort_values(by="age")
sns.histplot(nobel, x="age",kde=True).set_title("Age distribution of Winners")
#plt.show()
sns.lineplot(nobel,y="age",x="awardYear",errorbar=None).set_title("Age of Winners Over the years")
#plt.show()


#grouping the data by sex
gender=nobel.gender.value_counts().reset_index()
sns.set(style="darkgrid")
# Create the plot with different colors for males and females
sns.displot(data=nobel, x="gender", hue="gender", palette="Set2")
#plt.show()
counts = nobel['gender'].value_counts()
# Define your labels and colors
labels = counts.index
colors = sns.color_palette('pastel')[0:len(counts)]
# Create the pie chart
plt.pie(counts, labels=labels, colors=colors, autopct='%.0f%%')
#plt.show()

#distribution of winners based on country of origin
country_counts = nobel['birth_country'].value_counts().reset_index().head(20)

# Rename the columns for easier understanding
country_counts.columns = ['Country', 'Count']
print(country_counts.head(20))

# Create a horizontal bar plot
ax = sns.barplot(x='Count', y='Country', hue='Count', data=country_counts, palette="Set2", legend=False)
ax.set_ylim(bottom=0, top=country_counts['Count'].max() + 1)
ax.set_ylabel('Top 20 countries')

# Display the plot
#plt.show()

#checking for african countries
african_countries = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
    "Congo (Brazzaville)", "Congo (Kinshasa)", "Djibouti", "Egypt",
    "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia",
    "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho",
    "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania",
    "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", 
    "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone",
    "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo",
    "Tunisia", "Uganda", "Zambia", "Zimbabwe"
]

nobel_africa= nobel[nobel["birth_country"].isin(african_countries )]
africa_counts = nobel_africa['birth_country'].value_counts().reset_index()
# Rename the columns for easier understanding
africa_counts.columns = ['Country', 'Count']
print(africa_counts)
# Create a horizontal bar plot
ax=sns.barplot(x='Count', y='Country', data=africa_counts,palette="Set2")
ax.set_ylabel('African Countries')

# Display the plot
plt.show()





