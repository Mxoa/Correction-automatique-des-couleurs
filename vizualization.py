from matplotlib import pyplot as plt
import matplotlib
import loader as ld
import numpy as np

matplotlib.use('tkagg')


def show_histogram(image, channel=0):
    """
    
    | image : numpy array, the image to display the histogram
    | channel : int, the channel to display, 0 = red, 1 = green, 2 = blue
    Display the histogram of the image channel 'channel'.
    
    """
    data = image[:, :, channel].flatten()
    
    
    plt.hist(data, bins=256, range=(0, 256), density=True, color=('r' if channel == 0 else ('g' if channel == 1 else 'b')), alpha=0.75)
    plt.xlabel('Intensity value')
    plt.ylabel('Frequency')
    plt.title('Histogram of the image')
    plt.show()
    

def show_histogram_rgb(image):
    """
    
    | image : numpy array, the image to display the histogram
    Display the histograms of 'image'. (RGB)
    
    """
    
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    # Red channel histogram
    axs[0].hist(image[:, :, 0].flatten(), bins=256, range=(0, 256), density=True, color='r', alpha=0.75)
    axs[0].set_xlabel('Intensity value')
    axs[0].set_ylabel('Frequency')
    axs[0].set_title('Red Channel Histogram')

    # Green channel histogram
    axs[1].hist(image[:, :, 1].flatten(), bins=256, range=(0, 256), density=True, color='g', alpha=0.75)
    axs[1].set_xlabel('Intensity value')
    axs[1].set_ylabel('Frequency')
    axs[1].set_title('Green Channel Histogram')

    # Blue channel histogram
    axs[2].hist(image[:, :, 2].flatten(), bins=256, range=(0, 256), density=True, color='b', alpha=0.75)
    axs[2].set_xlabel('Intensity value')
    axs[2].set_ylabel('Frequency')
    axs[2].set_title('Blue Channel Histogram')

    plt.tight_layout()
    plt.ion()
    
    plt.show()
    
def save_histogram_rgb(image, name):
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    # Red channel histogram
    axs[0].hist(image[:, :, 0].flatten(), bins=256, range=(0, 256), density=True, color='r', alpha=0.75)
    axs[0].set_xlabel('Intensity value')
    axs[0].set_ylabel('Frequency')
    axs[0].set_title('Red Channel Histogram')

    # Green channel histogram
    axs[1].hist(image[:, :, 1].flatten(), bins=256, range=(0, 256), density=True, color='g', alpha=0.75)
    axs[1].set_xlabel('Intensity value')
    axs[1].set_ylabel('Frequency')
    axs[1].set_title('Green Channel Histogram')

    # Blue channel histogram
    axs[2].hist(image[:, :, 2].flatten(), bins=256, range=(0, 256), density=True, color='b', alpha=0.75)
    axs[2].set_xlabel('Intensity value')
    axs[2].set_ylabel('Frequency')
    axs[2].set_title('Blue Channel Histogram')

    plt.tight_layout()
    plt.savefig(f'histograms/{name.split("/")[-1].split(".")[0]}_histogram.png')
    plt.close()
        
        
def save_channel_rgb(image, channel, name):
    fig, ax = plt.subplots()
    ax.imshow(image[:, :, channel], cmap='gray')
    plt.savefig(f'channels/{name.split("/")[-1].split(".")[0]}_channel_{channel}.png')
    plt.close()

if __name__ == "__main__":
    img = ld.load_image("images/test1.jpg")
    show_histogram_rgb(img)
    img = ld.load_image("images/test1_scaled.png")
    
    show_histogram_rgb(img)