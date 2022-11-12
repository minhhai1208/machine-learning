import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.cluster import KMeans
import sklearn.cluster as cluster
import pickle
columns = [
       'Question 2: Sound (1-5)', 'Question 2.1: Music (1-5)',
       'Question 2.2 : Noise control (1-5)',
       'Question 2.3 : Speaking Style (1-5)', 'Question 3: Camera (1-5)',
       'Question 3.1: Stable (1-5)', 'Question 3.2: Angel diversity (0-1)',
       'Question 4: Images (1-5)', 'Question 4.1: Resolution (1-5)',
       'Question 4.2: Color (1-5)', 'Question 5: Content (1-5)',
       'Question 5.1: Introduction (0-1)',
       'Question 5.2: Food description (0-1)', 'Question 6: Reviewer (1-5)',
       'Question 6.1: Reviewer emotion is negative - neutral - positive (1-3)',
       'Question 6.2: Recommendation (0-1)',
       'Question 6.3: Clear information (0-1)']
core_columns = [
       'Question 2: Sound (1-5)','Question 3: Camera (1-5)',
       'Question 4: Images (1-5)', 'Question 5: Content (1-5)',
       'Question 6: Reviewer (1-5)',]
output_column = 'Attractive Level (1-5)'

data = pd.read_excel("C:\\Users\\user\\Downloads\\mean_data.xlsx")
df = pd.DataFrame(set(data['video id']), columns=['video id'])
for id in df['video id']:
    c = columns + [output_column]
    mean = data[data['video id'] == id][c]
    df.loc[df['video id'] == id, c] = np.array(mean)

print(df)

data = pd.read_excel("C:\\Users\\user\\Downloads\\mean_data.xlsx")
X_train, X_test, y_train, y_test = train_test_split(data[core_columns][:], data[output_column][:], test_size=0.2, shuffle=True)
K = range(2, 12)
wss = []

for k in K:
    kmeans = cluster.KMeans(n_clusters=k)
    kmeans = kmeans.fit(X_train)
    wss_iter = kmeans.inertia_
    wss.append(wss_iter)

plt.xlabel('K')
plt.ylabel('Within-Cluster-Sum of Squared Errors (WSS)')
plt.plot(K, wss)
plt.show()

kmeans=cluster.KMeans(n_clusters=3)
km=kmeans.fit(X_train)
print("Centers: ")
print(km.cluster_centers_)



