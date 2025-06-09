/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                                     */
/*  SAE204 - Implementation of the relational database schema (part1)  */
/*                                                                     */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ 

-- group : C24
-- author : ROUSSEL Mewen and FRANCEZ Matthias
-- date : Friday 2 may 2025

-- if the schema already exists, drop it --
DROP SCHEMA IF EXISTS partie1 cascade;

-- creation of the schema --
CREATE SCHEMA partie1;

-- go into the schema  --
SET SCHEMA 'partie1';

-- droping of the relation if already exists --
DROP TABLE IF EXISTS _resultat;
DROP TABLE IF EXISTS _programme;
DROP TABLE IF EXISTS _inscription;
DROP TABLE IF EXISTS _module;
DROP TABLE IF EXISTS _semestre;
DROP TABLE IF EXISTS _etudiant;
DROP TABLE IF EXISTS _candidat;
DROP TABLE IF EXISTS _individu;

-- creation of the relation "_individu" --
CREATE TABLE _individu (
    -- attributes --
    id_individu     INTEGER      NOT NULL,
    nom             VARCHAR(20)  NOT NULL,
    prenom          VARCHAR(20)  NOT NULL,
    date_naissance  DATE         NOT NULL,
    code_postal     VARCHAR(5)   NOT NULL,
    ville           VARCHAR(30)  NOT NULL,
    sexe            CHAR(1)      NOT NULL,
    nationalite     VARCHAR(7)   NOT NULL,
    INE             VARCHAR(11)  NOT NULL,

    -- constraints --
    CONSTRAINT individu_pk 
        PRIMARY KEY (id_individu),

    -- checks --
    CONSTRAINT individu_check_sexe
        CHECK (sexe = 'M' or sexe = 'F')
);

-- creation of the relation "_candidat" --
CREATE TABLE _candidat (
    -- attributes --
    no_candidat         INTEGER      NOT NULL,
    classement          VARCHAR(4),   -- NULL
    boursier_lycee      BOOLEAN      NOT NULL,
    profil_candidat     VARCHAR(40)  NOT NULL,
    etablissement       VARCHAR(50)  NOT NULL,
    dept_etablissement  VARCHAR(3)   NOT NULL,
    ville_etablissement VARCHAR(20)  NOT NULL,
    niveau_etude        VARCHAR(40)  NOT NULL,
    type_formation_prec VARCHAR(10)  NOT NULL,
    serie_prec          VARCHAR(50)  NOT NULL,
    dominante_prec      VARCHAR(50)  NOT NULL,
    specialite_prec     VARCHAR(50)  NOT NULL,
    LV1                 VARCHAR(50)  NOT NULL,
    LV2                 VARCHAR(50)  NOT NULL,
    -- attribute of the relation "_individu" --
    id_individu         INTEGER      NOT NULL,

    -- constraints --
    CONSTRAINT candidat_pk 
        PRIMARY KEY (no_candidat),
    
    CONSTRAINT candidat_fk_individu 
        FOREIGN KEY (id_individu)
            -- reference to the relation "_individu" --
            REFERENCES _individu(id_individu)
);

-- creation of the relation "_etudiant" --
CREATE TABLE _etudiant (
    -- attributes --
    code_nip                    VARCHAR(11)  NOT NULL,
    cat_socio_etu               VARCHAR(50)  NOT NULL,
    cat_socio_parent            VARCHAR(50)  NOT NULL,
    bourse_superieur            BOOLEAN      NOT NULL,
    mention_bac                 VARCHAR(20)  NOT NULL,
    serie_bac                   VARCHAR(40)  NOT NULL,
    dominante_bac               VARCHAR(40)  NOT NULL,
    specialite_bac              VARCHAR(50)  NOT NULL,
    mois_annee_obtention_bac    CHAR(7)      NOT NULL,
    -- attribute of the relation "_individu" --
    id_individu                 INTEGER      NOT NULL,

    -- constraints --
    CONSTRAINT etudiant_pk 
        PRIMARY KEY (code_nip),
    
    CONSTRAINT etudiant_fk_individu 
        FOREIGN KEY (id_individu)
            -- reference to the relation "_individu" --
            REFERENCES _individu(id_individu)
);

