# Write a Python program to load an image file, display it using Matplotlib,
# and create a color-inverted version of the image. Display both the original
# and inverted images for comparison.

import numpy as np
import matplotlib.pyplot as plt


# Load image
try:
    logo = plt.imread('numpy-logo.png')

    # Create a copy of the original image
    dark_logo = logo.copy()

    # Invert RGB channels
    if logo.dtype == np.uint8:
        dark_logo[..., :3] = 255 - dark_logo[..., :3]
    else:
        dark_logo[..., :3] = 1 - dark_logo[..., :3]

    # Display both images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original NumPy Logo")
    plt.grid(False)
    plt.imshow(logo)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("NumPy Dark Logo")
    plt.grid(False)
    plt.imshow(dark_logo)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("NumPy logo not found")