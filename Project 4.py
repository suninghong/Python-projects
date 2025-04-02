'''
Suning Hong, Scott Turney
CS 101
11/17/2024
Project 04
'''
from PIL import Image, ImageDraw, ImageFont # From the PIL package
from random import randint
import random
import os  # Used to check if the file path exists


# Draw the background
def draw_ground_and_sky(draw):
    draw.rectangle((0, 0, 500, 400), fill=(0, 0, 50))  # Dark blue sky
      
    # Fill the ground with random colors
    for y in range(int(500 * 0.8), 500): 
        for x in range(0, 500):
            r = random.randint(0, 120) # Not very intense color of red
            g = random.randint(100, 200)  #Relatively strong green color but not too intense
            b = random.randint(200, 255)  # This give us a dominant blue tone
            draw.point((x, y), fill=(r, g, b))

# Add stars to the sky
def add_stars(draw, count):
    for _ in range(count):
        x, y = randint(0, 500), randint(0, 230)  
        draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill="gold")

# Insert images (character characters)
def insert_character(canvas, character_image_path, position, size):
    if not os.path.exists(character_image_path):
        print(f"Error: '{character_image_path}' file does not exist. Please ensure the file path is correct.")
        return
    character_image = Image.open(character_image_path)
    character_image = character_image.resize(size)
    canvas.paste(character_image, position)


# Write text on the canvas
def write_sentence(draw, text):
    text_position = (50, 430)
    font_path = "/Library/Fonts/Georgia.ttf"  # From peers 
    font = ImageFont.truetype(font_path, 30)
    draw.text(text_position, text, "black", font)

# Select and insert character images
def enter_image(canvas):
    character_images = []
    for i in range(4):
        character = input(f"Enter the {i+1} character (e.g., Girl1, Girl2, Smurf1, Smurf2): ") + ".png"
        character_images.append(character)
    
    positions = [(350, 250), (250, 250), (110, 250), (0, 250)]
    for i, image in enumerate(character_images):
        insert_character(canvas, image, position=positions[i], size=(125, 125)) # The most difficult part of the code

# Apply vintage filter
def apply_vintage_filter(canvas):
    width, height = canvas.size
    pixels = canvas.load()
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            new_r = min(int(r * 1.1), 255)  # Enhance red
            new_g = int(g * 0.9)  # Reduce green
            new_b = int(b * 0.8)  # Reduce blue
            pixels[x, y] = (new_r, new_g, new_b, a)
    return canvas

# Main function
def main():
    canvas = Image.new("RGBA", (500, 500), (255, 255, 255, 255))  # Create a blank canvas
    draw = ImageDraw.Draw(canvas)  # Initialize the draw object

    draw_ground_and_sky(draw)  # Draw the background
    add_stars(draw, 100)  # Add stars

    # User selects the quote
    first_sentence = "(1) You are not alone"
    second_sentence = "(2) Happy Children's Day"
    third_sentence = "(3) Welcome to the Cartoon World"
    text = input(f"Choose the positive quote you want to add to the image: {first_sentence} {second_sentence} {third_sentence}\n, please type the sentence!\n")
    write_sentence(draw, text)  # Write text on the image

    # Insert character images
    enter_image(canvas)
    
    # Ask if the user wants to apply the vintage filter
    apply_filter = input("Would you like to apply a vintage filter? (y/n): ").lower()
    if apply_filter == 'y':
        canvas = apply_vintage_filter(canvas)  # Apply vintage filter
    
    canvas.show()  # Display the final image

if __name__ == "__main__":
    main()
