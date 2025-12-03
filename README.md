# Capsula Example Repository

This repository demonstrates the use of Capsula.

## Prerequisites

- [Capsula](https://github.com/ut-issl/capsula)
- [uv](https://docs.astral.sh/uv/)

## Running the Example

### Running without Capsula

Run the script directly using `uv`:

```bash
uv run python scripts/calc_pi.py
```

This will print the estimated value of π to the console and output the plot to `monte_carlo_pi_estimation.png`.

You can specify the number of samples and a random seed:

```bash
uv run python scripts/calc_pi.py --n-samples 100000 --seed 42
```

### Running with Capsula

Run the script using Capsula to capture the execution:

```
❯ capsula run uv run python scripts/calc_pi.py --n-samples 100000 --seed 42
Run ID: 01KBHF79ZDF56GYAZFVZ1053JP, Name: purring-fear
Run directory: /Users/nomura/ghq/github.com/shunichironomura/capsula-example/.capsula/pi-estimation/2025-12-03/064330-purring-fear
Total samples: 100000
Points inside circle: 78507
Estimated value of π: 3.14028
```

Capsula run ID, run name, and run directory will be displayed.

The run directory contains the following files:

```
.capsula/pi-estimation/2025-12-03/064330-purring-fear
├── _capsula
│   ├── command.json
│   ├── metadata.json
│   ├── post-run.json
│   └── pre-run.json
├── capsula-example.patch
├── capsula.toml
├── monte_carlo_pi_estimation.png
├── pyproject.toml
└── uv.lock
```

Notice that the generated plot `monte_carlo_pi_estimation.png` is moved to the run directory.

And the run name is embedded in the plot image:

![Plot with embedded run name](assets/monte_carlo_pi_estimation.png)

You can list all runs using:

```
❯ capsula list
TIMESTAMP (UTC)      NAME                  COMMAND
-----------------------------------------------------------------------------------------------------------------
2025-12-03 06:43:30  purring-fear          uv run python scripts/calc_pi.py --n-samples 100000 --seed 42
2025-12-03 06:42:18  organic-honey         uv run python scripts/calc_pi.py --n-samples 10000 --seed 42
2025-12-03 06:42:09  fancy-cup             uv run python scripts/calc_pi.py
2025-12-03 06:35:54  calculating-geese     uv run python scripts/calc_pi.py --n-samples 100000 --seed 7
2025-12-03 06:35:32  incompetent-achieve   uv run python scripts/calc_pi.py --n-samples 100000 --seed 7
2025-12-03 06:33:41  cagey-bait            uv run python scripts/calc_pi.py --n-samples 100000 --seed 7
2025-12-03 06:33:25  bouncy-spiders        uv run python scripts/calc_pi.py
```
