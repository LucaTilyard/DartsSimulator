from player import *
import matplotlib.pyplot as plt

luke_the_fluke_shittler = Player(1000)

print(luke_the_fluke_shittler.Throw(100))

def ConvertToPolar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# Load the image
image = plt.imread('src/dartboard.png')

# Create a figure and axis
fig, ax = plt.subplots()

# Display the image
ax.imshow(image, extent=[-1.345, 1.345, -1.345, 1.345])

plt.xlim(-1.345, 1.345)
plt.ylim(-1.345, 1.345)

ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
i = 0

while i < 3:
    throw = luke_the_fluke_shittler.Throw(1)
    print(ConvertToPolar(throw[0], throw[1]))
    plt.scatter(throw[0], throw[1], s=3, c='yellow', marker='o')
    i += 1

plt.show()

