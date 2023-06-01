import pynecone as pc
from pcconfig import config
from ..states import State


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text(
                "Random Number Generator",
            ),
            pc.text(
                State.randomNumber,
                font_size="1.5em",
                font_weight="bold"
            ),
            pc.input(
                placeholder="Max Number",
                value=State.maxNumberInput,
                on_change=State.set_max,
                border_color="black",
                rounded="0.25em"
            ),
            pc.button(
                "Generate",
                on_click=State.set_random,
                padding="0.5em",
                background_color="green",
                color="white",
                rounded="0.25em"
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )
