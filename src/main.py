from openai import OpenAI
from config import settings
from prompts import SYSTEM_PROMPT


def main():
    client = OpenAI(api_key=settings.openai_api_key)

    print("Personlig assistent v0.1")
    print("Modell:", settings.openai_model)
    print("Skriv något (eller 'exit'):")

    history = []

    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Avslutar.")
            break

        history.append({"role": "user", "content": user_input})

        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

        completion = client.chat.completions.create(
            model=settings.openai_model,
            messages=messages,
            temperature=0.5,
            max_tokens=400,
        )

        reply = completion.choices[0].message.content
        print("\nAI:", reply, "\n")

        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()