# Precacher

Precacher continuously requests the newest blocks/transactions from [sidecar](https://github.com/vokracko/stocra-sidecar) and forces sidecar to cache them to speed up subsequent requests.
It uses [stocra-sdk-python](https://github.com/vokracko/stocra-sdk-python) under the hood and requires sidecar to be exposed to the internet. 


## How to run locally
Define the following variables in `.env` file:
```dotenv
# for sidecar running on `https://bitcoin-1.stocra.com this would be set to `bitcoin-1`
ENVIRONMENT=<node subdomain>
```

### Terminal
```bash
./scripts/entrypoint
```

### Docker compose
```bash
docker-compose up -d
```
