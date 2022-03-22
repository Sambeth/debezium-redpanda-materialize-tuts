#!/bin/bash

psql -v ON_ERROR_STOP=1 --username "" --dbname "" <<-EOSQL
  -- set write-ahead log level to logical
  ALTER SYSTEM SET wal_level = logical;

  CREATE SCHEMA IF NOT EXISTS inventory;

  CREATE TABLE inventory.products
		( product_id varchar(255) NOT NULL,
		  quantity integer NOT NULL,
		  created_at TIMESTAMP,
		  updated_at TIMESTAMP,
		  CONSTRAINT product_id_pk PRIMARY KEY (product_id)
		);

	ALTER TABLE inventory.products REPLICA IDENTITY FULL;

	CREATE PUBLICATION inventorypub FOR TABLE inventory.products;

  CREATE USER debezium_user WITH PASSWORD 'debezium' REPLICATION LOGIN;

  GRANT USAGE ON SCHEMA inventory TO debezium_user;
  GRANT SELECT ON ALL TABLES IN SCHEMA inventory TO debezium_user;
EOSQL