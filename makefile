.PHONY: all
all: style.css

style.css: style.scss
	sass style.scss > style.css

.PHONY: lint
lint:
	jshint js/*.js

.PHONY: clean
clean:
	rm -f style.css *~
