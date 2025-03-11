import numpy as np
import matplotlib.pyplot as plt

# Dartboard Score Sections (Angles)
angles = np.linspace(1/20*np.pi, 2 * np.pi+1/20*np.pi, 21)

#Generate all angles for a smooth plotting
all_angles = np.linspace(0, 2 * np.pi, 1000)

# Rings (Dartboard Circles)
radii = [0.028, 0.071, 0.582, 0.629, 0.953, 1.0] 

# Create a polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Draw the circular dartboard rings
for r in radii:
    ax.plot(all_angles, [r] * len(all_angles), color='black')

# Draw the radial lines for 20 segments
for angle in angles:
    ax.plot([angle, angle], [0, 1], color='black')

# Remove axes
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_frame_on(False)

# Colouring in sections

plt.show()