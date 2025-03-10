import numpy as np
import matplotlib.pyplot as plt

# Dartboard Score Sections (Angles)
angles = np.linspace(1/20*np.pi, 2 * np.pi+1/20*np.pi, 21)  # 20 sections

print(angles)
# Rings (Dartboard Circles)
radii = [0.028, 0.071, 0.582, 0.629, 0.953, 1.0] 

fig, ax = plt.subplots(figsize=(6,6), subplot_kw={'projection': 'polar'})

# Draw the circular dartboard rings
for r in radii:
    ax.add_patch(plt.Circle((0, 0), r, transform=ax.transData._b, color="black", fill=False, lw=2))

# Draw the radial lines for 20 segments
for angle in angles:
    ax.plot([angle, angle], [0, 1], color='black')

# Remove axes
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.show()