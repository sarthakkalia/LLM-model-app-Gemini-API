# LLM-model-app-Gemini-API
This project leverages the Gemini API to provide advanced AI capabilities. Follow the steps below to set up and run the application.  
## Prerequisites  
* A Gemini API Key
## Setup Instructions  
**1. Generate Gemini API Key**  
&nbsp;&nbsp;&nbsp;&nbsp; Obtain your Gemini API key from the Gemini platform.  
**2. Clone the Repository**  
&nbsp;&nbsp;&nbsp;&nbsp; Clone this repository to your local machine using the following command:  
```sh
git clone https://github.com/sarthakkalia/LLM-model-app-Gemini-API.git
```
**3. Install Dependencies**  
&nbsp;&nbsp;&nbsp;&nbsp; Navigate to the project directory and install the required dependencies:
```
cd LLM-model-app-Gemini-API
pip install -r requirements.txt
```
**4. Configure Environment Variables**  
&nbsp;&nbsp;&nbsp;&nbsp; Create a `.env` file in the project directory and add your Gemini API key: `GOOGLE_API_KEY="*****************"`  

**5. Run the Application**  
* To run the text-only AI application:
  ```
  streamlit run app.py
  ```
* To run the AI application with both image and text capabilities:
   ```
   streamlit run vision.py
   ```
## Contributors:
**Sarthak Kalia**  (https://www.linkedin.com/in/sarthak-kalia-45sk24276/)
