from PIL import Image

img = Image.open("jigsaw.webp")

img_size = 500
grid_size = 5
tile_size = img_size // grid_size

mapping = [
    ((2,1),(0,0)), ((1,1),(0,1)), ((4,1),(0,2)), ((0,3),(0,3)), ((0,1),(0,4)),
    ((1,4),(1,0)), ((2,0),(1,1)), ((2,4),(1,2)), ((4,2),(1,3)), ((2,2),(1,4)),
    ((0,0),(2,0)), ((3,2),(2,1)), ((4,3),(2,2)), ((3,0),(2,3)), ((3,4),(2,4)),
    ((1,0),(3,0)), ((2,3),(3,1)), ((3,3),(3,2)), ((4,4),(3,3)), ((0,2),(3,4)),
    ((3,1),(4,0)), ((1,2),(4,1)), ((1,3),(4,2)), ((0,4),(4,3)), ((4,0),(4,4))
]

unscrambled = Image.new("RGB", (img_size, img_size))

for (orig_row, orig_col), (scr_row, scr_col) in mapping:
    left = scr_col * tile_size
    upper = scr_row * tile_size
    right = left + tile_size
    lower = upper + tile_size
    tile = img.crop((left, upper, right, lower))
    
    paste_left = orig_col * tile_size
    paste_upper = orig_row * tile_size
    unscrambled.paste(tile, (paste_left, paste_upper))

unscrambled.save("jigsaw-unscrambled.png")
