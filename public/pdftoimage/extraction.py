import cv2
import os

# Load the big images
big_image1 = cv2.imread('big_images/image1.jpeg')
big_image2 = cv2.imread('big_images/image2.jpeg')

# Define the number of rows, columns, and the size of each small image
num_rows = 12
num_columns = 6
space_width = 59  # Update this value with the actual spacing width
space_height = 43  # Update this value with the actual spacing height
small_image_height = (big_image1.shape[0] - (num_rows - 1) * space_height) // num_rows
small_image_width = (big_image1.shape[1] - (num_columns - 1) * space_width) // num_columns

# Create the output directory if it doesn't exist
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Iterate through each row and column combination
for row in range(num_rows):
    for column in range(num_columns):
        # Calculate the coordinates of the top-left and bottom-right corners of the small image
        top_left_x = column * (small_image_width + space_width)
        top_left_y = row * (small_image_height + space_height)
        bottom_right_x = top_left_x + small_image_width
        bottom_right_y = top_left_y + small_image_height
        
        # Extract the small image from big_image1
        small_image1 = big_image1[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

        # Extract the small image from big_image2
        small_image2 = big_image2[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

       # Generate the new filename for the small images
    
        image_number = row * num_columns + column + 1
        filename1 = f'{output_dir}/image{image_number}_1.jpg'
        filename2 = f'{output_dir}/image{image_number}_2.jpg'

        # Save the small images with the new filenames
        cv2.imwrite(filename1, small_image1)
        cv2.imwrite(filename2, small_image2)

        # Continue with the next column
    # Continue with the next row