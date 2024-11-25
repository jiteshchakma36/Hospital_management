ABOUT THE PROJECT


The presented models gives the user an overview of how database systems are put to use in real life scenarios by taking a hospital as an example. 
The model accounts for appointments between the patient and the doctor, the patient’s past medical history and Functional Requirement -
The model utilizes the flask package of Python to structure the front end of the system. 

Data Normalization


Functional Dependencies -

Patient :{ID,name,age,gender}

Appointment :{date, time, id}

Medical History : {apptID, date , diagnosis}

Doctor : {doctorID, name, age}

On basis if the functional dependencies that exist in the table, we realize that the entire database has been normalized upto 3 NF.

Table Utilized


Patient

Doctor

Appointment

Medical History

Relations between the tables -


Books between tables Patient and Appointment to signify the patient’s competency to book an appointment. The relation is a 1 : N relation.
Takes between tables Doctor and Appointment to signify the doctor’s vacancy to take a consultation. The relation is a 1 : 1 relation.
Record between tables Appointment and Medical History to demonstrate the pass record of a patient
