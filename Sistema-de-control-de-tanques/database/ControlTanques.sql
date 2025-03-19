--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: eventos; Type: TABLE; Schema: public; Owner: proyecto
--

CREATE TABLE public.eventos (
    id integer NOT NULL,
    tipo_evento character varying(50) NOT NULL,
    fecha_hora timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    tanque_id integer,
    descripcion text,
    duracion interval,
    CONSTRAINT eventos_tipo_evento_check CHECK (((tipo_evento)::text = ANY (ARRAY[('llenado'::character varying)::text, ('vaciado'::character varying)::text, ('fallo'::character varying)::text, ('transferencia'::character varying)::text])))
);


ALTER TABLE public.eventos OWNER TO proyecto;

--
-- Name: eventos_id_seq; Type: SEQUENCE; Schema: public; Owner: proyecto
--

CREATE SEQUENCE public.eventos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.eventos_id_seq OWNER TO proyecto;

--
-- Name: eventos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: proyecto
--

ALTER SEQUENCE public.eventos_id_seq OWNED BY public.eventos.id;


--
-- Name: sensores; Type: TABLE; Schema: public; Owner: proyecto
--

CREATE TABLE public.sensores (
    id integer NOT NULL,
    tipo character varying(50) NOT NULL,
    subtipo character varying(50),
    valor double precision NOT NULL,
    tanque_id integer,
    CONSTRAINT sensores_tipo_check CHECK (((tipo)::text = ANY (ARRAY[('temperatura'::character varying)::text, ('presion'::character varying)::text, ('nivel'::character varying)::text])))
);


ALTER TABLE public.sensores OWNER TO proyecto;

--
-- Name: sensores_id_seq; Type: SEQUENCE; Schema: public; Owner: proyecto
--

CREATE SEQUENCE public.sensores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sensores_id_seq OWNER TO proyecto;

--
-- Name: sensores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: proyecto
--

ALTER SEQUENCE public.sensores_id_seq OWNED BY public.sensores.id;


--
-- Name: tanques; Type: TABLE; Schema: public; Owner: proyecto
--

CREATE TABLE public.tanques (
    id integer NOT NULL,
    nivel_actual integer NOT NULL,
    capacidad integer NOT NULL,
    tipo_pintura character varying(100),
    CONSTRAINT tanques_capacidad_check CHECK ((capacidad > 0)),
    CONSTRAINT tanques_nivel_actual_check CHECK ((nivel_actual >= 0))
);


ALTER TABLE public.tanques OWNER TO proyecto;

--
-- Name: tanques_id_seq; Type: SEQUENCE; Schema: public; Owner: proyecto
--

CREATE SEQUENCE public.tanques_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tanques_id_seq OWNER TO proyecto;

--
-- Name: tanques_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: proyecto
--

ALTER SEQUENCE public.tanques_id_seq OWNED BY public.tanques.id;


--
-- Name: valvulas; Type: TABLE; Schema: public; Owner: proyecto
--

CREATE TABLE public.valvulas (
    id integer NOT NULL,
    estado character varying(50) NOT NULL,
    tanque_origen_id integer,
    tanque_destino_id integer,
    velocidad_flujo double precision,
    CONSTRAINT valvulas_estado_check CHECK (((estado)::text = ANY (ARRAY[('abierta'::character varying)::text, ('cerrada'::character varying)::text])))
);


ALTER TABLE public.valvulas OWNER TO proyecto;

--
-- Name: valvulas_id_seq; Type: SEQUENCE; Schema: public; Owner: proyecto
--

CREATE SEQUENCE public.valvulas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.valvulas_id_seq OWNER TO proyecto;

--
-- Name: valvulas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: proyecto
--

ALTER SEQUENCE public.valvulas_id_seq OWNED BY public.valvulas.id;


--
-- Name: eventos id; Type: DEFAULT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.eventos ALTER COLUMN id SET DEFAULT nextval('public.eventos_id_seq'::regclass);


--
-- Name: sensores id; Type: DEFAULT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.sensores ALTER COLUMN id SET DEFAULT nextval('public.sensores_id_seq'::regclass);


