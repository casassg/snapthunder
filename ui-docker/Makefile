all: build
build: build-client
push: push-client
.PHONY: push build


TAG_CLIENT = 1.0.8
PROJECT_NAME = snapthunderui

build-client:
	docker build -t casassg/$(PROJECT_NAME) .
	docker tag casassg/$(PROJECT_NAME) casassg/$(PROJECT_NAME):$(TAG_CLIENT)

push-client: build-client
	docker push casassg/$(PROJECT_NAME)
	docker push casassg/$(PROJECT_NAME):$(TAG_CLIENT)

clean:
	docker rmi casassg/$(PROJECT_NAME):$(TAG) || :
	docker rmi casassg/$(PROJECT_NAME) || : 