from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Placeholder, Static


class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """
    
class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """


class UtilityContainersExample(App):
    CSS_PATH = "layout.css"

    def compose(self) -> ComposeResult:
        yield Header(id="Taskwise")
        yield Footer(id="Automate Everything Efficiently")
        yield Horizontal(
            Vertical(
                Static("One"),
                Static("Two"),
                classes="column",
            ),
            Vertical(
                Static("Three"),
                Static("Four"),
                classes="column",
            ),
        )


if __name__ == "__main__":
    app = UtilityContainersExample()
    app.run()