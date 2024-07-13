from pdf2image import convert_from_path

def pdf_to_png(pdf_path):
    images = convert_from_path(pdf_path,poppler_path = r"C:\Users\Bhavya\Projects\Python Projects\HandwritingConversion\poppler-24.02.0\Library\bin")
    for i, image in enumerate(images):
        image.save(f'char_page_{i+1}.png', 'PNG')

# Example usage
pdf_file = 'Calligraphr-Template.pdf'  # Replace with your PDF file path  # Folder where PNGs will be saved
pdf_to_png(pdf_file)
