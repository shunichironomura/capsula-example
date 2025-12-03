import random
from typing import Annotated, NoReturn

import typer
from rich.console import Console

app = typer.Typer()
console = Console()
error_console = Console(stderr=True)


def _sample_points(n_samples: int, *, seed: int | None = None) -> int:
    rng = random.Random(seed)

    n_inside_circle = 0
    for _ in range(n_samples):
        x = rng.uniform(-1, 1)
        y = rng.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            n_inside_circle += 1

    return n_inside_circle


@app.command()
def main(
    n_samples: Annotated[int, typer.Option(..., help="Number of random samples to generate")],
    seed: Annotated[
        int | None,
        typer.Option(..., help="Random seed for reproducibility. If not provided, a random seed is used."),
    ] = None,
) -> NoReturn:
    """Estimate the value of π using the Monte Carlo method."""
    n_inside_circle = _sample_points(n_samples, seed=seed)
    pi_estimate = 4 * n_inside_circle / n_samples
    error_console.print(f"Total samples: {n_samples}")
    error_console.print(f"Points inside circle: {n_inside_circle}")
    console.print(f"Estimated value of π: [bold green]{pi_estimate}[/bold green]")
    raise typer.Exit


if __name__ == "__main__":
    app()
