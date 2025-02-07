import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def chunk_data(data, chunk_size):
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def generate_qr_codes(chunks, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    total_chunks = len(chunks)
    for idx, chunk in enumerate(chunks):
        chunk_number = idx + 1
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(chunk)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        # Add chunk number to the center
        img = add_chunk_number_to_image(img, chunk_number, total_chunks)
        
        # Save the image
        img_filename = os.path.join(output_dir, f'chunk_{chunk_number:03}.png')
        img.save(img_filename)
        print(f'QR code saved: {img_filename}')

def add_chunk_number_to_image(img, chunk_number, total_chunks):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font_size = int(height * 0.1)  # Font size relative to image height
    try:
        # Try to use a TrueType font
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # Fallback to default PIL font if TrueType font is not available
        font = ImageFont.load_default()

    text = f"{chunk_number}/{total_chunks}"
    text_width, text_height = draw.textsize(text, font=font)
    
    # Calculate position to center the text
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2

    # Add a white rectangle behind the text for better visibility
    rect_padding = int(font_size * 0.2)
    rect_x0 = text_x - rect_padding
    rect_y0 = text_y - rect_padding
    rect_x1 = text_x + text_width + rect_padding
    rect_y1 = text_y + text_height + rect_padding
    draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill="white")

    # Draw the text over the rectangle
    draw.text((text_x, text_y), text, font=font, fill="black")
    return img

def main():
    input_file = 'your_source_code.py'  # Replace with your source code file path
    output_directory = 'qr_codes'
    chunk_size = 1200  # Adjusted chunk size for QR code capacity

    print("Reading the source file...")
    data = read_file(input_file)
    print("Splitting data into chunks...")
    chunks = chunk_data(data, chunk_size=chunk_size)
    print(f"Total chunks created: {len(chunks)}")
    print("Generating QR codes...")
    generate_qr_codes(chunks, output_directory)
    print("All QR codes have been generated successfully!")

if __name__ == '__main__':
    main()
