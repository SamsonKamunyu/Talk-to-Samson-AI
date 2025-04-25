{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "adabcb68-f647-407b-b185-0403b84d0e9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# model/chat_engine.py\n",
    "import openai\n",
    "\n",
    "# Load persona prompt\n",
    "with open(r\"C:\\Users\\25471\\Documents\\Python\\Samson_AI\\Talk-to-Samson-AI\\Prompts\\persona_prompt.txt\", encoding='utf-8') as f:\n",
    "    persona_prompt = f.read()\n",
    "\n",
    "def get_response(user_input):\n",
    "    messages = [\n",
    "        {\"role\": \"system\", \"content\": persona_prompt},\n",
    "        {\"role\": \"user\", \"content\": user_input}\n",
    "    ]\n",
    "    \n",
    "    response = openai.ChatCompletion.create(\n",
    "        model=\"gpt-4\",\n",
    "        messages=messages,\n",
    "        temperature=0.7\n",
    "    )\n",
    "    return response['choices'][0]['message']['content']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c48c6d23-0638-4ced-89b0-7a751a2bd7db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
