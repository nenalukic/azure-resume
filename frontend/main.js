// This is the script that will fetch and display the counter.
// window.addEventListener('DOMContentLoaded', (event) => {
//     getVisitCount();
// });

const functionApiUrl = 'https://getmyresumecounter.azurewebsites.net/api/GetCounter?code=4htINawlMfvhJkUQ91g6w4OuW-h5jbr_gJHUyPKSxIJVAzFuW-ZrMQ==';
const localFunctionApi = 'http://localhost:7071/api/GetCounter'; 

const getVisitCount = () => {
    let count = 30;
    fetch(functionApiUrl)
    .then(response => {
        return response.text()
    })
    .then(response => {
        console.log("Website called function API.",response);
        count = response;
        document.getElementById('counter').innerText = count;
    }).catch(function(error) {
        console.log(error);
    });
    return count;
}

getVisitCount();