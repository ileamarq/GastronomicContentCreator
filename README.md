
# GASTRONOMIC CONTENT CREATOR
## 1-Getting account credentials:

- Have a Groq account:
You can register here:
https://groq.com/
FOTO
- Get Groq API key:
Once we are in Groq Cloud we must obtain its API Key, copy it and save it to place it later in Dify.

- Having a Dify account:
You can create your Dify account here:
 https://dify.ai/
FOTO

## 2-Dify assistant config:
- Add Groq as Model Provider:
Once you have your Dify account, look for the user area in the top right corner, there click on settings..
FOTO
After clicking on configuration you will see the Model Provider option, and click on it..
FOTO
As you can see there are several models available, we will look for the GroqCloud model, choose that one and then proceed to paste the APIKey we had previously copied and saved..

- Crear asistente (completion):
Inside Dify we can see a section at the top called Studio, click on it and it will show us the option to create an app, we will choose the option to create a blank app..
FOTO
Dify shows more options to continue creating, we will choose the text generator option for the type of app we are making, name the project and hit the create button.
FOTO
- Configure Prompt:
We can see an empty structure where we are going to place the prompt, this section is called Prefix Promp and it is the system role, the prompt can be found in the file  https://github.com/ileamarq/GastronomicContentCreator/blob/main/Prompt%20Dify.txt‘  located in the repository, copy and paste it in Prefix Promp.
- Choose Groq as a model:
We use groq's llama3-8b-8192, because the prompt has been optimised to work with this model.
- Configure input variables:
We choose the variable that we will use (text), you must choose in the field that says variable 
- Save settings.
##  3-Get Dify APP key:
- Access the Dify API Key
Dify has in its upper left side a section called Orchestrate, there we will see a window with several options, we are interested in the option that says API Access, by clicking there we can see the documentation of the API Key that Dify offers us.
FOTO
To copy the Dify APIKey we go to the top right, there we get a button that says API Key, and it is easy to locate because it has the drawing of a key.
We copy this key for later use in the Replit environment.

## 4-Deploy:
### Using replit virtual environment:
- Fork the project on replit:
http://replit.com/@ileartmq/GastronomicContentCreator

- Config Dify Secret Key on Replit:
In Replit look for the Tools panel and select Secrets , here you can paste the Dify APIKey and name it ‘Dify_APP_SECRET’, this will pass the authentication credentials securely without exposing them directly in the code.
FOTO
Secrets are accessed in your code as an environment variable
> 
my_sectret = os.environ[‘Dify_APP_SECRET’]

- Run application:
The Run property is used to run your code and start your project in the browser by displaying it in the console. In Shell the command is executed to be able to see the App in the browser and to be able to interact with it.
> 
streamlit run main.py  

- Test the application:
Test the App by typing the title of a recipe in the browser 
### Using Streamlit Cloud:
- Fork this github repository 
https://github.com/ileamarq/GastronomicContentCreator
- Go to streamlit cloud:
Login with Github, on the top right hand side click on Create App
FOTO
- Select assistant repository to deploy:
- We choose the option that we already have an APP created, then we select the repository of the APP we are going to deploy.
       
- Config Dify Secret Key.
Streamlit Cloud shows us all the applications we have created, and we must choose the APP we want to deploy, we look for the three dots that are located on the right side of the name of the App, and we click on the configuration option.
FOTO
A window will open where we will choose the option of Secrets, and it is there where we will place the ‘Dify_APP_SECRET’, we can see how it is obtained in step 3 (Get Dify APP key), finally we click on save.
Deploy the app.
Test the app.

