import requests


def register_connector(url, connector_config):
    try:
        r = requests.post(url=url, json=connector_config)

        if r.status_code == 201:
            return "Success"
        else:
            print(r.status_code)
            print(r.json())

    except Exception as e:
        raise e


if __name__ == "__main__":
    connector_config = {
      "name": "debezium-postgres-connector",
      "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "postgres",
        "database.port": "5432",
        "database.user": "postgres",
        "database.password": "postgres",
        "database.dbname": "postgres",
        "database.server.name": "debezium",
        "schema.whitelist": "inventory"
      }
    }

    url = "http://localhost:8083/connectors/"

    register_connector(url=url, connector_config=connector_config)