--
-- Name: tanques id; Type: DEFAULT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.tanques ALTER COLUMN id SET DEFAULT nextval('public.tanques_id_seq'::regclass);


--
-- Name: valvulas id; Type: DEFAULT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.valvulas ALTER COLUMN id SET DEFAULT nextval('public.valvulas_id_seq'::regclass);


--
-- Data for Name: eventos; Type: TABLE DATA; Schema: public; Owner: proyecto
--

COPY public.eventos (id, tipo_evento, fecha_hora, tanque_id, descripcion, duracion) FROM stdin;
\.


--
-- Data for Name: sensores; Type: TABLE DATA; Schema: public; Owner: proyecto
--

COPY public.sensores (id, tipo, subtipo, valor, tanque_id) FROM stdin;
1	temperatura	TempF	25	1
2	temperatura	TempH	22	1
3	temperatura	TempT	23	1
4	nivel	\N	100	1
5	nivel	\N	0	2
6	nivel	\N	100	3
7	nivel	\N	0	4
\.


--
-- Data for Name: tanques; Type: TABLE DATA; Schema: public; Owner: proyecto
--

COPY public.tanques (id, nivel_actual, capacidad, tipo_pintura) FROM stdin;
2	0	80000	Pintura Base Aceite
1	100	80000	Pintura Base Agua
3	100	80000	Pintura Base Aceite
4	0	80000	Pintura Base Agua
\.


--
-- Data for Name: valvulas; Type: TABLE DATA; Schema: public; Owner: proyecto
--

COPY public.valvulas (id, estado, tanque_origen_id, tanque_destino_id, velocidad_flujo) FROM stdin;
3	cerrada	3	4	\N
4	cerrada	4	3	\N
2	abierta	2	1	\N
1	abierta	1	2	\N
\.


--
-- Name: eventos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: proyecto
--

SELECT pg_catalog.setval('public.eventos_id_seq', 1, false);


--
-- Name: sensores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: proyecto
--

SELECT pg_catalog.setval('public.sensores_id_seq', 7, true);


--
-- Name: tanques_id_seq; Type: SEQUENCE SET; Schema: public; Owner: proyecto
--

SELECT pg_catalog.setval('public.tanques_id_seq', 4, true);


--
-- Name: valvulas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: proyecto
--

SELECT pg_catalog.setval('public.valvulas_id_seq', 4, true);


--
-- Name: eventos eventos_pkey; Type: CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.eventos
    ADD CONSTRAINT eventos_pkey PRIMARY KEY (id);


--
-- Name: sensores sensores_pkey; Type: CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.sensores
    ADD CONSTRAINT sensores_pkey PRIMARY KEY (id);


--
-- Name: tanques tanques_pkey; Type: CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.tanques
    ADD CONSTRAINT tanques_pkey PRIMARY KEY (id);


--
-- Name: valvulas valvulas_pkey; Type: CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.valvulas
    ADD CONSTRAINT valvulas_pkey PRIMARY KEY (id);


--
-- Name: eventos eventos_tanque_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.eventos
    ADD CONSTRAINT eventos_tanque_id_fkey FOREIGN KEY (tanque_id) REFERENCES public.tanques(id) ON DELETE CASCADE;


--
-- Name: sensores sensores_tanque_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.sensores
    ADD CONSTRAINT sensores_tanque_id_fkey FOREIGN KEY (tanque_id) REFERENCES public.tanques(id) ON DELETE CASCADE;


--
-- Name: valvulas valvulas_tanque_destino_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.valvulas
    ADD CONSTRAINT valvulas_tanque_destino_id_fkey FOREIGN KEY (tanque_destino_id) REFERENCES public.tanques(id) ON DELETE CASCADE;


--
-- Name: valvulas valvulas_tanque_origen_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: proyecto
--

ALTER TABLE ONLY public.valvulas
    ADD CONSTRAINT valvulas_tanque_origen_id_fkey FOREIGN KEY (tanque_origen_id) REFERENCES public.tanques(id) ON DELETE CASCADE;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES TO proyecto;


--
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TYPES TO proyecto;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS TO proyecto;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES TO proyecto;


--
-- PostgreSQL database dump complete
--

