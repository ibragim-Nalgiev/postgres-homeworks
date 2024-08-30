-- 1. Создать таблицу student с полями student_id serial,
--first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student (
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
)


-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar;

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birth_date, phone) VALUES('IBragim', 'NAlgiev', '1996-09-29', '89197305174');
INSERT INTO student (first_name, last_name, birth_date, phone) VALUES('IBrashka', 'NAlgievskiy', '1997-09-29', '89197305175');
INSERT INTO student (first_name, last_name, birth_date, phone) VALUES('IBra55gim', 'NA55lgiev', '1999-09-29', '79197305174');


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY;