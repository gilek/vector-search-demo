.PHONY: build extract-images

build:
	docker compose build

run: build
	docker compose up -d

.build-data:
	docker build data -t search-data

images: .build-data
	docker run --rm -v $(shell pwd)/ui/dist/images:/images --env-file $(shell pwd)/.env search-data extract-images

import: .build-data
	docker run --rm --env-file $(shell pwd)/.env search-data import

