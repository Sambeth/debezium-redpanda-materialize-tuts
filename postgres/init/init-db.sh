#!/bin/bash

psql -v ON_ERROR_STOP=1 --username "" --dbname "" <<-EOSQL
  -- set write-ahead log level to logical
  ALTER SYSTEM SET wal_level = logical;

  CREATE SCHEMA IF NOT EXISTS inventory;

  CREATE TABLE inventory.deliveries
		( delivery_id integer NOT NULL,
		  delivery_date date NOT NULL,
		  sender varchar(255),
		  receiver varchar(255),
		  CONSTRAINT delivery_id_pk PRIMARY KEY (delivery_id)
		);

	CREATE PUBLICATION inventorypub FOR TABLE inventory.deliveries;

  CREATE USER debezium_user WITH PASSWORD 'debezium' REPLICATION LOGIN;

  GRANT USAGE ON SCHEMA inventory TO debezium_user;
  GRANT SELECT ON ALL TABLES IN SCHEMA inventory TO debezium_user;
EOSQL