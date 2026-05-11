from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access variables
api_key = os.getenv('GROK_API_KEY')
print(f'Your API key is: {api_key}')

print('✅ .env loaded successfully!')