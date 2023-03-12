--ADAUGAM DATE IN TABELA DEPARTMENT
INSERT INTO DEPARTMENT(department_name) values('PR'); --id=1
INSERT INTO DEPARTMENT(department_name) values('IT'); --id=2
INSERT INTO DEPARTMENT(department_name) values('Logistics'); --id=3
INSERT INTO DEPARTMENT(department_name) values('HR'); --id=4
INSERT INTO DEPARTMENT(department_name) values('FirstAid'); --id=5
INSERT INTO DEPARTMENT(department_name) values('PhotoVideo'); --id=6


--ADAUGAM DATE IN TABELA VOLUNTEER

--departamentul Public Relations id =1
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Popescu', 'Maria', 'AC', 'popescumarius@gmail.com', '0756453423', 'Iasi', 1); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id)  
values ('Stan', 'Paula', 'ETTI', 'stanpaula@yahoo.com', '0756388899', 'Iasi', 1);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Nechifor', 'Cornel', 'IEEIA', 'nechifor14@yahoo.com', '0722556161', 'Vaslui', 1); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Miron', 'David', 'ETTI', 'mirond@gmail.com', '0766773466', 'Piatra Neamt', 1); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Constantinescu', 'Maria', 'CMMI', 'conm@gmail.com', '0766882345', 'Iasi', 1); 

--departamentul IT id = 2
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Munteanu', 'Andrei', 'AC', 'munteanu.andrei@yahoo.com', '0764201829', 'Vaslui', 2); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Ionescu', 'Ovidiu', 'ETTI', 'ovidiu.ionescu@yahoo.com', '0761734914', 'Iasi', 2);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Dabija', 'Eugen', 'ETTI', 'dabijaeugen@gmail.com', '0769932477', 'Piatra Neamt', 2);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Malaeru', 'Monica', 'DIMA', 'monicamalaeru@gmail.com', '0747730853', 'Iasi', 2);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id)
values ('Ghita', 'Emanuel', 'IEEIA', 'emanuelg@yahoo.com', '0729958729', 'Targu Frumos', 2);


--departamentul Logistics id = 3
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Palici', 'Nadia', 'AC', 'nadiapalici@yahoo.com', '0750856917', 'Vaslui', 3); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Malaia', 'Roberta', 'ETTI', 'malaiaroberta@yahoo.com', '0767888888', 'Iasi', 3);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Popescu', 'Alecu', 'ETTI', 'alecupopescu@gmail.com', '0769982227', 'Roman', 3);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Fratila', 'Cristi', 'Mecanica', 'cristifratila@gmail.com', '0724245555', 'Roman', 3);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Moldoveanu', 'Valentin', 'IEEIA', 'moldo.vali@yahoo.com', '0783718598', 'Bacau', 3);


--departmentul Human Resources
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Marguta', 'Clara', 'DIMA', 'claram@yahoo.com', '0754181405', 'Vaslui', 4); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id)
values ('Moldoveanu', 'Alberto', 'ETTI', 'albertom@yahoo.com', '0767888999', 'Iasi', 4);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Valculescu', 'Sabina', 'AC', 'sabina.val@gmail.com', '0769933227', 'Roman', 4);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Calin', 'Luminita', 'Mecanica', 'luminitacalin@gmail.com', '0724245500', 'Piatra Neamt', 4);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Negoita', 'Simona', 'IEEIA', 'simonanegoita@yahoo.com', '0777718778', 'Focsani', 4);

--departmanetul First Aid id = 5
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Nistor', 'Alexandru', 'DIMA', 'nistoralex@yahoo.com', '0775154953', 'Adjud', 5); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id)
values ('Vlasceanu', 'Camelia', 'ETTI', 'cameliav@yahoo.com', '0767382299', 'Iasi', 5);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Tomulescu', 'Sonia', 'IEEIA', 'tomulescus@gmail.com', '0764943227', 'Roman', 5);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Ilies', 'Madalina', 'Mecanica', 'madalinailies@gmail.com', '0723345550', 'Piatra Neamt', 5);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Dumitru', 'Smaranda', 'IEEIA', 'smarandadumi@yahoo.com', '0774418478', 'Targu Frumos', 5);

