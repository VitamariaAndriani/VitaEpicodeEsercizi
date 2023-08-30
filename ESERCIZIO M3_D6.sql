create database Esercizio_m3_d6;

create table Studente (
matricola_studente varchar(255),
nome_studente varchar(255),
città varchar(255),
	primary key (matricola_studente));

create table Corso (
codice_corso varchar(255),
nome_corso varchar(255),
matricola_docente varchar(255),
	primary key (codice_corso),
    constraint fk_matricola_docente_Corso_Docente foreign key (matricola_docente) 
    references Docente (matricola_docente) on update cascade on delete no action);

create table Docente (
matricola_docente varchar(255),
nome_docente varchar(255),
	primary key (matricola_docente,nome_docente));

create table Esame (
codice_corso varchar(255),
matricola_studente varchar(255),
data date not null,
voto float,
settore_scientifico varchar(255),
	primary key (codice_corso,matricola_studente),
    constraint fk_matricola_studente_Esame_Studente foreign key (matricola_studente) 
    references Studente(matricola_studente) on update cascade on delete no action,
    constraint fk_Esame_corso_corso foreign key (codice_corso) 
    references Corso(codice_corso) on update cascade on delete no action);
    
select max(voto_esame), min(voto_esame), avg(voto_eame),Studente.matricola_studente,Studente.nome_studente
  from Esame
  inner join Studente on Esame.matricola_studente=Studente.matricoa_studente
  group by Studente.matricola_studente,Studente.nome_studente;
  
select max(voto_esame) as voto_max, min(voto_esame), avg(voto_eame),Studente.matricola_studente,Studente.nome_studente
  from Esame
  inner join Studente on Esame.matricola_studente=Studente.matricoa_studente
  group by Studente.matricola_studente,Studente.nome_studente 
  having avg(Esame.voto_esame)>25 and COUNT(DISTINCT(Esame.data_esame))>=10
  order by voto_max asc;
  
  
  
create database Esercizio_m3_d6_parte2;
-- STUDENTE(matricola_studente,nome_studente,anno_laurea,titolo_studio,voto_laurea)
/*
DIPARTIMENTO(codice_dipartimento,nome_dipartimento,settore_scientifico,numero_docenti)
CONCORSOMASTER(codice_master,codice_dipartimento,data_pubblicazione,data_scadenza,numero_posti_disponibili)
PARTECIPACONCORSOMASTER(codice_dipartimento,codice_master,matricola_studente,data_invio_domanda)
*/

select Studente.nome_studente,Studente.matricola_studente,Dipartimento.settore_scientifico
from Studente,Dipartimento,Partecipaconcorsomaster
where Studente.matricola_studente=Partecipaconcorsomaster.mastricola_studente 
and Dipartimento.codice_dipartimento=Partecipaconcorsomaster.codice_dipartimento
group by Studente.matricola_studente,Studente.nome_studente
having count(Partecipaconcorsomaster.codice_master)>=3 
order by Studente.nome_studente;

select Dipartimento.nome_dipartimento,Dipartiemento.settore_scientifico, count(Concorsomaster.Codcie_master)
from Dipartimento 
inner join Concorsomaster on Dipartimento.concorso_dipartimento=Concorsomaster.codice_dipartimento
where Dipartimento.nome_dipartimento not in(select Concorsomaster.Codcie_dipartimento
											from Concorsomaster
											where Concorsomaster.numero_posti_disponibili>=7)
group by Dipartimento.nome_dipartimento,Dipartiemento.settore_scientifico;

SELECT s.Matricola, s.NomeStudente
FROM studente s
JOIN partecipaconcorsomaster pcm on pcm.MatricolaStudente=s.Matricola
JOIN concorsomaster cm on cm.CodiceMaster=pcm.CodiceMaster
WHERE s.VotoLaurea>100
GROUP BY s.Matricola, s.NomeStudente
HAVING COUNT(cm.CodiceMaster)>=2 AND COUNT(DISTINCT cm.DataPubblicazione) < COUNT(cm.CodiceMaster) ; 


  
  
  
  
  
  
  