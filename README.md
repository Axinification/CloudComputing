# CloudComputing

Jako aplikację wybraliśmy API do sklepu z książkami, działa na prostych założenaich ale dodane są specjalne filtry a także całość zbudowana jest we frameworku Django z wykorzystaniem DRF. Prosty client jest dołączony do repozytorium


Aplikacja znajduje się pod tym adresem: http://20.238.8.233/books/


API /books:

***Pozyskać można w ten sposób wszystkie, pofiltrowane pozycje, lub konkretną pozycję po jej ID***

**GET** /books

**GET** /books?author="Tolkien"&from=2003&to=2022&acquired=false

**GET** /books/123

**POST** /books - Dane książki do wprowadzenia ręcznie należy podać w body requestu

**PATCH** /books/123 - Dane do zmiany w książe wybranej po id należy podać w body requestu

**DELETE** /books/123

API /import:

Import odbywa się przez komunikację z zewnętrznym API Google Books - https://www.googleapis.com/books/v1/volumes

**POST** /import - w body requestu powinien się znaleźć filter po którym szukamy - {"author": "nazwisko"}

Aplikacja znajduje się na wirtualnej maszynie w serwisie Azure, zostosowaliśmy bazę danych postgreSQL wraz z jej replikacją.

![image](https://user-images.githubusercontent.com/73855075/178123419-987a8118-5d2c-494f-8213-151d0d24fe32.png)

![image](https://user-images.githubusercontent.com/73855075/178123434-f4ccf6f3-d5f9-4d74-a396-93b7166fac68.png)
