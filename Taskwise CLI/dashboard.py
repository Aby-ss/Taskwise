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


class Taskwise(App):
    CSS_PATH = "layout.css"

    def compose(self) -> ComposeResult:
        
        column_text = "Hey there!!"
        
        yield Header("Taskwise", show_clock=True)
        yield Footer("Automate Everything Efficiently")
        yield Horizontal(
            Vertical(
                Static(f"{column_text}"),
                Static(f"{column_text}"),
                classes="column",
            ),
            Vertical(
                Static(f"{column_text}"),
                Static(f"{column_text}"),
                classes="column",
            ),
        )


if __name__ == "__main__":
    app = Taskwise()
    app.run()