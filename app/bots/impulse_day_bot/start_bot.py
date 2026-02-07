import os
import time
from dotenv import load_dotenv


load_dotenv()


def main():
    print(os.getenv("TBANK_TOKEN"))
    print(os.getenv("DB_HOST"))
    print("Starting Impulse Day Bot...")


if __name__ == "__main__":
    main()
    time.sleep(1000)
