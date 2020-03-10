

fetch('http://127.0.0.1:5000/api/display-shows-data-in-table')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
            });
