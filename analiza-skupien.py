import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import calinski_harabasz_score, silhouette_score

data = pd.read_excel('Dane_Analiza_Skupien.xlsx')
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

features= data.columns.values.tolist()
del features[0]
X = data[features].copy()

# Wybór liczby klastrów metodą łokcia oraz sprawdzenie poprawności wyboru indeksami ocen : Calińskiego i Harabasza oraz Silhouette
results = []
wcss = []
for i in range(2, 8):
       kmeans = (KMeans(n_clusters=i, random_state=0, n_init=50))
       label = kmeans.fit_predict(X)
       wcss.append(kmeans.inertia_)
       ch = calinski_harabasz_score(X, label)
       ss = silhouette_score(X, label)
       results.append({
              'Liczba skupień': i,
              'Calinski Harabasz Score': round(ch, 4),
              'Silhouette Score': round(ss, 4)
       })

plt.plot(range(2, 8), wcss, color = 'darkblue')
plt.title('Metoda łokcia')
plt.xlabel("Liczba Klastrów")
plt.ylabel("Within-Cluster Sum of Squares")
plt.savefig('Kmeans_Elbow.png')
plt.show()

scores = pd.DataFrame(results)
scores.to_excel('KMEANS_Scores.xlsx')

kmeans = KMeans(n_clusters=3, random_state=0)

data['Klaster_Podziałowy'] = kmeans.fit_predict(X)

# Wykonanie grupowania hierarchicznego w tym narysowanie Dendogramu
lincage_data = linkage(X, method='ward', metric='euclidean')
dendrogram(lincage_data, labels=data.iloc[:,0].values, leaf_rotation=90)
plt.title('Dendrogram')
plt.tight_layout()
plt.savefig('Dendrogram.png')
plt.show()


# Analiza wykresu odległości wiązania względem etapów wiązania - wybór liczby grup
odleglosci = lincage_data[:, 2]
plt.figure(figsize=(8, 4))

plt.plot(range(1, len(odleglosci) + 1), odleglosci[::-1], marker='o', color='red')
plt.title("Wykres odległości wiązania")
plt.xlabel("Etapy wiązania")
plt.ylabel("Odległość wiązania")
plt.savefig('Odleglosci.png')
plt.show()

# Sprawdzenie poprawności wyboru indeksami ocen : Calińskiego i Harabasza oraz Silhouette
results = []
for k in range (2,8):
       label = fcluster(lincage_data, k, criterion='maxclust')
       ch = calinski_harabasz_score(X, label)
       ss = silhouette_score(X, label)

       results.append({
              'Liczba skupień':k,
              'Calinski Harabasz Score':round(ch,4),
              'Silhouette Score':round(ss,4)
       })
scores = pd.DataFrame(results)
scores.to_excel('Wald_Scores.xlsx')


data['Klaster_Hierarchiczny'] = fcluster(lincage_data, t=3, criterion='maxclust')
data.to_excel('Analiza_Skupien_Wyniki.xlsx')