--departamentul Photo/Video id = 6
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Albu', 'Paul', 'DIMA', 'albupaul@yahoo.com', '0723153333', 'Adjud', 6); 
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Muresan', 'Antoniu', 'ETTI', 'muresanantoniu@yahoo.com', '0744381299', 'Iasi', 6);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Tudor', 'Sebastian', 'IEEIA', 'tudorsebi@gmail.com', '0764141127', 'Roman', 6);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Florescu', 'Teodora', 'AC', 'florescuteodora@gmail.com', '0723025520', 'Piatra Neamt', 6);
INSERT INTO VOLUNTEER(last_name, first_name, faculty, email, phone_number, city, department_id) 
values ('Manolache', 'Lucia', 'AC', 'luciamanolache@yahoo.com', '0722414678', 'Targu Frumos', 6);



--ADAUGAM DATE IN TABELA LOCATION
INSERT INTO LOCATION(city, county, street, number_of_street) values ('iasi', 'iasi', 'decebal', 14); 
INSERT INTO LOCATION(city, county, street, number_of_street) values ('piatra neamt', 'neamt', 'principala', 2); 
INSERT INTO LOCATION(city, county, street, number_of_street) values ('iasi', 'iasi', 'stefan cel mare', 15); 
INSERT INTO LOCATION(city, county, street, number_of_street) values ('iasi', 'iasi', 'pacurari', 10); 
INSERT INTO LOCATION(city, county, street, number_of_street) values ('iasi', 'iasi', 'smardan', 7); 


--ADAUGAM DATE IN TABELA EVENT
INSERT INTO EVENT(starttime, endtime, location_id) values 
(TO_TIMESTAMP('2023-02-23 14:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP('2023-02-23 16:00:00', 'YYYY-MM-DD HH24:MI:SS'), 1); 
INSERT INTO EVENT(starttime, endtime, location_id) values 
(TO_TIMESTAMP('2023-03-20 16:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP('2023-03-20 18:00:00', 'YYYY-MM-DD HH24:MI:SS'), 2); 
INSERT INTO EVENT(starttime, endtime, location_id) values 
(TO_TIMESTAMP('2023-06-14 14:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP('2023-06-14 16:00:00', 'YYYY-MM-DD HH24:MI:SS'), 3); 
INSERT INTO EVENT(starttime, endtime, location_id) values 
(TO_TIMESTAMP('2023-05-15 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP('2023-05-15 18:00:00', 'YYYY-MM-DD HH24:MI:SS'), 4); 
INSERT INTO EVENT(starttime, endtime, location_id) values 
(TO_TIMESTAMP('2023-01-28 14:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP('2023-01-28 17:00:00', 'YYYY-MM-DD HH24:MI:SS'), 5); 


--ADAUGAM DATE IN TABELA REQUIREMENT
--pentru evenimentul de id=1
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(1, 1, 1); --id 1
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(2, 1, 6); --id 2

--pentru evenimentul de id=2
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(1, 2, 2); --id 3

--pentru evenimentul de id=3
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(1, 3, 3); --id 4
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(1, 3, 4); --id 5

--pentru evenimentul de id=4
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(1, 4, 5); --id 6
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(2, 4, 6); --id 7

--pentru evenimentul de id=5
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(2, 5, 5); --id 8
INSERT INTO REQUIREMENT(number_of_volunteers, event_id, department_id) values(1, 5, 1); --id 9


--ADAUGAM DATE IN TABELA APPOINTMENT
--requirement 1
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (1,1);

--requirement 2
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (27, 2);
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (28, 2);

--requirement 3
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (8, 3);

--requirement 4
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (14, 4);

--requirement 5
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (17, 5);

--requirement 6
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (23, 6);

--requirement 7
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (29, 7);
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (30, 7);

--requirement 8
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (21, 8);
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (22, 8);

--requirement 9
INSERT INTO APPOINTMENT(volunteer_id, requirement_id) values (3, 9);

--ADAUGAM DATE IN TABELA OBSERVATION
INSERT INTO OBSERVATION(message, appointment_id) values ('fii acolo cu o ora mai devreme', 4);
INSERT INTO OBSERVATION(message, appointment_id) values ('sa aiba aparat foto', 3);
INSERT INTO OBSERVATION(message, appointment_id) values ('a intarziat', 10);
INSERT INTO OBSERVATION(message, appointment_id) values ('sa porti tricoul evenimentului', 7);
INSERT INTO OBSERVATION(message, appointment_id) values ('a stat peste program sa ajute', 12);
