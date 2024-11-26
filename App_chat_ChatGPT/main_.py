# Instalar Typer con `pip install --upgrade "typer[all]"`
# rich es una librería para añadir texto rico https://github.com/Textualize/rich ; https://rich.readthedocs.io/en/latest/
import os

import openai
import typer
from dotenv import load_dotenv
from rich import print as rprint
from rich.table import Table

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_ENGINE = "gpt-4o"

# Tabla informativa para mostrar cuando se inicie el programa
table = Table("Comando", "Descripción")
table.add_row("exit", "Salir de la aplicación")
table.add_row("new", "Comenzar una nueva conversación")

client = openai.OpenAI(api_key=OPENAI_API_KEY)
context = {
    "role": "system",
    # Contexto del asistente: le damos un contexto inicial a ChatGPT
    "content": "Eres un asistente..."
}
# Para ir almacenando todo lo que le pasaremos luego a messages en create()
messages = [
    context,
]


def __prompt() -> str:
    """
    Devuelve el prompt o aborta el programa.

    Returns:
        str: La entrada del usuario.

    Raises:
        typer.Abort: Si el usuario confirma que desea salir.
    """
    rprint("[bold blue]\nRealiza tu consulta > [/bold blue]",
           end="")  # Añadimos end vacío para que no se realice salto de línea
    prompt = input()

    if prompt == "exit":
        exit = typer.confirm("🛑 ¿Seguro que quieres cerrar la aplicación?")
        if exit:
            rprint(f"¡Nos vemos! 👋")
            raise typer.Abort()  # En lugar de exit
        return __prompt()

    return prompt


def main():
    """
    Mantiene una conversación con ChatGPT a través de su API.
    """
    global messages
    rprint("[bold green]Conexión con la API de ChatGPT usando Python 🐍\n[/bold green]")
    rprint(table)

    while True:
        prompt = __prompt()

        while prompt == "new":
            rprint("Reiniciando conversación 🆕")
            messages = [
                context,
            ]
            # Reinicializamos messages tan sólo con el contexto, no se tienen en cuenta mensajes y respuestas anteriores
            prompt = __prompt()

        messages.append({"role": "user", "content": prompt, })
        response_content = "Respuesta que daría ChatGPT"
        """     
        # Guardamos el prompt
        chat_completion = client.chat.completions.create(
            messages=messages,
            # Mensajes para generar respuestas
            model=MODEL_ENGINE,
            # Modelo a utilizar para generar respuestas
            temperature=0.7,
            # Concreción de las respuestas. Entre 0 y 2, más concretas cuanto más cerca de 0. También
            n=1,
            # Número de respuestas
        )

        response_content = chat_completion.choices[0].message
        """

        messages.append({"role": "assistant", "content": response_content})
        # Contexto de las respuestas: vamos guardando cada respuesta del chat para que durante la conversación tenga en cuenta las respuestas anteriores.
        rprint(f"\n💬 [green]{response_content}[/green]")


if __name__ == "__main__":
    typer.run(main)
