# Developer shortcuts for local setup and workflow.

.PHONY: install train shell actions test

install:
	pip install -r requirements.txt

train:
	rasa train

shell:
	rasa shell

actions:
	rasa run actions

test:
	rasa test
