from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError

# Replace with your Azure Blob Storage connection string
connection_string = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Replace with your container name
container_name = "xxxxx"

# File to save the URLs
output_file_path = "xxxxxxx"

try:
    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)

    # List blobs in the container
    blob_list = container_client.list_blobs()

    # Open the file in write mode
    with open(output_file_path, "w") as output_file:
        for blob in blob_list:
            blob_url = container_client.get_blob_client(blob).url
            output_file.write(blob_url + "\n")

    print(f"Blob URLs saved to {output_file_path}")
except ResourceNotFoundError:
    print(f"Container '{container_name}' not found. Please check the container name.")
except Exception as e:
    print(f"An error occurred: {str(e)}")