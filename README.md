# `datediff`

CLI to compute the difference between two dates.

> **Set up Instructions**
    * Run `make build` to create a conda environment.
    * Activate conda environment and locally install the package with `pip install path/to/datediff`

> **Usage instructions**
    * Input date must follow the convention `YYYY-MM-DD`.

> **Development**
    * Run tests using `make test-unit`.
    * Run styling using `make style-inplace`.

**Usage**:

```console
$ datediff [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `get-diff`

## `datediff get-diff`

**Usage**:

```console
$ datediff get-diff [OPTIONS]
```

**Options**:

* `--date1 TEXT`
* `--date2 TEXT`
* `--help`: Show this message and exit.
