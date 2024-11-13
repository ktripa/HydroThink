import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs

# Set up the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10), subplot_kw={'projection': ccrs.Robinson()})
ax.set_global()
ax.stock_img()
ax.coastlines()
ax.add_feature(cartopy.feature.BORDERS, linestyle=':')

plt.title('World Map with Topography')
plt.show()
