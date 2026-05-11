from dotenv import load_dotenv
import os

# Load everything from your .env file
load_dotenv()

# Test it — this should print your exact message!
print("✅ Dotenv is working perfectly!")
print("TEST_MESSAGE =", os.getenv("TEST_MESSAGE"))