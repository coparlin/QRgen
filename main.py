import qrcode

def generate_qr_code(input_string, file_name='qrcode.png'):
    """
    Generate a QR code for the input string and save it to a file.

    Parameters:
    - input_string (str): The string for which to generate the QR code.
    - file_name (str): The name of the file to save the QR code image.

    Returns:
    - str: Message indicating the success of QR code generation.
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(input_string)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)

    return f"QR code generated successfully. Saved as '{file_name}'."

if __name__ == "__main__":
    # Example usage
    user_input = input("Enter the string for QR code generation: ")
    result_message = generate_qr_code(user_input)
    print(result_message)
