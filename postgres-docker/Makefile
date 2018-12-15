
all: psqlsnapthunder
push: push-psqlsnapthunder
.PHONY: push push-psqlsnapthunder psqlsnapthunder

TAG = 1.0.0

psqlsnapthunder:
	docker build -t casassg/psqlsnapthunder .
	docker tag casassg/psqlsnapthunder casassg/psqlsnapthunder:$(TAG)

push-psqlsnapthunder: psqlsnapthunder
	docker push casassg/psqlsnapthunder
	docker push casassg/psqlsnapthunder:$(TAG)

clean:
	docker rmi casassg/psqlsnapthunder:$(TAG) || :
	docker rmi casassg/psqlsnapthunder || :