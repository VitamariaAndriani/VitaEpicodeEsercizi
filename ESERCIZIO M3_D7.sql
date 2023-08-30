-- esercizio M3-D7;

-- Creazione della tabella Dipendenti
CREATE TABLE Dipendenti (
    id_nome VARCHAR(255),
    cognome VARCHAR(255),
    email VARCHAR(255),
    numero_telefono VARCHAR(255),
    data_assunzione DATE,
    id_lavoro INT,
    salario DECIMAL(10, 2),
    id_manager INT,
    id_dipartimento INT,
		PRIMARY KEY (id_nome),
		FOREIGN KEY (id_lavoro) REFERENCES Dipendente(id_lavoro),
		FOREIGN KEY (id_manager) REFERENCES Dipendente(id_manager),
		FOREIGN KEY (id_dipartimento) REFERENCES Dipartimento(id_dipartimento)
);

INSERT INTO Dipendente (id, nome, cognome, email, numerotelefono, data_assunzione, id_lavoro, salario, id_manager, id_dipartimento)
VALUES
    (1, 'Mario', 'Rossi', 'mario.rossi@email.com', '1234567890', '2023-01-15', 1, 50000.00, 4, 1),
    (2, 'Luca', 'Bianchi', 'luca.bianchi@email.com', '9876543210', '2023-02-20', 2, 55000.00, 4, 2),
    (3, 'Anna', 'Verdi', 'anna.verdi@email.com', '5678901234', '2023-06-10', 1, 48000.00, 5, 1),
    (4, 'Giovanna', 'Marrone', 'giovanna.marrone@email.com', '6789012345', '2022-12-01', 3, 60000.00, 4, 2),
    (5, 'Paolo', 'Giallo', 'paolo.giallo@email.com', '3456789012', '2022-09-05', 2, 52000.00, 5, 3),
    (6, 'Roberto', 'Neri', 'roberto.neri@email.com', '1231231234', '2022-05-15', 2, 49000.00, 5, 2),
    (7, 'Giulia', 'Bianchi', 'giulia.bianchi@email.com', '4564564567', '2022-08-12', 1, 55000.00, 3, 3),
    (8, 'Elena', 'Verdi', 'elena.verdi@email.com', '7897897890', '2022-07-10', 3, 60000.00, 4, 1),
    (9, 'Massimo', 'Giallo', 'massimo.giallo@email.com', '2342342345', '2022-09-20', 1, 48000.00, 5, 2),
    (10, 'Laura', 'Rosa', 'laura.rosa@email.com', '3453453456', '2022-03-05', 2, 52000.00, 6, 3),
    (11, 'Simone', 'Marrone', 'simone.marrone@email.com', '5675675678', '2022-11-18', 1, 49000.00, 5, 1),
    (12, 'Francesca', 'Rossi', 'francesca.rossi@email.com', '7897897890', '2022-10-02', 3, 57000.00, 4, 2),
    (13, 'Marco', 'Neri', 'marco.neri@email.com', '1231231234', '2022-06-25', 2, 52000.00, 6, 3),
    (14, 'Sara', 'Verdi', 'sara.verdi@email.com', '2342342345', '2022-04-15', 1, 46000.00, 3, 1),
    (15, 'Davide', 'Giallo', 'davide.giallo@email.com', '4564564567', '2022-12-28', 2, 49000.00, 4, 2);


-- Creazione della tabella Dipartimento
CREATE TABLE Dipartimento (
    id_dipartimento INT PRIMARY KEY,
    nome_dip VARCHAR(50),
    id_manager INT,
    id_location INT,
    FOREIGN KEY (id_manager) REFERENCES Dipendente(id_manager),
    FOREIGN KEY (id_location) REFERENCES TabellaLocation(id_location)
);

INSERT INTO Dipartimento (id_dipartimento, nome_dip, id_manager, id_location)
VALUES
    (1, 'Amministrazione', 4, 101),
    (2, 'Vendite', 5, 102),
    (3, 'Produzione', 6, 103);
    

-- Visualizzare la data di assunzione dei manager ei loro id appartenenti al dipartimento 'Amministrazione' nel formato Nome mese, giorno, anno:
SELECT DATE_FORMAT(Dipendente.data_assunzione, '%M %e, %Y') AS Data_Assunzione, Dipendente.id
FROM Dipendente
inner join Dipartimento on Dipendente.id=Dipartimento.id_manager
WHERE Dipendente.id in (select Dipartimento.id_manager
from Dipartimento
where Dipartimento.nome_dip="Amministrazione");
	  
      
-- Visualizzare il nome e il cognome dei dipendenti assunti nel mese di Giugno:
SELECT Dipendente.nome,Dipendente.cognome, Dipendente.data_assunzione
FROM Dipendente
WHERE monthname(data_assunzione)="june";


-- Visualizzare gli anni in cui più di 10 dipendenti sono stati assunti:
SELECT YEAR(Dipendete.data_assunzione) AS Data_Assunzione
FROM Dipendente
GROUP BY year(Dipendente.data_assunzione)
HAVING count(*)>10;

-- Visualizzare il nome del dipartimento, il nome del manager, il salario del manager di tutti i manager la cui esperienza è maggiore di 5 anni:
SELECT Dipartimento.nome_dip, CONCAT(Dipendete.nome,' ', Dipendente.cognome), Dipendente_salario
FROM Dipartimento, Dipendente
WHERE Dipartimento.id_manager=Dipendete.id
and (year(now))-year(Dipendete.data_assunzione)>5; -- 5 anni * 365 giorni/anno=1825
     