import openai
# Set your OpenAI API key
api_key = &#39;sk-proj-J89Zs4YKmykEE1Mt1w7LT3BlbkFJSyokIKU&#39;
openai.api_key = api_key
# Define the function to interact with GPT-3
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine=&quot;text-davinci-003&quot;,
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text.strip()
# Main function to handle the conversation
def chat():
    print(&quot;Jarvis: Hello! How can I help you?&quot;)
    while True:
        user_input = input(&quot;user: &quot;).strip()
        if user_input.lower() == &quot;exit&quot;:
            print(&quot;Chatbot: Goodbye!&quot;)
            break
        response = ask_gpt(&quot;You: &quot; + user_input + &quot;\nChatbot:&quot;)
        print(&quot;Chatbot:&quot;, response)
# Start the conversation

if __name__ == &quot;__main__&quot;:
    chat()
