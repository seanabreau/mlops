CREATE TABLE experiment_data
(experiment_name text, learning_rate double precision, momentum double precision,
loss text);

\copy experiment_data FROM '/var/lib/postgresql/postgres_data/data.csv' csv header;
