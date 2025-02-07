import os
from pyzbar import pyzbar
from PIL import Image
import base64
import re

def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = pyzbar.decode(img)
    if decoded_objects:
        qr_data = decoded_objects[0].data.decode('ascii')
        return qr_data
    else:
        print(f"Warning: No QR code found in {image_path}")
        return None

def parse_qr_data(qr_data):
    # Expected format: 'chunk_number/total_chunks:chunk_data'
    match = re.match(r'^(\d+)/(\d+):(.*)$', qr_data, re.DOTALL)
    if match:
        chunk_number = int(match.group(1))
        total_chunks = int(match.group(2))
        chunk_data = match.group(3)
        return chunk_number, total_chunks, chunk_data
    else:
        print("Warning: QR data format is incorrect.")
        return None, None, None

def reconstruct_base64_data(chunks, total_chunks):
    base64_data = ''
    for i in range(1, total_chunks + 1):
        if i in chunks:
            base64_data += chunks[i]
        else:
            print(f"Warning: Missing chunk {i}.")
            return None
    return base64_data

def decode_base64_to_binary(base64_data):
    return base64.b64decode(base64_data)

def main():
    input_directory = 'qr_codes'  # Directory with QR code images
    output_file = 'reconstructed_file.bin'  # Output binary file
    
    print("Starting reconstruction process...")
    
    chunks = {}
    total_chunks = None
    files = [f for f in os.listdir(input_directory) if f.endswith('.png')]
    files.sort()  # Ensure files are processed in order if named sequentially
    
    for file_name in files:
        image_path = os.path.join(input_directory, file_name)
        print(f"Decoding {file_name}...")
        
        qr_data = decode_qr_code(image_path)
        if qr_data:
            chunk_number, total_chunks_from_data, chunk_data = parse_qr_data(qr_data)
            if chunk_number is not None:
                chunks[chunk_number] = chunk_data
                if total_chunks is None:
                    total_chunks = total_chunks_from_data
                elif total_chunks != total_chunks_from_data:
                    print("Warning: Inconsistent total chunks detected.")
    
    if total_chunks is None:
        print("Error: No valid chunks found.")
        return
    
    print("Reassembling Base64 data...")
    base64_data = reconstruct_base64_data(chunks, total_chunks)
    if base64_data is None:
        print("Error: Reconstruction failed due to missing chunks.")
        return
    
    print("Decoding Base64 data to binary...")
    binary_data = decode_base64_to_binary(base64_data)
    
    print(f"Writing binary data to {output_file}...")
    with open(output_file, 'wb') as f:
        f.write(binary_data)
    
    print("File reconstruction complete!")

if __name__ == '__main__':
    main()
