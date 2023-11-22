from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from collections import OrderedDict
from pymongo import MongoClient
import sys


# Set the default encoding to utf-8
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

endpoint = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
key = "xxxxxxxxxxxxxxxxxxxxxx"


model_id = "xxxxxxxxxx"

# Read form URLs from a text file
with open("blob_urls.txt", "r") as file:
    formUrls = file.read().splitlines()

# Create the Document Analysis client
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['Different_voters2']  # Replace 'Different_voters' with your desired database name

# Counter for completed, pending, and total documents
initial_completed_count = 0
initial_pending_count = len(formUrls)
total_documents = len(formUrls)

# Display initial counts
print("\nInitial Counts - Completed Documents: {}, Pending Documents: {}, Total Documents: {}".format(initial_completed_count, initial_pending_count, total_documents))

# Iterate through the list of form URLs
for idx, formUrl in enumerate(formUrls, start=1):
    # Extract the form name from the URL
    form_name = formUrl.split("/")[-1].split(".")[0]

    # Create a collection name based on the form name
    collection_name = "Azure_voter_details_" + form_name
    collection = db[collection_name]

    # Begin analyzing the document using the custom model
    poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
    result = poller.result()

    # Create an ordered dictionary to store the fields and their values in order
    fields_output = OrderedDict()

    for document in result.documents:
        print("--------Analyzing document #{}--------".format(idx))
        print("Document has type {}".format(document.doc_type))
        print("Document has confidence {}".format(document.confidence))
        print("Document was analyzed by model with ID {}".format(result.model_id))

        # Extracting and storing fields in the fields_output dictionary
        for name, field in document.fields.items():
            if field.value:
                field_value = field.value
            else:
                field_value = field.content

            print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence))

            fields_output[name] = field_value

    # Insert the fields_output dictionary into the dynamically named collection
    collection.insert_one(fields_output)

    # Increment counters based on document status
    if poller.status() == "succeeded":
        initial_completed_count += 1
        initial_pending_count -= 1

    # Print the fields output in order
    print("\nFields Output (Order Wise) for {}: ".format(form_name))
    for key, value in fields_output.items():
        print("{}: {}".format(key, value))

    # Display current completed, pending, and total counts after processing each document
    print("\nCurrent Counts - Completed Documents: {}, Pending Documents: {}, Total Documents: {}".format(initial_completed_count, initial_pending_count, total_documents))

# Close the MongoDB connection
mongo_client.close()