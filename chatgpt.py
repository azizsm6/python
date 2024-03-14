import openai

def generate_text():
    # Set your API key here
    openai.api_key = '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'

    # Prompt for generating text
    prompt = input("Enter the prompt: ")

    # Generate text using GPT-3
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Name of the engine used
        prompt=prompt,
        max_tokens=100  # Number of words to generate
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    # Return the generated text
    return generated_text


# Call the function to generate text
generated_text = generate_text()

# Display the generated text
print("Here is the text that was generated:")
print(generated_text)