VERSION = 1.3.0

test:
	docker build --target test -t anagrams-env .
	docker run -it anagrams-env python -tt -m pytest --cov=anagrams --cov-report term-missing tests
