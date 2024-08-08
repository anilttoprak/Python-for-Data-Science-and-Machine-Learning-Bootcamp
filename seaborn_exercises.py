# Seaborn Exercises

# Time to practice your new seaborn skills! Try to recreate the plots below (don't worry about color schemes, just the plot itself.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
# titanic = titanic.select_dtypes(include=[np.number])
a=titanic.head()

# <seaborn.axisgrid.JointGrid at 0x11d0389e8>

sns.jointplot(x='fare',y='age',data=titanic)
# or
t = sns.JointGrid(x="fare", y="age", data=titanic)
t = t.plot(sns.scatterplot, sns.histplot)

# <matplotlib.axes._subplots.AxesSubplot at 0x11fc5ca90>

sns.histplot(x='fare',data=titanic)
# or
sns.distplot(titanic['fare'],bins=30,kde=False,color='red')

# <matplotlib.axes._subplots.AxesSubplot at 0x11f23da90>

sns.boxplot(x="class", y="age", data=titanic,palette='rainbow')

# <matplotlib.axes._subplots.AxesSubplot at 0x11f215320>

sns.swarmplot(x="class", y="age", data=titanic,palette='rainbow')

# <matplotlib.axes._subplots.AxesSubplot at 0x11f207ef0>

sns.countplot(x="sex",data=titanic)

# <matplotlib.text.Text at 0x11d72da58>

sns.heatmap(titanic.corr())
plt.title('titanic.corr()')

# <seaborn.axisgrid.FacetGrid at 0x11d81c240>

t = sns.FacetGrid(titanic, col="sex")
t = t.map(plt.hist, "age")


