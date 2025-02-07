# backup2qr

# QR Code File Backup Utility

A Python utility to **encode any file—text or binary—into a series of QR codes** and decode them back into the original file. This tool lets you create a **physical, printable backup** of important files, providing a tangible safeguard in case digital storage fails.

## Table of Contents

- [Motivation](#motivation)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Encoding Files to QR Codes](#encoding-files-to-qr-codes)
  - [Decoding QR Codes to Files](#decoding-qr-codes-to-files)
- [Examples](#examples)
- [Limitations and Considerations](#limitations-and-considerations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Motivation

In our digital age, it's easy to forget how fragile electronic storage can be. Hard drives fail, servers crash, and sometimes the unthinkable happens—a total system meltdown. This project was born from the idea of having a **last-resort, physical backup**: turning your essential files into QR codes that you can print and store securely. It's like creating a modern-day Rosetta Stone for your data—a way to piece everything back together if everything goes under.

By transforming your files into printable QR codes, you're not just backing up data; you're preserving it in a form that transcends the digital realm. It's a safeguard against the vulnerabilities of electronic storage, ensuring that even if all else fails, you have a tangible copy to fall back on.

---

## Features

- **Supports All File Types**: From text documents to images, videos, and executables.
- **Safe Binary Encoding**: Uses Base64 to encode binary data for reliable QR code storage.
- **Customizable Chunk Sizes**: Adjust data chunk sizes to optimize QR code capacity and error correction levels.
- **High Error Correction**: Employs robust error correction to ensure data integrity, even if QR codes are partially damaged.
- **Visual Chunk Indicators**: Overlays chunk numbers on QR codes for easy identification and assembly.
- **Complete Reconstruction**: Decode and reconstruct your original file seamlessly from the QR codes.

---

## Getting Started

### Prerequisites

- **Python 3.6+**
- Python Libraries:
  - `qrcode`
  - `Pillow` (PIL)
  - `pyzbar`
- **System Dependencies**:
  - **zbar** library (required by `pyzbar` for QR code decoding)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/qr-code-file-backup.git
   cd qr-code-file-backup
   ```

2. **Install Python Dependencies**

```bash
pip install qrcode Pillow pyzbar
Install zbar Library
```

For Debian/Ubuntu

```bash
sudo apt-get install libzbar0
For macOS
```

```bash
brew install zbar
For Windows
```

**Download and install the Windows binaries for zbar from the official repository.**

## Usage

### Encoding Files to QR Codes

1. Prepare Your File

Place the file you wish to back up in the project directory or note its absolute path.

2. Run the Encoding Script

```bash
python encode_file_to_qr.py -i path/to/yourfile.ext -o qr_codes -s 1000

Arguments:

-i, --input: Path to your input file.
-o, --output: Directory to save QR code images (default is qr_codes).
-s, --chunk_size: Maximum size (in characters) of each data chunk. Adjust based on QR code capacity and error correction level.
```

3. Result
The script will generate a series of QR code images in the specified output directory.
Each QR code image will have the chunk number overlaid at the center for easy identification.

4. Print the QR Codes (Optional)
For a physical backup, print the QR code images using a high-resolution printer to ensure scannability.

### Decoding QR Codes to Files

1. Gather QR Code Images
Collect all the QR code images into a single directory. If you've printed and scanned them, ensure the scanned images are clear and properly cropped.

2. Run the Decoding Script
```bash
python decode_qr_to_file.py -i qr_codes -o reconstructed_file.ext

Arguments:
-i, --input: Directory containing the QR code images.
-o, --output: Path and name for the reconstructed output file.
```

3. Result
The script will decode the QR codes, reconstruct the original file, and save it to the specified output path.

4. Verify Integrity
It's recommended to compare the original and reconstructed files using checksums (e.g., MD5 or SHA256) to ensure data integrity.

### Examples

Example 1: Backing Up a Source Code File

**Encoding**

```bash
python encode_file_to_qr.py -i my_script.py -o qr_codes/my_script -s 800
```

Encodes my_script.py into QR codes saved in qr_codes/my_script, with each chunk being up to 800 characters.

**Decoding**

```bash
python decode_qr_to_file.py -i qr_codes/my_script -o restored_script.py
```

Reconstructs the original script from the QR codes and saves it as restored_script.py.

Example 2: Creating a Physical Backup of a PDF Document
Encoding

```bash
python encode_file_to_qr.py -i important_document.pdf -o qr_codes/document_backup -s 1000
```

### Printing

Print the QR codes from qr_codes/document_backup on high-quality paper.

**Decoding**

Scan the printed QR codes and save the images to qr_codes/scanned_backup.

```bash
python decode_qr_to_file.py -i qr_codes/scanned_backup -o restored_document.pdf
```

### Limitations and Considerations

  - Data Capacity per QR Code: The amount of data each QR code can hold is limited and depends on the error correction level and the complexity of the data.
  - Higher error correction levels reduce capacity but improve reliability.
  - Base64 encoding increases data size by approximately 33%.
  - Quality of QR Codes:
    - Printing: Use high-resolution printers to produce clear QR codes.
    - Scanning: Use a good scanner or camera to capture the QR codes without distortion.
  - Storage and Handling:
    - Physical QR codes are susceptible to damage from environmental factors.
    - Store printed QR codes in a safe, dry place away from direct sunlight.
  - Security:
    - Physical backups can be lost, stolen, or viewed by unauthorized individuals.
    - Consider encrypting sensitive data before encoding.

### Future Enhancements

  - **Data Compression:**
    - Implement optional compression (e.g., using zlib) to reduce the number of QR codes needed.
  - **Encryption Support:**
    - Add features to encrypt data before encoding to protect sensitive information.
  - **Checksum Verification:**
    - Include checksums for each chunk to verify integrity during decoding.
  - **Error Correction Coding:**
    - Implement additional error correction at the data level for improved resilience.
  - **Graphical User Interface (GUI):**
    - Develop a user-friendly interface to simplify usage for non-technical users.

### Contributing
Contributions are welcome! Here's how you can help:

  - Fork the Repository
    - Click the "Fork" button at the top-right corner of the repository page.
  - Clone Your Fork

```bash
git clone https://github.com/yourusername/qr-code-file-backup.git
cd qr-code-file-backup
```

  - Create a New Branch

```bash
git checkout -b feature/your_feature
Make Your Changes
```

  - Add your features or fix bugs.
  - Commit and Push

```bash
git add .
git commit -m "Add your message here"
git push origin feature/your_feature
```

  - Go to the original repository and click "New Pull Request."

### License

This project is licensed under the MIT License—see the LICENSE file for details.
   
