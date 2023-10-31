// This is the script that will fetch and display the counter.
// window.addEventListener('DOMContentLoaded', (event) => {
//     getVisitCount();
// });


const functionApi = ''; 

const getVisitCount = () => {
    let count = 30;
    fetch(functionApi)
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