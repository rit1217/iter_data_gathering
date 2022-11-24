include .env


.PHONY: install
install:
	python3 -m venv .\
		&& source ./bin/activate \
		&& pip3 install -r requirements.txt \
		&& deactivate


.PHONY: tat/extract
tat/extract:
	source ./bin/activate \
		&& python3 -m TAT_raw_data -e
	