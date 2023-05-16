# dokku-prefect

## Create Dokku app

On your server (where Dokku is installed):
``` sh
dokku apps:create prefect
dokku postgres:create prefect
dokku postgres:link prefect prefect
```

## CI/CD envs

In order to enable Dokku auto deployment after a commit / PR to _main_ branch, you need to set Repo secrets in Github repo's settings:

1. Open
Settings -> Secrets and variables -> Actions -> New repository secret

2. Set variables
- SSH_PRIVATE_KEY (`cat .ssh/id_rsa` & copy-paste your key)
- DOKKU_HOST  (e.g. myserver.dokku.com)
- DOKKU_APP_NAME (e.g. prefect)