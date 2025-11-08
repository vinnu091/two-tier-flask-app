#!/bin/sh

set -e

echo "Waiting for MySQL to be ready..."
until mysql -h "$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;" >/dev/null 2>&1; do
  echo "MySQL is not ready yet..."
  sleep 3
done

echo "MySQL is up! Starting Flask..."
exec python app.py
