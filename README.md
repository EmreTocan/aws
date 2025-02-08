İlk olarak bir python ile api oluşturdum bunların içinde
Kullandığım Endpoint Örnekleri

POST	/tasks	Yeni bir görev oluşturur
GET	/tasks	Tüm görevleri listeler
GET	/tasks/{id}	Belirli bir görevi getirir
PUT	/tasks/{id}	Belirli bir görevi günceller
DELETE	/tasks/{id}	Belirli bir görevi siler

Ardından bu api'yi dockerize etmek için Dockerfile ve requirements.txt dosyası oluşturdum ve pushladım. 
Ardından SSH ile AWS'de oluşturduğum Ubuntu sunucuda pull ettim ve container'ı çalıştırdım. 

