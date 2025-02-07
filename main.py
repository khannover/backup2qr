import os
import qrcode
import base64
from PIL import Image, ImageDraw, ImageFont

def read_binary_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

def encode_data_to_base64(data):
    return base64.b64encode(data).decode('ascii')

def chunk_base64_data(data, chunk_size):
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def generate_qr_codes(chunks, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    total_chunks = len(chunks)
    for idx, chunk in enumerate(chunks):
        chunk_number = idx + 1
        # Prepare data with chunk info
        qr_data = f"{chunk_number}/{total_chunks}:{chunk}"
        
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        # Add chunk number in the center
        img = add_chunk_number_to_image(img, chunk_number, total_chunks)
        
        # Save the image
        img_filename = os.path.join(output_dir, f'chunk_{chunk_number:03d}.png')
        img.save(img_filename)
        print(f"QR code saved: {img_filename}")

def add_chunk_number_to_image(img, chunk_number, total_chunks):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font_size = int(height * 0.1)  # Adjust font size relative to image height
    try:
        # Use a TrueType font (adjust the path to the font as necessary)
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # Fall back to default font if TrueType font is unavailable
        font = ImageFont.load_default()
    
    text = f"{chunk_number}/{total_chunks}"
    text_width, text_height = draw.textsize(text, font=font)
    
    # Calculate position to center the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw a white rectangle behind the text for readability
    background_size = (text_width + 10, text_height + 10)
    background_position = (x - 5, y - 5)
    draw.rectangle(
        [background_position, (background_position[0] + background_size[0], background_position[1] + background_size[1])],
        fill="white"
    )
    draw.text((x, y), text, font=font, fill="black")
    
    return img

def main():
    input_file = 'your_binary_file.bin'  # Replace with your binary file path
    output_directory = 'qr_codes'
    max_chunk_size = 1000  # Adjust based on QR code capacity and error correction level
    
    print("Reading the binary file...")
    binary_data = read_binary_file(input_file)
    
    print("Encoding data to Base64...")
    base64_data = encode_data_to_base64(binary_data)
    
    print("Chunking Base64 data...")
    chunks = chunk_base64_data(base64_data, max_chunk_size)
    total_chunks = len(chunks)
    print(f"Total chunks created: {total_chunks}")
    
    print("Generating QR codes...")
    generate_qr_codes(chunks, output_directory)
    print("All QR codes have been generated successfully!")

if __name__ == '__main__':
    main()
