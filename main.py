import mood_responses

def main():
    try:
        name = input("What's your name? ")
        greeting = "Hello good looking"
        print(f"{greeting}, {name}! How are you feeling today?")
        mood = input()
        print(mood_responses.mood_response(mood))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

