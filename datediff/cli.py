from typing import List, Optional

import typer

from .date import ComputeDiff, Date
from .errors import InvalidDate, InvalidInput, InvalidMonth, InvalidYear

app = typer.Typer()


@app.callback()
def callback():
    """
    CLI to compute the difference between two dates.

    > **Set up Instructions**
        * Run `make build` to create a conda environment.
        * Activate conda environment and locally install the package with `pip install path/to/datediff`

    > **Usage instructions**
        * Input date must follow the convention `YYYY-MM-DD`.

    > **Development**
        * Run tests using `make test-unit`.
        * Run styling using `make style-inplace`.
    """


@app.command()
def get_diff(
    date1: str = typer.Option(None, "--date1", prompt=True),
    date2: str = typer.Option(None, "--date2", prompt=True),
):
    d1 = _process_input(date1)
    d2 = _process_input(date2)
    diff = ComputeDiff(date1=d1, date2=d2).get_diff()
    typer.echo(f"Difference between {date1} and {date2} in days: {diff}")


def _process_input(dt: str) -> Date:
    try:
        d = list(map(int, dt.split("-")))
    except:
        raise InvalidInput("Invalid input to CLI. Date must be of format YYYY-MM-DD.")
    _validate(d)
    return Date(**{"year": d[0], "month": d[1], "day": d[2]})


def _validate(d: List) -> Optional[Exception]:
    if not len(d) == 3:
        raise InvalidInput("Invalid input to CLI. Date must be of format YYYY-MM-DD.")
    if not (year := len(str(d[0]))) == 4:
        raise InvalidYear(f"Invalid value {d[0]} for Year. Valid values: 1000 - 9999.")
    if not (month := d[1]) in range(1, 13):
        raise InvalidMonth(f"Invalid value {month} for Month.")
    if (day := d[2]) > 31:
        raise InvalidDate(f"Invalid value {day} for Date.")
