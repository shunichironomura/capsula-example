import os
import random
from collections.abc import Collection
from typing import Annotated, NoReturn

import matplotlib.pyplot as plt
import typer
from matplotlib.axes import Axes
from rich.console import Console

app = typer.Typer()
console = Console()


def _sample_points_in_unit_square(*, n_samples: int, seed: int | None = None) -> list[tuple[float, float]]:
    rng = random.Random(seed)
    return [(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(n_samples)]


def _plot_points(points: Collection[tuple[float, float]], ax: Axes) -> Axes:
    xs_inside = [x for x, y in points if x**2 + y**2 <= 1]
    ys_inside = [y for x, y in points if x**2 + y**2 <= 1]
    xs_outside = [x for x, y in points if x**2 + y**2 > 1]
    ys_outside = [y for x, y in points if x**2 + y**2 > 1]

    ax.set_aspect("equal", "box")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.scatter(xs_inside, ys_inside, color="blue", s=0.5, alpha=0.5, label="Inside Circle")
    ax.scatter(xs_outside, ys_outside, color="red", s=0.5, alpha=0.5, label="Outside Circle")
    ax.add_patch(plt.Circle((0, 0), 1, color="black", fill=False, linestyle="-"))  # type: ignore[attr-defined]
    ax.set_title("Monte Carlo Sampling for π Estimation")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    return ax


@app.command()
def main(
    n_samples: Annotated[int, typer.Option(..., help="Number of random samples to generate")] = 1_000,
    seed: Annotated[
        int | None,
        typer.Option(..., help="Random seed for reproducibility. If not provided, a random seed is used."),
    ] = None,
) -> NoReturn:
    """Estimate the value of π using the Monte Carlo method."""
    # Sample points and estimate π
    points = _sample_points_in_unit_square(n_samples=n_samples, seed=seed)
    n_points_inside_circle = sum(1 for x, y in points if x**2 + y**2 <= 1)
    pi_estimate = 4 * n_points_inside_circle / n_samples
    console.print(f"Total samples: {n_samples}")
    console.print(f"Points inside circle: {n_points_inside_circle}")
    console.print(f"Estimated value of π: [bold green]{pi_estimate}[/bold green]")

    # Plot the points
    fig, ax = plt.subplots(figsize=(6, 6))
    _plot_points(points, ax)

    # Add Capsula run name to the plot if available
    # Run with `capsula run -- uv run python scripts/calc_pi.py...` to see the run name on the plot
    if (capsula_run_name := os.getenv("CAPSULA_RUN_NAME")) is not None:
        plt.suptitle(f"Run: {capsula_run_name}", y=0.98, fontsize=10, color="gray")

    fig.tight_layout()
    fig.savefig("monte_carlo_pi_estimation.png")

    raise typer.Exit


if __name__ == "__main__":
    app()
