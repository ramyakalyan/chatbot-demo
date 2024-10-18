{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8323bb4f-39b4-42fc-9379-587ccdbf71b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot is ready! Type 'exit' or 'quit' to end the conversation.\n"
     ]
    }
   ],
   "source": [
    "import openai\n",
    "import os\n",
    "\n",
    "# Set your OpenAI API key\n",
    "openai.api_key = os.getenv('OPENAI_API_KEY') # Make sure to set this environment variable\n",
    "\n",
    "# Check if the API key is set correctly\n",
    "if not openai.api_key:\n",
    "    raise ValueError(\"The API key is not set. Please set the OPENAI_API_KEY environment variable.\")\n",
    "\n",
    "# Initialize the conversation history\n",
    "conversation_history = [\n",
    "    {\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}\n",
    "]\n",
    "\n",
    "def chat_with_openai(prompt):\n",
    "    # Add the user's message to the conversation history\n",
    "    conversation_history.append({\"role\": \"user\", \"content\": prompt})\n",
    "    \n",
    "    try:\n",
    "        # Generate a response using the OpenAI API\n",
    "        response = openai.ChatCompletion.create(\n",
    "            model=\"gpt-3.5-turbo\",\n",
    "            messages=conversation_history\n",
    "        )\n",
    "        # Extract the assistant's message from the response\n",
    "        answer = response.choices[0].message['content'].strip()\n",
    "        # Add the assistant's message to the conversation history\n",
    "        conversation_history.append({\"role\": \"assistant\", \"content\": answer})\n",
    "        return answer\n",
    "    except Exception as e:\n",
    "        return f\"An error occurred: {e}\"\n",
    "\n",
    "# Main loop for the chatbot\n",
    "print(\"Chatbot is ready! Type 'exit' or 'quit' to end the conversation.\")\n",
    "while True:\n",
    "    # Get the user's input\n",
    "    user_input = input(\"You: \")\n",
    "    # Exit the loop if the user wants to quit\n",
    "    if user_input.lower() in [\"exit\", \"quit\"]:\n",
    "        print(\"Goodbye!\")\n",
    "        break\n",
    "    # Get the chatbot's response\n",
    "    response = chat_with_openai(user_input)\n",
    "    # Print the chatbot's response\n",
    "    print(f\"Assistant: {response}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa7ebfe5-de35-43a8-99dd-388ef55f1cd2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
