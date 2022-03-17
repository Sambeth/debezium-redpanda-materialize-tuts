import requests


def register_connector(url, connector_config):
    try:
        response = requests.post(url=url, json=connector_config)

        if response.status_code == 201:
            print(response)
        else:
            print(response.status_code)
            print(response.json())

    except Exception as e:
        raise e


if __name__ == "__main__":
    connector_config = {
      "name": "debezium-tracking-connector",
      "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "plugin.name": "pgoutput",
        "database.hostname": "postgres",
        "database.port": "5432",
        "database.user": "debezium_user",
        "database.password": "debezium",
        "database.dbname": "postgres",
        "database.server.name": "debezium",
        "schema.whitelist": "inventory",
        "publication.name": "inventorypub"
      }
    }

    url = "http://localhost:8083/connectors/"

    register_connector(url=url, connector_config=connector_config)
