CREATE TABLE public.users
(
    id bigserial NOT NULL,
    name text,
    password text NOT NULL,
    PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;