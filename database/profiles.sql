CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30),
    email VARCHAR(100),
    firstname VARCHAR(25),
    lastname VARCHAR(25)
);

INSERT INTO users (username, email, firstname, lastname)
VALUES ('testuser', 'testuser@test.com', 'Lester', 'Tester');

INSERT INTO users (username, email, firstname, lastname)
VALUES ('eviluser', 'eviluser@test.com', 'EVIL', 'Tester');