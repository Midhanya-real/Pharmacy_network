<h1>Список путей:</h1>
<h2>Начальная ссылка: http://127.0.0.1:8000/pharmacies/</h2>

<ul>
    <h3>Методы POST</h3>
    <li>medication/add/ - добавление медикамента</li>
    <li>add_item/ - привязка медикамента к аптеке</li>
</ul>

<ul>
    <h3>Методы PUT</h3>
    <li>medication/update/{key} - обновление информации о медикаменте (данные вводятся полностья)</li>
</ul>

<ul>
    <h3>Методы GET</h3>
    <li>all/ - список аптек</li>
    <li>detail/{key} - детально об отдельной аптеке</li>
    <li>detail/{key}/items - список товарор по аптеке</li>
    <li>all/city={city} - сортировка аптеки по городу</li>
    <li>medication/all/ - список всех медикаментов</li>
    <li>medication/detail/{key} - детально о каждом медикаменте</li>
</ul>

