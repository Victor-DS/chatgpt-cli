from typing import List
from openai import OpenAI
from openai.types.chat.chat_completion import Choice
import typer

app = typer.Typer()
client = OpenAI()


@app.command()
def query(question: str):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "You are a general-knowledge assistant that replies to question in a concise way."},
            {"role": "user", "content": question}
        ]
    )

    print(completion.choices[0].message.content)


@app.command()
def code(question: str):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "You are a coding assistant that gives detailed answers to coding and technical questions, "
                        "and provides a coding example whenever possible."},
            {"role": "user", "content": question}
        ]
    )

    print(completion.choices[0].message.content)


if __name__ == '__main__':
    app()
