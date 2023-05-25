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



 







