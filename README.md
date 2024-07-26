## Elaboration of a Gastronomic Content Creator APP

Welcome to the creation of my application where the AI can generate quality content on culinary topics, getting a complete and detailed information about the elaboration of a recipe has been one of the main reasons to create this APP.

To develop the PPP ‘Gastronomy Content Creator’ we started by doing the following:

# GASTRONOMIC CONTENT CREATOR
## 1-Getting account credentials:

- Have a Groq account:
You can register here:
https://groq.com/

![modelo Grog](https://github.com/user-attachments/assets/8e8c38ca-299a-4b40-ac4d-85bca5f945a7)

- Get Groq API key:
Once we are in Groq Cloud we must obtain its API Key, copy it and save it to place it later in Dify.

- Having a Dify account:
You can create your Dify account here:
 https://dify.ai/

![crear cuenta en dify](https://github.com/user-attachments/assets/9cc4073b-7021-4ccc-ac84-47df2aa5d33c)

## 2-Dify assistant config:

- Add Groq as Model Provider:
Once you have your Dify account, look for the user area in the top right corner, there click on settings..

![usuario dify](https://github.com/user-attachments/assets/9f63b2d8-0e77-44ef-b316-3583f99fb660)

After clicking on configuration you will see the Model Provider option, and click on it..

![model provider](https://github.com/user-attachments/assets/7e578f5e-fbed-4a9b-8844-a16fb9282101)

As you can see there are several models available, we will look for the GroqCloud model, choose that one and then proceed to paste the APIKey we had previously copied and saved..

- Crear asistente (completion):
Inside Dify we can see a section at the top called Studio, click on it and it will show us the option to create an app, we will choose the o
ption to create a blank app..

![crear en blanco1](https://github.com/user-attachments/assets/65c9bf4a-b313-4695-ad10-6bdbd49c4465)

Dify shows more options to continue creating, we will choose the text generator option for the type of app we are making, name the project and hit the create button.

![crear en blanco verdadero](https://github.com/user-attachments/assets/a26ae8ae-8880-4c27-9ec1-2853861d007e)

- Configure Prompt:
We can see an empty structure where we are going to place the prompt, this section is called Prefix Promp and it is the system role, the prompt can be found in the file  https://github.com/ileamarq/GastronomicContentCreator/blob/main/Prompt%20Dify.txt‘  located in the repository, copy and paste it in Prefix Promp.

![Screenshot (44)](https://github.com/user-attachments/assets/9a2dbb08-d463-4a8c-b25c-e60b971ee06a)

- Choose Groq as a model:
We use groq's llama3-8b-8192, because the prompt has been optimised to work with this model.
- Configure input variables:

We choose the variable that we will use (text), you must choose in the field that says variable 
- Save settings.
  
##  3-Get Dify APP key:

- Access the Dify API Key
Dify has in its upper left side a section called Orchestrate, there we will see a window with several options, we are interested in the option that says API Access, by clicking there we can see the documentation of the API Key that Dify offers us.

![orchestatre](https://github.com/user-attachments/assets/0c20fab1-d519-4440-829a-c3abb27c653d)

To copy the Dify APIKey we go to the top right, there we get a button that says API Key, and it is easy to locate because it has the drawing of a key.

![APIKey](https://github.com/user-attachments/assets/fc7ebf47-7d03-498f-97a4-6924bc89aa5f)

We copy this key for later use in the Replit environment.

## 4-Deploy:

### Using replit virtual environment:

- Fork the project on replit:
http://replit.com/@ileartmq/GastronomicContentCreator

- Config Dify Secret Key on Replit:
In Replit look for the Tools panel and select Secrets , here you can paste the Dify APIKey and name it ‘Dify_APP_SECRET’, this will pass the authentication credentials securely without exposing them directly in the code.

![secrets settings replit](https://github.com/user-attachments/assets/758419d0-0f73-4e47-bdc8-ba4c1008bbb6)

Secrets are accessed in your code as an environment variable
 
my_sectret = os.environ[‘Dify_APP_SECRET’]
 
![secret DIFY_APP_SECRET](https://github.com/user-attachments/assets/09b3c894-0702-4164-ab04-32be5bbc9831)

- Run application:
The Run property is used to run your code and start your project in the browser by displaying it in the console. In Shell the command is executed to be able to see the App in the browser and to be able to interact with it.

streamlit run main.py

- Test the application:
  
![replit interfaz](https://github.com/user-attachments/assets/4f6b9dfd-2d7c-4465-aefd-8c9ee45028e7)

Test the App by typing the title of a recipe in the browser 

### Using Streamlit Cloud:

- Fork this github repository 

https://github.com/ileamarq/GastronomicContentCreator

- Go to streamlit cloud:
Login with Github, on the top right hand side click on Create App

![crear app streamlit](https://github.com/user-attachments/assets/551eb10f-edac-46d7-a884-24075da6ea97)

- Select assistant repository to deploy:
- We choose the option that we already have an APP created, then we select the repository of the APP we are going to deploy.
  
 ![streamlit3](https://github.com/user-attachments/assets/8cb8425e-44e6-4759-9983-4864ed85c647)
  
- Config Dify Secret Key.
Streamlit Cloud shows us all the applications we have created, and we must choose the APP we want to deploy, we look for the three dots that are located on the right side of the name of the App, and we click on the configuration option.

![streamlit2](https://github.com/user-attachments/assets/8be38e69-302d-4166-986b-3ccd8a559c24)

A window will open where we will choose the option of Secrets, and it is there where we will place the ‘Dify_APP_SECRET’, we can see how it is obtained in step 3 (Get Dify APP key), finally we click on save.

![API Key Secret Streamlit](https://github.com/user-attachments/assets/7ae472b1-1a75-491d-bf94-81431aec7d5a)

Deploy the app.
Test the app.

![como se ve la aplicacion](https://github.com/user-attachments/assets/613487b3-9416-4faa-b68b-78ac8d23cf67)

![Screenshot (45)](https://github.com/user-attachments/assets/d16b482a-72b8-4bfc-a8c7-6b2afbdbac2d)


