# MLAI
ML &amp; AI Azure


A cloud computing platform provided by Microsoft, to extract 
data from PDF files and generate JSON output. Azure likely offers 
services or tools that enable them to process PDF documents and extract 
relevant information in a structured format, such as JSON. This approach 
can be useful for automating data extraction and analysis from PDF files, 
which are commonly used for storing textual and graphical information.

# Create an Azure account

Go to the Azure portal website at https://portal.azure.com.

Click on the "Start free" or "Create account" button on the homepage.

Once your account is created, you will be redirected to the Azure portal, 
where you can start exploring and using various Azure services.

<img width = "500" src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/azure14.png">



# Create storage account

Now, we have to create storage account to store trained data.

<img width= "500" src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/azure2.png">


# Form Recognizer

Form Recognizer helps automate the process of extracting key information 
from forms and documents. Instead of manually reading and inputting data,
you can use Form Recognizer to extract data fields such as names, addresses,
dates, invoice numbers, and more. This can save time, reduce errors, and improve
efficiency in various business processes.

<img width= "500" src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/azure3.png">

Create your form recognizer

Open your form recognizer and click on form recognizer studio(click on try it)

<img width = "500" src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/azure4.png">

open custom models 

Train custom models to classify documents and extract text, structure and fields from your forms or documents.

<img width = "500" src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/azure5.png">

You need to create your project 

Upload minimum 5 pdf files from your local device and click on "Run Layout" for analyze.

To "Train" your pdfs you have to do label your pdfs, for labeling clik on "Draw Region".

<img width = "500" src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/azure6.png">

Model has been created

Open model -> Click on test -> Upload pdfs --> Run Analyze 

You can see your output in "Result".

<img width = "500" src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/azure7.png">

Now download result --> import in database

# processing files in the loop with Azure document recognizer

# Installation

1. Clone the repository:

     git clone https://github.com/vivifyhealthcare/Document-OCR-Azure.git

2. Install the required dependencies:

     pip install azure-core

     pip install azure-ai-formrecognizer

     pip install pymongo

     pip install azure-storage-blob


## How to uplaod pdf to blob container

First, do the 'git clone'. Now select ``UploadPdfs_Azure.py``then open PyCharm or Visual Studio and Save the file.

Give the Azure Account details in the code.

Give the Storage_Account_name:
 - Open the Azure Account and click on the "Storage Account"(Please refer to the below image for reference)

  <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Azure+image6.png">


Give the Account_key:
 - Open the Azure Account Click on the "Storage Account" and then click on the Bucket(you Already created a Bucket name) scroll down to see the "Security + networking" tab is showing. Inside the Access keys button is there, click on it. (Please refer to the below image for reference)

      <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Azure+image7.png">


Give the container_name :
 - Open the Azure Account click on the storage Account, and then click on "your Bucket" The Data storage folder is there see the down Containers tab and click on it. container names will show (Please refer to the below image for reference).

   <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Azure+image4.png">

Save the Python file. Run the code using the "Run" button or relevant shortcut (ex: python your filename). Check the Output

   <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/azure+image8.png">

Now you can select the pdfs.

<img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Azure+image9.png">


## Get All the pdf urls from the blob container

Now select ``Azure_geturls.py`` and then open PyCharm or Visual Studio. Save the file.

Give the Azure Account details in the code:
 
Give the connection_string :
 - Open the Azure Account click on the "Storage Account" click the Bucket see the left side  "Security + networking" tab is inside Click the Access keys there is the Connection string choose the one that is it. (Please refer to the below image for reference)

   <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Azure+image3.png">

Give the container_name :
 - Open the Azure Account click on the storage Account and then click the "your Bucket" Data storage folder is there see put the down Containers tab is click on it container names will come.(Please refer to the below image for reference)

   <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Azure+image4.png">


Save the Python file. Run the code using the "Run" button or relevant shortcut (ex: python your filename) check the Output.
Verify the console for any generated output. Verify "blob_urls.txt".(Please refer to the below image for reference)

 <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+2023-11-16+123707.png"> 

Click on the "blob_urls.txt" then you will get the urls.(Please refer to the below image for reference).

  <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+2023-11-16+170815.png">



## How to train the pdf urls and how to stored in database

Now select ``Azure_database.py`` and then open PyCharm or Visual Studio. Save the file

Give the Azure Account details in code:

Give the Keys And Endpoint : 

  - Open the Azure Account and click on Document Intelligence. Click on the AI services you created. "Resource Management" is showing on the left side and below that "Key and Endpoint" folder is showing click on it. "Key and Endpoint" will be shown, the first is the key and the last is the endpoint (please refer to the following image for reference).  

  <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/azure+image.png">


Give the model_id
  - Open the Azure account and click on "Document Intelligence". Click on the AI services you created. Scroll down and click on "Document Intelligence Studio", there is a "Try it" option click on it. Scroll down "Custom Models" will be shown and within it the "Custom Extraction Model" will be shown click on it. Scrolling down will show your project name then click on it. Click on the left side "Models" and model ID will show (please refer to the following image for reference).

   <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/azure+image2.png">

Save the Python file. Run the code using the "Run" button or relevant shortcut (ex: python your filename) check the Output. (please refer to the following image for reference).

  <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+2023-11-20+113310.png">

When you run the code, every PDF trained data will be sent to the MongoDB database  (please refer to the following image for reference).

  <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+2023-11-20+112148.png">

MongoDB database shows the saved deta  (please refer to the following image for reference).

  <img width="500" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+2023-11-16+125224.png">



<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>



 







