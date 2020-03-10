// fetch('http://127.0.0.1:5000/api/display-shows-data-in-table')
//             .then((response) => response.json())
//             .then((data) => {
//                 console.log(data);
//             });

let titelSort = document.querySelector('#titel');
titelSort.addEventListener('click', handelColumnTitleClick)

function handelColumnTitleClick() {
    console.log('title clicked');
    let column = 'shows.title';
    let data = {column};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };
    fetch('http://127.0.0.1:5000/api/sort-by-title', options);
}
