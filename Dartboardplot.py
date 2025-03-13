import numpy as np
import matplotlib.pyplot as plt

def plot_dartboard():
    # Angles of scoring sections
    dartboard_angles = np.linspace(1/20*np.pi - np.pi, np.pi+1/20*np.pi, 21)

    # for a smooth plot
    all_angles = np.linspace(-np.pi, np.pi, 1000)

    radii = [127/3400, 8/85, 99/170, 107/170, 81/85, 1.0] 

    # Create a polar plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    #Draw circles
    for r in radii:
        ax.plot(all_angles, [r] * len(all_angles), color='grey')

    # Draw radii
    for angle in dartboard_angles:
        ax.plot([angle, angle], [radii[1], 1], color='grey')

    # Remove axes
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    ax.grid(False)

    #Colouring in Board
    for i in range(20):
        theta1 = dartboard_angles[i]
        theta2 = dartboard_angles[i+1]
        theta = np.linspace(theta1, theta2, 50) 

        # singles
        single_colour = 'black' if i % 2 == 0 else 'beige'
        ax.fill_between(theta, np.full_like(theta, radii[1]), np.full_like(theta, radii[2]), color=single_colour)
        ax.fill_between(theta, np.full_like(theta, radii[3]), np.full_like(theta, radii[4]), color=single_colour)

        # doubles and trebles
        treble_colour = 'red' if i % 2 == 0 else 'green'
        ax.fill_between(theta, np.full_like(theta, radii[4]), np.full_like(theta, radii[5]), color=treble_colour)
        ax.fill_between(theta, np.full_like(theta, radii[2]), np.full_like(theta, radii[3]), color=treble_colour)
    
    # Bullseye
    ax.fill_between(all_angles, radii[0], radii[1], color='green')
    ax.fill_between(all_angles, 0, radii[0], color='red')

    return fig, ax
