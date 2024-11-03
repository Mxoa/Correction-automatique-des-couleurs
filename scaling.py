import numpy as np
import loader as ld
import tqdm

def scaling(image, channel=0):
    """
    
    | channel : int, the channel to rescale, 0 = red, 1 = green, 2 = blue
    | image : numpy array, the image to rescale
    Rescale the image channel 'channel' to the range [0, 255] 
    Associate the minimum value of the channel to 0 and the maximum value to 255.
    Modify the image in place.
    
    """
    
    print("Scaling an image of shape ", image[:, :, 0].shape)
    print(" | Channel ", channel)
    print(" | max/min ", image[:, :, channel].max(), image[:, :, channel].min())
    print(" | mean ", image[:, :, channel].mean())
    
    max_intensity = image[:, :, channel].max()
    min_intensity = image[:, :, channel].min()
    
    for i in tqdm.tqdm(range(image.shape[0])):
        for j in range(image.shape[1]):
            intensity = np.round(255 * (image[i, j, channel] - min_intensity) / (max_intensity - min_intensity))
            image[i, j, channel] = intensity
            

    
    

def scaling_gw_wp(image_r, channel=0):
    """
    
    | channel : int, the channel to rescale, default 0 = all channels, 1 = red, 2 = green, 3 = blue
    | image_r : numpy array, the image to rescale with the white point and the gray world algorithm, should be in [-1, 1]
    Rescale the image channel 'channel' to the range [0, 255] 
    Associate the mid value of the channel to 127.5 and the maximum value to 255.
    Modify the image in place.
    
    """
    print(" |------------------------------------------------------------------|")
    print(" | Scaling an image of shape ", image_r[:, :, 0].shape)
    print(" | Channel ", channel)
    print(" | max/min ", image_r[:, :, channel].max(), image_r[:, :, channel].min())
    print(" | mean ", image_r[:, :, channel].mean())
    
    I = image_r.copy()
    #I = I - I.min()
    
    max_channel = I[:, :, channel].max()
    
    for i in tqdm.tqdm(range(image_r.shape[0])):
        for j in range(image_r.shape[1]):
            intensity = np.round(127.5 + image_r[i, j, channel] / max_channel * 127.5)
            image_r[i, j, channel] = intensity


if __name__ == "__main__":
    img = ld.load_image("images/test1.jpg")
    img = scaling(img)
    img = scaling(img, 1)
    img = scaling(img, 2)
    ld.save_image(img, "test1_scaled")