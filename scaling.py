import numpy as np
import loader as ld

def scaling(image, channel=0):
    """
    
    | channel : int, the channel to rescale, default 0 = all channels, 1 = red, 2 = green, 3 = blue
    | image : numpy array, the image to rescale
    Rescale the image channel 'channel' to the range [0, 255] 
    Associate the minimum value of the channel to 0 and the maximum value to 255.
    Return a copy of the image.
    
    """
    
    #print(image[:, :, 0].shape)
    
    max_intensity = image[:, :, channel].max()
    min_intensity = image[:, :, channel].min()
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            intensity = np.round(255 * (image[i, j, channel] - min_intensity) / (max_intensity - min_intensity))
            image[i, j, channel] = intensity
            
    return image

    
    

def scaling_gw_wp(image_r, channel=0):
    """
    
    | channel : int, the channel to rescale, default 0 = all channels, 1 = red, 2 = green, 3 = blue
    | image_r : numpy array, the image to rescale with the white point and the gray world algorithm, should be in [-1, 1]
    Rescale the image channel 'channel' to the range [0, 255] 
    Associate the mid value of the channel to 127.5 and the maximum value to 255.
    Modify the image in place.
    
    """
    I = image_r[:, :][channel]
    I = I - I.min()
    I = np.round(127.5 + I / I.max() * 127.5)
    image_r[:, :][channel] = I


if __name__ == "__main__":
    img = ld.load_image("images/test1.jpg")
    img = scaling(img)
    img = scaling(img, 1)
    img = scaling(img, 2)
    ld.save_image(img, "test1_scaled")