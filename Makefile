project_name = search_demo
data_container_name = $(project_name)_data

build:
	docker compose build

run:
	docker compose -p $(project_name) up -d

stop:
	docker compose -p $(project_name) stop

.build-data:
	docker build data -t $(data_container_name)

images: .build-data
	docker run --rm -v $(shell pwd)/ui/dist/images:/images --env-file $(shell pwd)/.env $(data_container_name) extract-images

import: .build-data
	docker run --rm --env-file $(shell pwd)/.env --network $(project_name)_default $(data_container_name) import

