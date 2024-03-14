import openai

openai.api_key = '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'

def generate_brd(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    brd = response.choices[0].text.strip()

    return brd

prompt = input("Enter the prompt: ")

brd = generate_brd(prompt)

print(brd)
