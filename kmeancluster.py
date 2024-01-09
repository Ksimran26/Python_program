from flask import Flask,render_template
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import haversine_distances
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from sklearn.cluster import AgglomerativeClustering
import geopandas as gpd
import folium

# Read the data from Excel
df = pd.read_excel(r'C:\Users\simranpreet\Downloads\archive\sales.xlsx')
print(df)

# Function to convert latitude and longitude to radians
def degrees_to_radians(degrees):
    return degrees * np.pi / 180

# Function to calculate distance using Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(degrees_to_radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    d_lat = lat2_rad - lat1_rad
    d_lon = lon2_rad - lon1_rad
    a = np.sin(d_lat/2) ** 2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(d_lon/2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    
    # Earth's radius in miles
    earth_radius_miles = 3958.8
    
    # Calculate the distance
    distance = earth_radius_miles * c
    return distance

# Extract latitude and longitude columns
store_coords = df[['Latitude', 'Longitude']].values

# Calculate the distance matrix using Haversine formula
distances = haversine_distances(np.radians(store_coords))
distances = distances * 3958.8  # Convert the distances from radians to miles

# Perform k-means clustering
clusters = 30
kmeans = KMeans(n_clusters=clusters, random_state=42)
clusters = kmeans.fit_predict(distances)

# Separate the stores based on the clusters
clustered_stores = {}
for i, label in enumerate(clusters):
    if label not in clustered_stores:
        clustered_stores[label] = []
    clustered_stores[label].append(store_coords[i])

    label = np.unique(label)
    centroids = kmeans.cluster_centers_
# Points assigned to each cluster
clusters_with_points = {cluster: store_coords[clusters == cluster] for cluster in range(len(np.unique(clusters)))}
# print("Stores in each cluster (Latitude, Longitude):")
# for cluster, points in clusters_with_points.items():
#     # print(f"Cluster {cluster}:{points}")
#     print(f"{cluster}")

ac = AgglomerativeClustering(n_clusters=21)
df['n_clusters'] = ac.fit_predict(df.iloc[:,6:8].values)
df_table = tabulate(df, headers='keys', tablefmt="simple")
# print(df_table)

# Plot the stores in clusters
df['n_clusters'] = clusters
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.scatterplot(x=df['Latitude'], y=df['Longitude'],label =i , hue=df['n_clusters'], palette = "deep")
# plt.title('Stores in Clusters', fontweight='bold', fontsize=20, color='purple', loc='center')
# plt.show()

map_center = [np.mean(df['Latitude']), np.mean(df['Longitude'])]
map_instance = folium.Map(location=map_center, zoom_start=10)

def set_marker_icon(store_size):
    if store_size == 'Small':
        return 'shopping-cart'
    elif store_size == 'Medium':
        return 'shopping-bag'
    elif store_size == 'High':
        return 'store'
    else:
        return 'circle'
    
def set_marker_color(cluster_label):
    color_palette = ['lightgreen', 'red', 'lightblue', 'green', 'darkblue', 'beige', 'darkpurple', 'darkred', 'purple', 'lightred', 
                     'black','orange', 'lightgray', 'white', 'cadetblue', 'gray', 'blue', 'darkgreen', 'pink']
    return color_palette[cluster_label % len(color_palette)]

for index, row in df.iterrows():
    size_icon = set_marker_icon(row['Volume'])
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=(row['Store'], row['Volume']),
        icon=folium.Icon(color=set_marker_color(row['n_clusters']), prefix='fa', icon=size_icon)
    ).add_to(map_instance)

map_instance.save("clustered_stores_map.html")

