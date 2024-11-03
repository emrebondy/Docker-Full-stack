CREATE TABLE message(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(200)
);

INSERT INTO message (nom)
 VALUES ('Hello World');