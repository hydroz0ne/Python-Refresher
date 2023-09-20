#PRefresher Activity 6
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colorremove = [0, 4, 5]
newcolors = [colors[i] for i in range(len(colors)) if i not in colorremove]
print('New color list:', newcolors)