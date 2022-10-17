from typing import Dict, List

from rich.panel import Panel
from rich.table import Table

from textual.app import App
from textual.widget import Widget
from textual.reactive import Reactive

card_template = """┌────────┐
│      %s │
│   %s    │
│        │
│        │
└────────┘"""


class Title(Widget):
    def on_mount(self):
        self.layout_size = 3

    def render(self):
        style = "green bold"
        table = Table.grid(padding=(0, 1), expand=True)
        table.style = style
        table.add_column(justify="left", ratio=1)
        table.add_column(justify="left", ratio=1)
        table.add_column(justify="center", ratio=1)
        table.add_column(justify="right", ratio=1)
        table.add_column(justify="right", ratio=1)
        table.add_row(
            "♠", "♥", "Console Poker", "♣", "♦"
        )
        title = Panel(table, style=style)

        return title


class Hand(Widget):
    style: Reactive[str] = Reactive("")
    cards: Reactive[List[Dict[str,str]]] = Reactive([{}])

    def __init__(self, *, name = None, cards = {}, style = "white on dark_green") -> None:
        super().__init__(name=name)
        self.cards = cards
        self.style = style

    def render(self):
        cards = [card_template % (card["suit"], card["value"]) for card in self.cards]

        table = Table.grid(padding=(1, 1), expand=False)
        table.style = self.style

        for i in range(len(cards)):
            table.add_column(f"card{i}", justify="center", ratio=1)

        table.add_row(
            self.name, *["" for _ in range(len(cards) - 1)]
        )

        table.add_row(
            *cards
        )

        hand = table

        return hand



class ConsolePoker(App):
    """A Console Poker Textual App"""

    async def on_mount(self) -> None:
        """Create and dock the widgets."""

        cards = [
            {
                "suit": "♠",
                "value": "2"
            },
            {
                "suit": "♥",
                "value": "A"
            },
            {
                "suit": "♣",
                "value": "Q"
            }
        ]

        await self.view.dock(Title(), edge="top")
        await self.view.dock(
            Hand(style="green", cards=cards),
            Hand(style="green", cards=cards),
            Hand(style="green", cards=cards),
            edge="left"
        )


ConsolePoker.run(title="Console Poker", log="textual.log")
