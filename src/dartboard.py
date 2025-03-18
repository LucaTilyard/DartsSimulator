import numpy as np
import matplotlib.pyplot as plt

class Dartboard:
    """
        A class to represent a dartboard for scoring and plotting darts.

        This class provides methods to initialize the dartboard, plot it using matplotlib,
        and calculate the score based on the position of a dart.

        Attributes
        ----------
        dartboard_angles : numpy.ndarray
            Angles for the dartboard segments.
        angels2 : numpy.ndarray
            Extended angles for the dartboard segments.
        all_angles : numpy.ndarray
            All angles for plotting the dartboard.
        radii : list
            Radii for different scoring areas on the dartboard.
        board_order : list
            Order of numbers on the dartboard.
        number_plotting_angles : numpy.ndarray
            Angles for plotting the numbers around the dartboard.
        number_plotting_radii : float
            Radius for plotting the numbers around the dartboard.

        Methods
        -------
        __str__():
            Returns a string representation of the dartboard.
        plot():
            Plots the dartboard using matplotlib.
        CalculateValue(r, theta):
            Calculates the score value based on the radial distance and angle.
    """

    def __init__(self):
        """
            Initializes the Dartboard class.

            This method sets up the dartboard with predefined angles, radii, and board order.
            It also prepares the plotting parameters for the dartboard.

            Parameters
            ----------

            Returns
            -------
            None
        """
        self.dartboard_angles = np.linspace(1/20*np.pi - np.pi, np.pi+1/20*np.pi, 21)
        self.angels2 = np.linspace(-np.pi-(1/20*np.pi), np.pi+(1/20*np.pi), 22)
        self.all_angles = np.linspace(-np.pi, np.pi, 1000)
        self.radii = [127/3400, 8/85, 99/170, 107/170, 81/85, 1.0, 1.2]
        self.board_order = [11, 8, 16, 7, 19, 3, 17, 2, 15, 10, 6, 13, 4, 18, 1, 20, 5, 12, 9, 14]
        self.number_plotting_angles = np.linspace(-np.pi, np.pi, 21)
        self.number_plotting_radii = 1.11

    def __str__(self):
        return "Dartboard providing scoring and plotting"

    def plot(self):
        """
           Plots the dartboard using matplotlib.

           This method creates a polar plot of the dartboard, including the bullseye,
           single, double, and treble scoring areas, as well as the numbers around the
           board.

           Parameters
           ----------


           Returns
           -------
           fig : matplotlib.figure.Figure
               The figure object containing the plot.
           ax : matplotlib.axes._subplots.PolarAxesSubplot
               The axes object containing the plot.
        """
        # Create a polar plot
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

        # Draw circles
        for r in self.radii:
            ax.plot(self.all_angles, [r] * len(self.all_angles), color='grey', linewidth=0.8)

        # Draw radii
        for angle in self.dartboard_angles:
            ax.plot([angle, angle], [self.radii[1], 1], color='grey', linewidth=0.8)

        # Remove axes
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_yticks([])
        ax.set_frame_on(False)
        ax.grid(False)

        # Colouring in Board
        for i in range(20):
            theta1 = self.dartboard_angles[i]
            theta2 = self.dartboard_angles[i + 1]
            theta = np.linspace(theta1, theta2, 50)

            # singles
            single_colour = 'black' if i % 2 == 0 else 'beige'
            ax.fill_between(theta, np.full_like(theta, self.radii[1]), np.full_like(theta, self.radii[2]), color=single_colour)
            ax.fill_between(theta, np.full_like(theta, self.radii[3]), np.full_like(theta, self.radii[4]), color=single_colour)

            # doubles and trebles
            treble_colour = 'red' if i % 2 == 0 else 'green'
            ax.fill_between(theta, np.full_like(theta, self.radii[4]), np.full_like(theta, self.radii[5]), color=treble_colour)
            ax.fill_between(theta, np.full_like(theta, self.radii[2]), np.full_like(theta, self.radii[3]), color=treble_colour)

        # Bullseye
        ax.fill_between(self.all_angles, self.radii[0], self.radii[1], color='green')
        ax.fill_between(self.all_angles, 0, self.radii[0], color='red')

        # Outer board
        ax.fill_between(self.all_angles, self.radii[5], self.radii[6], color='black')

        # Draw numbers
        for i in range(20):
            ax.text(self.number_plotting_angles[i], self.number_plotting_radii, str(self.board_order[i]), fontsize=13, ha='center',
                    va='center', fontdict={'family': 'serif', 'style': 'italic', 'weight': 'bold'}, color='white')

        return fig, ax

    def calculate_value(self, r, theta):
        """
            Calculate the score value based on the radial distance and angle.

            Parameters
            ----------
            r : float
                The radial distance from the center of the dartboard.
            theta : float
                The angle in radians from the positive x-axis.

            Returns
            -------
            int
                The score value based on the position on the dartboard.
        """
        multiplier = 1
        # This board order has one extra entry compared to the value given in the class it's self
        # Ideally fix this so this method uses the classes value but for now this works
        board_order = [11, 8, 16, 7, 19, 3, 17, 2, 15, 10, 6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11]

        # Within board.
        if r > 1:
            return 0

        # Bullseye.
        if r < 127 / 3400:
            return 50

        # Outer Bullseye.
        if r < 8 / 85:
            return 25

        # Triple.
        if (99 / 170) < r < (107 / 170):
            multiplier = 3

        # Double.
        if (81 / 85) < r < 1:
            multiplier = 2

        # Calculate total score.
        for i in range(21):
            if theta < self.angels2[i + 1]:
                return multiplier * board_order[i]
            i += 1