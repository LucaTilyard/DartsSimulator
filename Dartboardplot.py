import numpy as np
import matplotlib.pyplot as plt

def plot_dartboard():
    # Angles of scoring sections
    dartboard_angles = np.linspace(1/20*np.pi - np.pi, np.pi+1/20*np.pi, 21)

    # for a smooth plot
    all_angles = np.linspace(-np.pi, np.pi, 1000)

    radii = [127/3400, 8/85, 99/170, 107/170, 81/85, 1.0, 1.2]

    # Values for the plots of numbers
    BoardOrder = [11,8,16,7,19,3,17,2,15,10,6,13,4,18,1,20,5,12,9,14]
    number_plotting_angles = np.linspace(-np.pi, np.pi, 21)
    number_plotting_radii = 1.11

    # Create a polar plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    #Draw circles
    for r in radii:
        ax.plot(all_angles, [r] * len(all_angles), color='grey',linewidth=0.8)

    # Draw radii
    for angle in dartboard_angles:
        ax.plot([angle, angle], [radii[1], 1], color='grey',linewidth=0.8)

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

    #Outer board
    ax.fill_between(all_angles, radii[5], radii[6], color='black')

    # Draw numbers
    for i in range(20):
        ax.text(number_plotting_angles[i], number_plotting_radii, str(BoardOrder[i]), fontsize=13, ha='center', va='center', fontdict={'family': 'serif', 'style': 'italic', 'weight': 'bold'}, color = 'white')

    return fig, ax
