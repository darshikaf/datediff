import pytest
from typer.testing import CliRunner

from datediff.cli import app
from datediff.errors import InvalidDate, InvalidInput, InvalidMonth, InvalidYear

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert b"CLI to compute the difference between two dates." in result.stdout_bytes


def test_diff():
    result = runner.invoke(app, ["get-diff", "--date1=2014-09-01", "--date2=2020-09-02"])
    assert result.exit_code == 0
    assert b"Difference between 2014-09-01 and 2020-09-02 in days: 2192" in result.stdout_bytes


def test_invalid_input():
    with pytest.raises(
        InvalidInput,
        match="Invalid input to CLI. Date must be of format YYYY-MM-DD.",
    ):
        runner.invoke(
            app,
            ["get-diff", "--date1=2014-09-01", "--date2=2014-0902"],
            catch_exceptions=False,
        )


def test_invalid_year():
    with pytest.raises(InvalidYear, match="Valid values: 1000 - 9999."):
        runner.invoke(
            app,
            ["get-diff", "--date1=20211-03-02", "--date2=2021-03-03"],
            catch_exceptions=False,
        )


def test_invalid_month():
    with pytest.raises(InvalidMonth, match="Invalid value 13 for Month"):
        runner.invoke(
            app,
            ["get-diff", "--date1=2021-13-02", "--date2=2021-03-03"],
            catch_exceptions=False,
        )


def test_invalid_date():
    with pytest.raises(InvalidDate, match="Invalid value 33 for Date"):
        runner.invoke(
            app,
            ["get-diff", "--date1=2021-03-33", "--date2=2021-03-03"],
            catch_exceptions=False,
        )
