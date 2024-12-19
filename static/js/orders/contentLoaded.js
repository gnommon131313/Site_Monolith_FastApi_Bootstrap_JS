export function initializeOnContentLoaded() {
    fetch('api/orders') // URL для получения данных
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось загрузить данные');
        }
        return response.json(); // Парсим JSON-ответ
    })
    .then(data => {
        // Вывод в консоль браузера (F12 что посмотреть)
        console.log(data);

        // Очищаем таблицу перед добавлением новых данных
        const newList = document.getElementById('orders-list');
        newList.innerHTML = '';

        // Заполняем таблицу полученными данными
        data.orders.forEach(function(order) {
            let row = `<tr>
                <td>${order.id}</td>
                <td>${order.date}</td>
                <td>${order.total}</td>
                <td>${order.product_id}</td>
                <td>${order.status}</td>
            </tr>`;
            newList.insertAdjacentHTML('beforeend', row);
        });
    })
    .catch(error => {
        alert(error.message);
    });
}