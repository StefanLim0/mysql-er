select a1.id, b.name from db.ac a1 join db.bc b on a1.id=b.id where a1.cnt > 10;
select a1.id, b.phone from db.bc a1 join db.de b on a1.id=b.uid where a1.status = 1;