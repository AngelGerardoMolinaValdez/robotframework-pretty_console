import argparse


def parse_entry_arguments(values: list) -> object:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="Robot Framework - Pretty Console",
        usage="""Añade al ejecutar en la consola de comandos,
        cada paso que ejecuta, este mismo puede venir sin color o con color
        y el estilo puede ser con el color en la letra o el fondo.""",
        prefix_chars="@"
    )
    parser.add_argument(
        "@color", "@c", type=str, const="store_true")
    parser.add_argument(
        "@style", "@s", type=str, choices=["Back", "Fore"], const="store_true")
    return parser.parse_args()
