CREATE TABLE ecm_cores (
    pk_ecm_color BIGINT AUTO_INCREMENT PRIMARY KEY,
    na_color VARCHAR(55) NOT NULL,
    hex_cod VARCHAR(7) NOT NULL
);

CREATE TABLE ecm_catalogo (
    pk_ecm_product BIGINT AUTO_INCREMENT PRIMARY KEY,
    nce BIGINT,
    fk_color BIGINT,
    sku VARCHAR(255) AS (CONCAT(nce, ' ', fk_color)) STORED,
    na_product VARCHAR(55) NOT NULL,
    na_description VARCHAR(255) NOT NULL,
    total_vl VARCHAR(25) NOT NULL,
    installments JSON NULL,
    images JSON NULL,
    FOREIGN KEY (fk_color) REFERENCES ecm_cores(pk_ecm_color)
);

CREATE TABLE ecm_categorias (
    pk_ecm_category BIGINT AUTO_INCREMENT PRIMARY KEY,
    na_category VARCHAR(55) NOT NULL
);

CREATE TABLE ecm_produto_categoria (
    pk_ecm_product BIGINT,
    pk_ecm_category BIGINT,
    PRIMARY KEY (pk_ecm_product, pk_ecm_category),
    FOREIGN KEY (pk_ecm_product) REFERENCES ecm_catalogo(pk_ecm_product),
    FOREIGN KEY (pk_ecm_category) REFERENCES ecm_categorias(pk_ecm_category)
);

CREATE TABLE ecm_eventos (
    pk_ecm_event BIGINT AUTO_INCREMENT PRIMARY KEY,
    tp_event VARCHAR(55) NOT NULL,
    payload JSON NOT NULL,
    origin VARCHAR(55) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP NULL
);