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
		
# .PHONY: load/mongodb
# load/mongodb:
# 	mongosh "mongodb+srv://iter.iuxqfey.mongodb.net/myFirstDatabase" --apiVersion 1 --username ${MONGODB_USERNAME} \
# 	&& ${MONGODB_PASSWORD} \
# 	&& mongoimport --uri "mongodb+srv://iteradmin:HzBYrU93SIYEjhNA@iter.iuxqfey.mongodb.net/?retryWrites=true&w=majority" -d iter-1 -c place_raw --type json --file ./temp/places.json --jsonArray