-- creation of the relation "_semestre" --
CREATE TABLE _semestre (
    -- attributes --
    id_semestre     INTEGER  NOT NULL,
    num_semestre    CHAR(5)  NOT NULL,
    annee_univ      CHAR(9)  NOT NULL,

    -- constraints --
    CONSTRAINT semestre_fk 
        PRIMARY KEY (id_semestre)
);

-- creation of the relation "_module" --
CREATE TABLE _module (
    -- attributes --
    id_module       CHAR(5)      NOT NULL,
    libelle_module  VARCHAR(50)  NOT NULL,
    ue              CHAR(2)      NOT NULL,

    -- constraints --
    CONSTRAINT module_pk 
        PRIMARY KEY (id_module)
);

-- creation of the relation "_inscription" --
CREATE TABLE _inscription (
    -- attributes --
    groupe_tp               CHAR(2)      NOT NULL,
    amenagement_evaluation  VARCHAR()    NOT NULL, -- ** not in the data ** --
    -- attribute of the relation "_etudiant" --
    code_nip                VARCHAR(11)  NOT NULL,
    -- attribute of the relation "_semestre" --
    id_semestre             INTEGER      NOT NULL,

    -- constraints --
    CONSTRAINT inscription_pk 
        PRIMARY KEY (code_nip, id_semestre),
    
    CONSTRAINT inscription_fk_etudiant 
        FOREIGN KEY (code_nip)
            -- reference to the relation "_etudiant" --
            REFERENCES _etudiant(code_nip),
    
    CONSTRAINT inscription_fk_semestre 
        FOREIGN KEY (id_semestre)
            -- reference to the relation "_semestre" --
            REFERENCES _semestre(id_semestre)
);

-- creation of the relation "_programme" --
CREATE TABLE _programme (
    -- attributes --
    coefficient REAL     NOT NULL,
    -- attribute of the relation "_module" --
    id_module   CHAR(5)  NOT NULL,
    -- attribute of the relation "_semestre" --
    id_semestre INTEGER  NOT NULL,

    -- constraints --
    CONSTRAINT programme_pk 
        PRIMARY KEY (id_module, id_semestre),
    
    CONSTRAINT programme_fk_module 
        FOREIGN KEY (id_module)
            -- reference to the relation "_module" --
            REFERENCES _module(id_module),
    
    CONSTRAINT programme_fk_semestre 
        FOREIGN KEY (id_semestre)
            -- reference to the relation "_semestre" --
            REFERENCES _semestre(id_semestre)
);

-- creation of the relation "_resultat" --
CREATE TABLE _resultat (
    -- attributes --
    moyenne     REAL        NOT NULL,
    -- attribute of the relation "_etudiant" --
    code_nip    VARCHAR(11) NOT NULL,
    -- attribute of the relation "_semestre" --
    id_semestre INTEGER     NOT NULL,
    -- attribute of the relation "_module" --
    id_module   CHAR(5)     NOT NULL,

    -- constraints --
    CONSTRAINT resultat_pk 
        PRIMARY KEY (code_nip, id_semestre, id_module),
    
    CONSTRAINT resultat_fk_etudiant
        FOREIGN KEY (code_nip)
            -- reference to the relation "_etudiant" --
            REFERENCES _etudiant(code_nip),
    
    CONSTRAINT resultat_fk_semestre
        FOREIGN KEY (id_semestre)
            -- reference to the relation "_semestre" --
            REFERENCES _semestre(id_semestre),
    
    CONSTRAINT resultat_fk_module
        FOREIGN KEY (id_module)
            -- reference to the relation "_module" --
            REFERENCES _module(id_module)
);

/* END OF FILE */