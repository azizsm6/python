import openai

def generate_text():
    
    openai.api_key = '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'

    
    prompt = input("Enter the prompt: ")

    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Name of the engine used
        prompt=prompt,
        max_tokens=100  # Number of words to generate
    )

    generated_text = response.choices[0].text.strip()

    return generated_text


generated_text = generate_text()

print("Here is the text that was generated:")
print(generated_text)
