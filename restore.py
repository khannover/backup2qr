import os
from pyzbar import pyzbar
from PIL import Image
import re

def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = pyzbar.decode(img)
    if decoded_objects:
        data = decoded_objects[0].data.decode('utf-8')
        return data
    else:
        print(f"Warning: No QR code found in {image_path}")
        return None

def extract_chunk_number(file_name):
    # Assumes file name is like 'chunk_001.png'
    match = re.search(r'chunk_(\d+)', file_name)
    if match:
        return int(match.group(1))
    else:
        print(f"Warning: Could not extract chunk number from {file_name}")
        return None

def reconstruct_source_code(qr_codes_dir, output_file):
    chunks = {}
    total_chunks = 0

    # Scan the directory for QR code images
    for file_name in os.listdir(qr_codes_dir):
        if file_name.endswith('.png'):
            file_path = os.path.join(qr_codes_dir, file_name)
            print(f"Decoding {file_name}...")
            data = decode_qr_code(file_path)
            if data:
                # Extract chunk number from the data or file name
                chunk_number = extract_chunk_number(file_name)
                if chunk_number:
                    chunks[chunk_number] = data
                    total_chunks += 1

    if not chunks:
        print("No chunks were found. Exiting.")
        return

    # Sort chunks based on chunk number
    sorted_chunks = [chunks[i] for i in sorted(chunks.keys())]
    reconstructed_data = ''.join(sorted_chunks)

    # Write the reconstructed data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(reconstructed_data)

    print(f"Reconstruction complete! Source code saved to {output_file}")

def main():
    qr_codes_directory = 'qr_codes'       # Directory containing QR code images
    output_file = 'reconstructed_code.py'  # Destination file for the reconstructed source code

    print("Starting reconstruction process...")
    reconstruct_source_code(qr_codes_directory, output_file)
    print("Process finished.")

if __name__ == '__main__':
    main()
