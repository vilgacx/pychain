test:
	python3 src/test.py

clean:
	rm -rf src/__pycache__

serve:
	python3 src/api.py
