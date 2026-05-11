from dotenv import load_dotenv
from loguru import logger
from rich.console import Console
from openai import OpenAI
import os

load_dotenv()

console = Console()
logger.add("logs/agent.log", rotation="10 MB", level="INFO")

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def main():
    console.print("Grok Agent is live!")
    console.print("Talk to me naturally.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in :
                console.print("Goodbye!")
                break
                
            console.print("Agent is thinking...")
            
            response = client.chat.completions.create(
                model="grok-beta",
                messages=[
                    {"role": "system", "content": "You are a helpful and truthful assistant."},
                    {"role": "user", "content": user_input} 0].message.content
            console.print(f"Agent: {reply}\n")
            
        except Exception as e:
            console.print("Something went wrong.")
            logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
