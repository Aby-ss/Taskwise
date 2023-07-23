from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder


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


class Section(Placeholder):
    DEFAULT_CSS = """
    Section {
        height: 5;
        width: 1fr;
        border: tall $background;
    }
    """


class Column(VerticalScroll):
    DEFAULT_CSS = """
    Column {
        height: 1fr;
        width: 32;
        margin: 0 2;
    }
    """

    def compose(self) -> ComposeResult:
        for Section_no in range(1, 20):
            yield Section(id=f"Section{Section_no}")


class SectionScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")
        with HorizontalScroll():
            yield Column()
            yield Column()
            yield Column()
            yield Column()


class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(SectionScreen())


if __name__ == "__main__":
    app = LayoutApp()
    app.run()
