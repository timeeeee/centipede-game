.PHONY: all
all: style.css bundle.js

style.css: style.scss
	sass style.scss > style.css

bundle.js: main.js centipede.js
	browserify js/main.js -o bundle.js

.PHONY: lint
lint:
	jshint js/*.js

.PHONY: clean
clean:
	rm -f style.css bundle.js
