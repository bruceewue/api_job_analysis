GIT_TAG := $(shell git describe --abbrev=0 --tags)

# 安裝環境
install-python-env:
	pipenv sync

# 建立 dev 環境變數
gen-dev-env-variable:
	python genenv.py

# 建立 staging 環境變數
gen-staging-env-variable:
	VERSION=STAGING python genenv.py

# 建立 release 環境變數
gen-release-env-variable:
	VERSION=RELEASE python genenv.py

# 啟動 api
up-api:
	docker-compose -f api.yml up
	
# 建立 docker image
build-image:
	docker build -f Dockerfile -t bruceewue/api:${GIT_TAG} .

# 推送 image
push-image:
	docker push bruceewue/api:${GIT_GIT_TAG}

# 部屬 api
deploy-api:
	GIT_TAG=${GIT_TAG} docker stack deploy --with-registry-auth -c api.yml api

# 測試覆蓋率
test-cov:
	pipenv run pytest --cov-report term-missing --cov-config=.coveragerc --cov=./api/ tests/

format:
	black -l 40 api tests

