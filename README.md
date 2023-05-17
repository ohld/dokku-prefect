# dokku-prefect

## How to deploy

### TL;DR:

1. Create Dokku app, link Postgres
2. Clone this Template
3. Set CI/CD envs in Github repo settings
4. Push something to trigger deploy
5. Enable Https if required

### Create Dokku app

On your server (where Dokku is installed):
``` sh
dokku apps:create prefect
dokku config:set prefect POSTGRES_DATABASE_SCHEME=postgresql+asyncpg \
    PREFECT_API_URL=https://prefect.yourdomain.com/api

dokku postgres:create prefect
dokku postgres:link prefect prefect -a PREFECT_API_DATABASE_CONNECTION
```

Read more about [Prefect database connection](https://docs.prefect.io/latest/host/#configuring-a-postgresql-database) for self-hosted production deployment.

### CI/CD envs

In order to enable Dokku auto deployment after a commit / PR to _main_ branch, you need to set Repo secrets in Github repo's settings:

1. Open
Settings -> Secrets and variables -> Actions -> New repository secret

2. Set variables
- SSH_PRIVATE_KEY (`cat .ssh/id_rsa` & copy-paste your key)
- DOKKU_HOST  (e.g. myserver.dokku.com)
- DOKKU_APP_NAME (e.g. prefect)


### How to enable Https

``` sh
dokku letsencrypt:enable prefect
```

### How to enable https basic auth

WIP: I'm waiting for an answer at https://github.com/dokku/dokku-http-auth/issues/21

``` sh
dokku plugin:install https://github.com/dokku/dokku-http-auth.git
dokku http-auth:enable prefect admin admin_password
dokku http-auth:add-allowed-ip prefect IP_ADDRESS_MASK_HERE
dokku ps:restart prefect
```