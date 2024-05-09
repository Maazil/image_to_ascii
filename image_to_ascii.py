from PIL import Image

# ASCII characters from dark to light
ASCII_CHARS = [' ', '.', ':', '=', '+', '*','X', '#', '%', '@']

def image_to_ascii(image_path, output_width=100):
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale

    # Calculate the aspect ratio of the image and scale the height accordingly
    width, height = image.size
    aspect_ratio = height / width
    output_height = int(aspect_ratio * output_width)

    # Resize the image while maintaining aspect ratio
    image = image.resize((output_width, output_height))

    # Convert the image to ASCII text
    # Each pixel is represented by an ASCII character based on its brightness
    # The brightness is calculated by dividing the pixel value by 255 (maximum brightness value)
    ascii_image = ""
    for y in range(output_height):
        for x in range(output_width):
            pixel_brightness = image.getpixel((x, y)) / 255
            ascii_image += ASCII_CHARS[int(pixel_brightness * (len(ASCII_CHARS) - 1))]
        ascii_image += '\n'

    return ascii_image

def save_ascii_to_file(ascii_image, file_path):
    with open(file_path, 'w') as f:
        f.write(ascii_image)

if __name__ == "__main__":
    image_path = "matty.jpg"
    output_file = "matty.txt"
    ascii_image = image_to_ascii(image_path)
    save_ascii_to_file(ascii_image, output_file)
    print("ASCII representation saved to", output_file)
