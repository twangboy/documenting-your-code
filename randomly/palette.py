import matplotlib.pyplot as plt
import requests
from matplotlib.figure import Figure


def plot_palette(model: str) -> Figure:
    """
    Display five color swatches side-by-side

    Args:
        model (str): The type of model to create. Must be ond of [default, ui]

    Returns:
        Figure: A matplotlib figure object
    """
    # Validate the model
    if model not in {"default", "ui"}:
        raise ValueError(f"{model} is not supported.")

    # Create the data structure for post to colormind
    data = f'{{"model": "{model}"}}'

    # Post to the colormind api and get the palette
    response = requests.post("http://colormind.io/api/", data=data)
    palette = response.json()

    # Not sure what this is parsing
    fig, axs = plt.subplots(figsize=(10, 2), nrows=1, ncols=5)

    # Not sure why we're doing this, if we're not returning axs
    for idx, color in enumerate(palette["result"]):
        color_decimal = [val / 256 for val in color]
        axs[idx].set_facecolor(color_decimal)

        axs[idx].set_title(color)
        axs[idx].set_xticks([])
        axs[idx].set_yticks([])

    return fig
