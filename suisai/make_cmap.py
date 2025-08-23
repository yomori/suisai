import matplotlib

#https://photocontest.smithsonianmag.com/photocontest/detail/a-crescent-moon-death-valley/
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#120E17','#423647','#72556A',"#B8756C", "#DB8C5C",'#F9BF5D','#F5F2ED' ])
rgbtemp = cmap(np.linspace(0, 1, 512))[np.newaxis, :, :3][0]
np.savetxt('forestdawna-rgb.txt', rgbtemp)
plt.imshow(np.arange(900).reshape(30,30),cmap=cmap)


