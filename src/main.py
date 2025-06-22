from client_llm import generate


def main():
    context = []

    while True:
        user_input = input("\nPosez votre question, nous serons ravi de vous aider :\n> ")
        print()
        context = generate(user_input, context)

if __name__ == "__main__":
    main()
