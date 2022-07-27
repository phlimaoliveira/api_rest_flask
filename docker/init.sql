CREATE TABLE musicos (
    id serial PRIMARY KEY,
    nome varchar(100) UNIQUE NOT NULL,
    genero_musical varchar(100) NOT NULL,
    musica_mais_famosa varchar(300) NOT NULL
);

INSERT INTO musicos(nome, genero_musical, musica_mais_famosa) VALUES ('Alok', 'Eletrônica', 'Hear Me Now');
INSERT INTO musicos(nome, genero_musical, musica_mais_famosa) VALUES ('Jorge e Mateus', 'Sertanejo', 'Louca de Saudade');
INSERT INTO musicos(nome, genero_musical, musica_mais_famosa) VALUES ('Guns N Roses', 'Hard Rock', 'Sweet Child O Mine');
INSERT INTO musicos(nome, genero_musical, musica_mais_famosa) VALUES ('System of a down', 'Rock', 'Chop Suey');