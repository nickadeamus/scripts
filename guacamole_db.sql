createdb guacamole_db

ls schema/
001-create-schema.sql  002-create-admin-user.sql

cat schema/*.sql | psql -d guacamole_db -f -

CREATE TYPE
CREATE TYPE
CREATE TYPE
CREATE TABLE
CREATE INDEX
...
INSERT 0 1
INSERT 0 4
INSERT 0 3


psql -d guacamole_db
psql (9.3.6)
Type "help" for help.

guacamole=# CREATE USER guacamole_user WITH PASSWORD 'some_password';
CREATE ROLE
guacamole=# GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA public TO guacamole_user;
GRANT
guacamole=# GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public TO guacamole_user;
GRANT
guacamole=# \q

$ psql -d guacamole_db
psql (9.3.6)
Type "help" for help.

guacamole=# GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA public TO guacamole_user;
GRANT
guacamole=# GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public TO guacamole_user;
GRANT
guacamole=# \q
