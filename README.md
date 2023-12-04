# QR Code Generator

This Python script generates a QR code for the input string and saves it to a file using the `qrcode` library. Before running the script, make sure to install the library by using `pip install qrcode[pil]`.

## Usage Instructions:

1. **Install Dependencies:**
    ```bash
    pip install "qrcode[pil]"
    ```

2. **Run the Script:**
    ```bash
    python qr_code_generator.py
    ```

3. **Input:**
   - Enter the string for which you want to generate the QR code when prompted.

4. **Result:**
   The script will generate a QR code and save it as "qrcode.png" in the same directory.


## Dependencies:
__qrcode__: A Python library for creating QR codes.

## Example:

**Input:**
```plaintext
Enter the string for QR code generation: Hello, QR Code!
```

**Result:**
```plaintext
QR code generated successfully. Saved as 'qrcode.png'.
```
