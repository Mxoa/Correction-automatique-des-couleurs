import cv2
import numpy as np

def load_image(image_path):
    image = cv2.imread(image_path)
    return np.array(image)

def save_image(image, name="image"):
    cv2.imwrite(f"images/{name}.png", image)

if __name__ == "__main__":
    image = load_image("images/test1.jpg")
    print("Shape", image.shape)
    