# 🔐 Keycloak Setup for Authentication

This document shows how to setup the keycloak for authentication

---

## Step 1: Keycloak Installation

- Download Keycloak from [https://www.keycloak.org/downloads](https://www.keycloak.org/downloads)
- Docker Setup (Docker File):

```dockerfile
services:
  keycloak:
    image: quay.io/keycloak/keycloak
    container_name: keycloak
    command: start-dev
    ports:
      - "8080:8080"
    environment:
      - KEYCLOAK_ADMIN=admin
      - KEYCLOAK_ADMIN_PASSWORD=admin
    volumes:
      - ./custom-login-pages:/opt/keycloak/themes/custom-login-pages
      - keycloak_data:/opt/keycloak/data
```

- Run using

```bash
docker compose up --build
```

- After installation goto (<http://localhost:8080>) or (<http://auth.reskill.com>) or where it is installed

## Step - 2

1. Create a new realm named Reskilll-Auth
2. goto left panel and select clients and add a new client with client id (Remember this) and fill name for easier acccess
    1. Root URL = URL of starting Page
    2. Valid Redirect URL = After login/signup where to redirect
    3. Web Origins = * for any origin (or) valid URL for security purposes

## Step - 3

### Setting up a user with strong credintial for easier access from Backend

- Go to left panel and select users
- Add User ---> Fill all required Info ---> Create
- Select Created User ---> Credinatials Tab ---> Enter Password ---> Save
- Add the username and credentials to the backend for login

## Step - 4

### Setup URL's in Backend

- URL from where RESTAPI's can be accessed (<http://keycloak-url/realms/your-realm-name/protocol/openid-connect/token>)
- POST data into the above url with the following parameters

```json
granttype: 'password'
username: <your-username>
password: <your-password>
client-id: 'admin-cli'
```

- If the response is Admin Token then your login is successful and you can access **login page**