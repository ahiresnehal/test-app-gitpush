# Two-tier application example   

Example that shows how to control the order of service startup with Docker Compose.

# TL;DR

Start both services with:

```bash
docker-compose up
```

You should see output similar to the one below:

```
Starting two-tier-app-example_db_1 ... done
Recreating two-tier-app-example_app_1 ... done
Attaching to two-tier-app-example_db_1, two-tier-app-example_app_1
db_1   |
db_1   | PostgreSQL Database directory appears to contain a database; Skipping initialization
db_1   |
db_1   | 2020-12-01 18:29:32.309 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1   | 2020-12-01 18:29:32.311 UTC [1] LOG:  could not create IPv6 socket for address "::": Address family not supported by protocol
db_1   | 2020-12-01 18:29:32.316 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1   | 2020-12-01 18:29:32.346 UTC [20] LOG:  database system was shut down at 2020-12-01 18:28:48 UTC
db_1   | 2020-12-01 18:29:32.351 UTC [1] LOG:  database system is ready to accept connections
db_1   | 2020-12-01 18:29:33.175 UTC [27] LOG:  incomplete startup packet
app_1  | 2020-12-01 18:29:33 INFO     client Properties: {'user': 'spongebob', 'dbname': 'ocean', 'host': 'db', 'port': '5432', 'tty': '', 'options': '', 'sslmode': 'prefer', 'sslcompression': '0', 'gssencmode': 'disable', 'krbsrvname': 'postgres', 'target_session_attrs': 'any'}
app_1  |
app_1  | 2020-12-01 18:29:33 INFO     client You are connected to ('PostgreSQL 10.15 on x86_64-pc-linux-musl, compiled by gcc (Alpine 9.3.0) 9.3.0, 64-bit',)
app_1  |
app_1  | 2020-12-01 18:29:33 INFO     client PostgreSQL connection was closed
two-tier-app-example_app_1 exited with code 0
```
