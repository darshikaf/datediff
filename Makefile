.PHONY: build clean test-unit style-check style-inplace

build:
	conda env create -f .conda/environment.template.yaml

style-check:
	isort --multi-line=3 --trailing-comma --force-grid-wrap=0 \
    --use-parentheses --line-width=120 --section-default=THIRDPARTY --project=app \
    --force-sort-within-sections --check .
	black --line-length 120 --check .

style-inplace:
	isort --multi-line=3 --trailing-comma --force-grid-wrap=0 \
    --use-parentheses --line-width=120 --section-default=THIRDPARTY --project=app \
    --force-sort-within-sections .
	black --line-length 120 .

test-unit:
	pytest -s
	pytest --cov=datediff tests/