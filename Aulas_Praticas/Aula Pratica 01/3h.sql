-- Table: public.t1

-- DROP TABLE public.t1;

CREATE TABLE public.t1
(
    c1 integer NOT NULL,
    c2 character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "PK_T1" PRIMARY KEY (c1)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.t1
    OWNER to postgres;