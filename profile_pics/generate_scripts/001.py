from PIL import Image, ImageDraw

# Image size
img_size = 512
square_size = 40
commit_color = (57, 211, 83)  # GitHub green

# Create black background
img = Image.new('RGB', (img_size, img_size), (0, 0, 0))
draw = ImageDraw.Draw(img)

# Calculate square position
x = (img_size - square_size) // 2
y = (img_size - square_size) // 2

# Draw the green commit square
corner_radius = 6  # Adjust as needed for roundness
draw.rounded_rectangle(
    [x, y, x + square_size, y + square_size],
    radius=corner_radius,
    fill=commit_color
)

# Save it
img.save('001.png')
