import tabula
import pandas as pd

pdf_path = "./q-extract-tables-from-pdf.pdf"
bounding_box = [80, 20, 750, 570] # The coordinates are reversed from pdfplumber

# import pdfplumber
# from PIL import Image, ImageDraw
#
# with pdfplumber.open(pdf_path) as pdf:
#     page = pdf.pages[0]
#
#     im = page.to_image()
#     draw = ImageDraw.Draw(im.original)
#     draw.rectangle(bounding_box, outline="red", width=5)
#
#     im.original.save('temp.png')

combined_df = pd.DataFrame(columns=["Maths", "Physics", "English", "Economics", "Biology"])

tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True, area=bounding_box)

for i, table in enumerate(tables):
    if 25 <= i < 57:
        combined_df = pd.concat([combined_df, table], ignore_index=True)

print(combined_df.shape)
print(combined_df[combined_df['English'] >= 31]['Physics'].sum())