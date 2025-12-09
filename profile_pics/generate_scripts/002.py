from PIL import Image, ImageDraw

# Image size
img_size = 512
square_size = 40
commit_color = (57, 211, 83)  # GitHub green

# Create black background
img = Image.new('RGB', (img_size, img_size), (0, 0, 0))
draw = ImageDraw.Draw(img)

# Calculate squares positions
x1 = (img_size / 2) - (1.5 * square_size)
x2 = (img_size / 2) + (0.5 * square_size)
y = (img_size / 2) - (0.5 * square_size)

# Draw the green commit square
corner_radius = 6  # Adjust as needed for roundness
for x in [x1, x2]:
    draw.rounded_rectangle(
        [x, y, x + square_size, y + square_size],
        radius=corner_radius,
        fill=commit_color
    )

# Save it
img.save('002.png')
