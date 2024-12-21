from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):

    with open(input_path, 'rb') as input_file:
        input_image = input_file.read()

    output_image = remove(input_image)

    with open(output_path, 'wb') as output_file:
        output_file.write(output_image)

if __name__ == "__main__":

    input_image_path = './img/1.jpg'  
    output_image_path = './img/output_image.png' 

    remove_background(input_image_path, output_image_path)
    print(f"Background removed. Saved to {output_image_path}")
