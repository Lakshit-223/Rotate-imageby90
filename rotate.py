import os
import sys
from PIL import Image

# Function to rotate the image
def rotate_image(input_image_path):
    # Open the image
    image = Image.open(input_image_path)

    # Rotate the image by 90 degrees clockwise
    rotated_image = image.transpose(Image.ROTATE_90)

    # Get the directory of the input image
    input_dir = os.path.dirname(input_image_path)

    # Get the filename of the input image
    input_filename = os.path.basename(input_image_path)

    # Construct the output image path in the same directory with a suffix
    output_image_path = os.path.join(input_dir, "rotated_" + input_filename)

    # Save the rotated image
    rotated_image.save("rotated.png")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_image_path>")
        sys.exit(1)

    input_image_path = "AcceptString.png"
    rotate_image(input_image_path)
