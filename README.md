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
