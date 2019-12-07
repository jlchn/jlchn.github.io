``` bash
# add a database
sudo -i -u postgrespsql 
CREATE DATABASE test_manager OWNER test_manager ENCODING 'UTF8' LC_COLLATE 'en_US.utf8' LC_CTYPE 'en_US.utf8' TEMPLATE template0;
# drop database
sudo -u postgres psqldrop database test_manager
# add a user
CREATE USER test_manager with password 'test_manager';
# add permissions for a user
GRANT ALL ON ALL TABLES IN SCHEMA public TO test_manager;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO test_manager;GRANT ALL ON ALL FUNCTIONS IN SCHEMA public TO test_manager;
# dump schema
pg_dump -h localhost -U test_manager -s test_manager > exportFile.dmp
# dump data of all tables
pg_dump -h localhost -U test_manager --column-inserts test_manager > my_dump.sql
# import schema and data from files
# method 1
psql -h localhost -d test_manager_script_refactor -U test_manager -f schema.dmp psql -h localhost -d test_manager_script_refactor -U test_manager -f data.sql
# method 2
gunzip < /home/jiangli/Downloads/10.28.40.0-1515117003-test_manager.gz | psql test_manager
#select last id of a sequence
SELECT last_value FROM test_id_seq;
```