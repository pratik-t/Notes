import os
import img2pdf

input_dir = "D:\Study\LATEX\Figures"
output_dir = "D:\Study\LATEX\Figures\\test"

# Set the compression options
options = {
    "jpegopt": {
        "quality": 20,  # Adjust the quality value (0-100)
        "optimize": True,  # Enable optimization
        "progressive": True  # Use progressive (interlaced) encoding
    }
}

# Iterate over JPEG files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name.replace(".jpg", ".pdf").replace(".jpeg", ".pdf"))

        # Convert the JPEG image to PDF with compression options
        with open(output_path, "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(input_path, options=options))

print("JPEG to PDF conversion completed for all files in the directory.")
import os

directory = "D:\Study\LATEX\Figures\\test"

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith("_compressed.pdf"):
        original_path = os.path.join(directory, filename)
        new_filename = filename.replace("_compressed", "")
        new_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(original_path, new_path)

print("File renaming completed for all '_compressed' files in the directory.")
