CREATE DATABASE IF NOT EXISTS vprojects;
USE vprojects;

CREATE TABLE IF NOT EXISTS colaboradores (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS avaliacoes (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    colaborador_id INT,
    data_avaliacao DATE,
    FOREIGN KEY (colaborador_id) REFERENCES colaboradores(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS criterios (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    tipo ENUM('comportamental', 'execucao') NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS notas (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    avaliacao_id INT,
    criterio_id INT,
    nota DECIMAL(2,1) NOT NULL CHECK (nota BETWEEN 0 AND 10),
    justificativa TEXT,
    FOREIGN KEY (avaliacao_id) REFERENCES avaliacoes(id) ON DELETE CASCADE,
    FOREIGN KEY (criterio_id) REFERENCES criterios(id) ON DELETE CASCADE
);

INSERT INTO criterios (descricao, tipo) VALUES
('Sentimento de dono', 'comportamental'),
('Resiliencia nas adversidades', 'comportamental'),
('Organizacao no trabalho', 'comportamental'),
('Capacidade de aprender', 'comportamental'),
('Ser \"team player\"', 'comportamental'),
('Entregar com qualidade', 'execucao'),
('Atender aos prazos', 'execucao'),
('Fazer mais com menos', 'execucao'),
('Pensar fora da caixa', 'execucao');