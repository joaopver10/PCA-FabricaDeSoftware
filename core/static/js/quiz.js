
const url = window.location.href
const quizBox = document.getElementById('quiz-box')
let data

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response){
        const data = response.data
        data.forEach(el =>{
            for (const [questoes, respostas] of Object.entries(el)){
                quizBox.innerHTML +=`
            <hr>
            <div class="mb-4">
                <b>${questoes}</b>
            </div>
            `
            respostas.forEach(resposta =>{
                quizBox.innerHTML +=`
                    <div>
                        <input type="radio" class="ans" id="${questoes}-${resposta}" name="${questoes}" value="${resposta}">
                        <label for="${questoes}" >${resposta}</label>
                    </div>
                `
            })
            }
        })
        },
    error: function (error){

    }
})