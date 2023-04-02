# GPTVoice

GPTVoice is a simple voice assistant built with Python that uses the GPT language model to process voice commands. With GPTVoice, you can easily convert your speech to text and execute commands by simply speaking into your microphone.

## Installation

To install GPTVoice, first make sure that you have Python 3.x installed on your system. Then, follow these steps:

1. Clone or download the repository to your local machine.
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Set up your API keys for the Google Cloud Speech-to-Text API and the OpenAI GPT model by following the instructions in the `API Keys` section below.

## API Keys

Before running GPTVoice, you will need to obtain two API keys: one for the Google Cloud Speech-to-Text API and another for the OpenAI GPT model. Follow the instructions below to obtain these keys:

### Google Cloud Speech-to-Text API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project from the dropdown menu at the top of the page.
3. In the left sidebar, click on "APIs & Services" > "Credentials".
4. Click the "Create Credentials" button and select "Service Account Key".
5. Choose "JSON" as the key type, and click "Create".
6. Save the resulting API key file to your computer.
7. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your API key file. You can do this by running the following command in your terminal, replacing `/path/to/your/api_key.json` with the path to your API key file:




### OpenAI GPT API Key

1. Go to the [OpenAI API page](https://beta.openai.com/docs/api-reference).
2. Create an account if you haven't already, and log in.
3. Navigate to the "API Keys" tab.
4. Copy your API key to your clipboard.
5. Create a new file called `gpt.txt` inside the `api` directory of your GPTVoice project.
6. Paste your API key into the `gpt.txt` file and save it.

## Usage

To run GPTVoice, simply execute the `main.py` script using Python:


