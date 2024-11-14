
PHONY: run

run: build execute

execute:
	@py build/nevis.py

build: clean
	@pypack

clean:
	@if [ -e "build/nevis.py" ]; then \
    	rm.exe build/nevis.py; \
	fi

