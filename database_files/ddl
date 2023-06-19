CREATE TABLE ifest.termo_lgpd (
	id serial4 NOT NULL,
	texto text NULL,
	"data" timestamp NULL,
	CONSTRAINT termo_lgpd_pkey PRIMARY KEY (id)
);

CREATE TABLE ifest.user_termo (
	id serial4 NOT NULL,
	id_user int8 NULL,
	id_termo int8 NULL,
	"data" timestamp NULL,
	CONSTRAINT user_termo_pkey PRIMARY KEY (id)
);

CREATE TABLE ifest.produto_decoracao (
	id int4 NOT NULL DEFAULT nextval('ifest.nome_da_tabela_id_seq'::regclass),
	nome_decoracao varchar(255) NOT NULL,
	valor int4 NULL,
	CONSTRAINT nome_da_tabela_pkey PRIMARY KEY (id)
);

CREATE TABLE ifest.produto_review (
	id_user varchar(256) NULL,
	division_name varchar(512) NULL,
	department_name varchar(50) NULL,
	class_name varchar(50) NULL,
	clothing_id varchar(50) NULL,
	title varchar(512) NULL,
	review_text varchar(512) NULL,
	alike_feedback_count varchar(512) NULL,
	rating varchar(512) NULL,
	"recommend_index) VALUES" varchar(256) NULL,
	id int8 NULL,
	recommend_index int8 NULL
);

CREATE TABLE ifest.usuario_novo (
	id serial4 NOT NULL,
	email varchar(255) NOT NULL,
	idade int4 NULL,
	id_localizacao int4 NULL,
	CONSTRAINT usuario_novo_pkey PRIMARY KEY (id)
);
