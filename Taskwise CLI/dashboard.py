from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Placeholder, Static
from textual.widgets import Header, Footer

import requests
from rich.panel import Panel
from rich import box


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
        
        city = 'Dubai'
        api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
        response = requests.get(api_url, headers={'X-Api-Key': 'E9SmCxTQQtyVD79D96wfpg==7Z30WK1D8Do2AOcN'})

        if response.status_code == requests.codes.ok:
            json_data = response.json()

            overall_aqi = json_data['overall_aqi']
            CO_concentration = json_data['CO']['concentration']
            CO_aqi = json_data['CO']['aqi']
            PM10_concentration = json_data['PM10']['concentration']
            PM10_aqi = json_data['PM10']['aqi']
            SO2_concentration = json_data['SO2']['concentration']
            SO2_aqi = json_data['SO2']['aqi']
            PM25_concentration = json_data['PM2.5']['concentration']
            PM25_aqi = json_data['PM2.5']['aqi']
            O3_concentration = json_data['O3']['concentration']
            O3_aqi = json_data['O3']['aqi']
            NO2_concentration = json_data['NO2']['concentration']
            NO2_aqi = json_data['NO2']['aqi']

            air_quality = f"Overall Air Quality Index [aqi]: {overall_aqi}\n\n[b]C0 Conc.[/]: {CO_concentration}  [b]C0 AQI[/]: {CO_aqi}\n[b]PM10 Conc.[/]: {PM10_concentration}  [b]PM10 AQI[/]: {PM10_aqi}\n[b]SO2 Conc.[/]: {SO2_concentration}   [b]SO2 AQI[/]: {SO2_aqi}\n[b]PM25 Conc.[/]: {PM25_concentration}  [b]PM25 AQI[/]: {PM25_aqi}\n[b]O3 Conc.[/]: {O3_concentration}  [b]O3 AQI[/]: {O3_aqi}\n[b]NO2 Conc.[/]: {NO2_concentration}  [b]NO2 AQI[/]: {NO2_aqi}"
            
        column_text = f"{air_quality}"
        
        yield Header("Taskwise", classes="Header",)
        yield Footer("Automate Everything Efficiently")
        yield Horizontal(
            Vertical(
                Static(f"{column_text}"),
                Static(f"{column_text}"),
                classes="column",
            ),
            Vertical(
                Static(f"{column_text}"),
                classes="column",
            ),
        )
    
        def on_mount(self) -> None:
            self.Header.styles.background = "#9932CC"


if __name__ == "__main__":
    app = Taskwise()
    app.run()