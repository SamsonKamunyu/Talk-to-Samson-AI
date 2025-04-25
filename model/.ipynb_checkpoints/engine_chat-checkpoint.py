{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6f56f6d6-aa77-41e0-a63d-b93a1ed8c3ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# model/engine_chat.py\n",
    "import openai\n",
    "import os\n",
    "\n",
    "# Load the persona prompt from file\n",
    "with open(r\"C:\\Users\\25471\\Documents\\Python\\Samson_AI\\Talk-to-Samson-AI\\Prompts\\persona_prompt.txt\", encoding='utf-8') as f:\n",
    "    persona_prompt = f.read()\n",
    "\n",
    "def get_response(user_input):\n",
    "    messages = [\n",
    "        {\"role\": \"system\", \"content\": persona_prompt},\n",
    "        {\"role\": \"user\", \"content\": user_input}\n",
    "    ]\n",
    "\n",
    "    try:\n",
    "        response = openai.ChatCompletion.create(\n",
    "            model=\"gpt-4\",\n",
    "            messages=messages,\n",
    "            temperature=0.7\n",
    "        )\n",
    "        return response['choices'][0]['message']['content']\n",
    "    \n",
    "    except Exception as e:\n",
    "        return f\"Something went wrong: {str(e)}\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a7e88b02-d77b-45b2-98e9-d160051a0027",
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
