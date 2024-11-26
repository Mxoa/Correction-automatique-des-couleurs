import cv2
import numpy as np

def load_image(image_path, lab=False):
    try:
        image = cv2.imread(image_path)
        if image.shape == ():
            raise Exception("Error while loading the image")
        
        if lab:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        
        return np.array(image)
    except:
        print("Error while loading the image")
        raise Exception("Error while loading the image")

def save_image(image, name="image", lab=False):
    image.astype(np.uint8)
    if lab:
        image[:, :, 0] = np.clip(image[:, :, 0], 0, 255)
        image[:, :, 1] = np.clip(image[:, :, 1], 0, 255)
        image[:, :, 2] = np.clip(image[:, :, 2], 0, 255)
        image = cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_LAB2BGR)
    cv2.imwrite(f"{name}", image)
    print(f"Image saved as {name}")

if __name__ == "__main__":
    image = load_image("images/article_pont.png")
    print("Shape", image.shape)
    print("Type", type(image))
    print("Max L", image[:, :, 0].max())
    print("Min L", image[:, :, 0].min())
    print("Max A", image[:, :, 1].max())
    print("Min A", image[:, :, 1].min())
    print("Max B", image[:, :, 2].max())
    print("Min B", image[:, :, 2].min())
    save_image(image, "test1_saveds.jpg")
    