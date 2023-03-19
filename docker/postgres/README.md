**POSTGRES**
---

Postgres configuration with docker.

**Table of contents:**

- [Command line connection](#command-line-connection)
- [Databases management](#databases-management)


# Command line connection

Connect to postgres container bash:

```bash
cd postgres && docker-compose exec postgres bash
```

Connect to postgres:

```bash
psql -U postgres
```

# Databases management

Create database:

```sql
CREATE DATABASE <DB_NAME>;
```

Show databases:

```sql
SELECT datname FROM pg_database;
```
