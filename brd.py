import openai

# Set up OpenAI API credentials
openai.api_key = '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'

def generate_brd(prompt):
    # Generate BRD using OpenAI GPT-3
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

    # Extract the generated BRD from the API response
    brd = response.choices[0].text.strip()

    return brd

# Prompt input from the user
prompt = input("Enter the prompt: ")

# Generate the BRD
brd = generate_brd(prompt)

# Print the generated BRD
print(brd)
