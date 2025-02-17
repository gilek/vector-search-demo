.PHONY: build extract-images

run:
	docker compose up -d

.build-data-container:
	docker build data -t search-data

images: .build-data-container
	docker run --rm -v $(shell pwd)/ui/dist/images:/images --env-file $(shell pwd)/.env search-data extract-images

import: .build-data-container
	docker run --rm --env-file $(shell pwd)/.env search-data import

