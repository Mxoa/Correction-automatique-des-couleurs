import cv2
import numpy as np

def load_image(image_path):
    try:
        image = cv2.imread(image_path)
        if image.shape == ():
            raise Exception("Error while loading the image")
        return np.array(image)
    except:
        print("Error while loading the image")
        raise Exception("Error while loading the image")

def save_image(image, name="image"):
    cv2.imwrite(f"{name}.png", image)

if __name__ == "__main__":
    image = load_image("images/test1.jpg")
    print("Shape", image.shape)
    