from azure.storage.blob import BlobServiceClient
from tkinter import Tk, filedialog
import os

# Set your Azure Storage account information
Storage_Account_name = 'xxxxxxxxxxx'
account_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
container_name = 'xxxxx'

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient(account_url=f"https://{Storage_Account_name}.blob.core.windows.net", credential=account_key)

# Create a ContainerClient
container_client = blob_service_client.get_container_client(container_name)

# Create Tkinter root window
root = Tk()
root.withdraw()

# Open file dialog to choose multiple PDF files
pdf_file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])

# Check if the user selected any files
if pdf_file_paths:
    for pdf_file_path in pdf_file_paths:
        # Specify the name of the file in Azure Storage
        pdf_file_name = os.path.basename(pdf_file_path)

        # Create a BlobClient
        blob_client = container_client.get_blob_client(pdf_file_name)

        try:
            # Upload the PDF file to Azure Storage
            with open(pdf_file_path, "rb") as data:
                blob_client.upload_blob(data)

            print(f"File {pdf_file_name} uploaded successfully.")

        except Exception as e:
            print(f"Error uploading {pdf_file_name}: {str(e)}")

    print("All selected files uploaded successfully.")

else:
    print("No files selected. Exiting.")







