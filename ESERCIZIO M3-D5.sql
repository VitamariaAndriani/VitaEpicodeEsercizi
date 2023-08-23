create database esercizio_D5_M3_parte1;

use esercizio_D5_M3_parte1;

create table Disco (
nro_serie_disco varchar(255),
titolo_album varchar(255) not null,
anno year,
prezzo dec(4,2) unsigned,
    primary key (nro_serie_disco));

create table Esecuzione (
codice_reg varchar(255),
titolo_canzone varchar(255),
anno year,
   primary key (codice_reg));
   
create table Autore (
nome_autore varchar(255),
titolo_canzone varchar(255),
anno year,
 primary key (nome_autore,titolo_canzone));
 
  create unique index index_autore
  on Autore (nome_autore,titolo_canzone);
  
create table Cantante (
nome_cantante varchar(255),
codice_reg varchar(255),
  primary key (codice_reg),
     constraint fk_codice_reg_Cantante_Esecuzione foreign key (codice_reg) references Esecuzione(codice_reg) on update cascade on delete no action);
  
  create unique index index_cantante
  on Cantante (nome_cantante,codice_reg);
  
create table Contiene (
nro_serie_disco varchar(255),
codice_reg int unsigned,
nro_prog int unsigned,
   primary key (nro_serie_disco,codice_reg),
        constraint fk_nro_serie_disco_Contiene_Disco foreign key (nro_serie_disco) references Disco(nro_serie_disco) on update cascade on delete no action,
        constraint fk_codice_reg_Contiene_Esecuzione foreign key (codice_reg) references Esecuzione(codice_reg) on update cascade on delete no action);
        
select Cantante.nome_cantante
from Cantante 
inner join Esecuzione on Cantante.codice_reg=Esecuzione.codice_reg
inner join Autore on Autore.titolo_canzone=Esecuzione.titolo_canzone
where Autore.nome_autore_autore=Cantante.nome_cantante and  Autore.nome_autore like "D%";

select Disco.titolo_album
from Disco
inner join Contiene on Disco_nro_serie_disco=Contiene.nro_serie_disco
inner join Esecuzione on Esecuzione.codice_reg=Contiene.codice_reg
where Esecuzione.anno is null;

select Cantante.nome_cantante
from Cantante
where Cantante2.nome_cantante not in
(select Cantante.nome_cantante 
     from Cantante as Cantante2
     inner join Cantante as Cantante3 on Cantante2.codice_reg=Cantante3.codice_reg 
     where Cantante2.nome_cantante>Cantante3.nome_cantante)

create database esercizio_D5_M3_parte2;

use esercizio_D5_M3_parte2;


create table Studente (
matricola_studente varchar(255),
nome_studente varchar(255),
città varchar(255),
	primary key (matricola_studente));

create table Corso (
codice_corso varchar(255),
nome_corso varchar(255),
matricola_docente varchar(255),
	primary key (codice_corso));

create table Docente (
matricola_docente varchar(255),
nome_docente varchar(255),
	primary key (matricola_docente,nome_docente));

create table Esame (
codice_esame varchar(255),
matricola_studente varchar(255),
data date not null,
voto float,
settore_scientifico varchar(255),
	primary key (codice_esame,matricola_studente),
    constraint fk_matricola_studente_Esame_Studente foreign key (matricola_studente) 
    references Studente(matricola_studente) on update cascade on delete no action,
    constraint fk_Esame_corso_Esame foreign key (codice_esame) 
    references Corso(codice_corso) on update cascade on delete no action);
    
select Esame.matricola_studente,Studente.citta_studente,Studente.nome_studente,Docente.nome_docente,Esame.codice_esame   
from Esame 
inner join Corso on Esame.codice_esame=Corso.codice_corso
inner join Docente on Corso.matricola_docente=Docente.matricola_docente
inner join Studente on Studente.matricola_studente=Esame.matricola_studente
where Esame.voto>28;

select Docente.nome_docente,Esame.settore_scientifico,Corso.nome_corso
from Docente
inner join Corso on Corso.matricola_docente=Docente.matricola_docente
inner join Esame on Corso.codice_corso=Esame.codice_esame





 



