import os
import shutil
import rembg
from tqdm import tqdm

def remove_background(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in tqdm(os.listdir(input_folder), desc="Processing images"):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)

            # Remove the file extension and add "_removed" to the filename
            output_filename = os.path.splitext(filename)[0] + "_removed" + os.path.splitext(filename)[1]
            output_path = os.path.join(output_folder, output_filename)

            with open(input_path, "rb") as input_file:
                with open(output_path, "wb") as output_file:
                    output_file.write(rembg.remove(input_file.read()))

if __name__ == "__main__":
    input_folder = r"C:\Users\user\OneDrive\Desktop\models"
    output_folder = r"C:\Users\user\OneDrive\Desktop\images"

    remove_background(input_folder, output_folder)
