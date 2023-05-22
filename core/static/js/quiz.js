
const url = window.location.href
const quizBox = document.getElementById('quiz-box')
let data
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
const activateTimer = (time) =>{

    if(time.toString().length < 2){
        timerBox.innerHTML = `<b>0${time}:00</b>`
    }else{
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer =setInterval(() =>{
        seconds --
        if (seconds < 0){
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2){
            displayMinutes = '0' + minutes
        }else {
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2){
            displaySeconds = '0' + seconds
        }else {
            displaySeconds = seconds
        }

        if(minutes === 0 && seconds === 0){
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('O Tempo Acabou')
                sendData()
            }, 500)


        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1009)
}

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
            activateTimer(response.tempo)
        },
    error: function (error){

    }
})

const quizForm = document.getElementById('quiz-form')
const  csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () =>{
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if(el.checked){
            data[el.name] = el.value
        }else{
            if(!data[el.name]){
                data[el.name] = null
                }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response){
            const results = response.results
            quizForm.classList.add('not-visible')

            scoreBox.innerHTML = `${response.passed ? 'Parabéns ' : 'Ops... Não foi dessa vez'} | Sua pontuação é ${response.score.toFixed(2)}%} `

            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for(const [question, resp] of Object.entries(res)){
                    resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    if (resp=='Não respondido'){
                        resDiv.innerHTML += ' - Não respondido'
                        resDiv.classList.add('bg-danger')
                    }else{
                        const answer = resp['respondido']
                        const correto = resp['resp_correta']

                        if(answer==correto){
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` ** Respondido: ${answer}`
                        }else{
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | Resposta correta: ${correto}`
                            resDiv.innerHTML += ` | Sua Resposta: ${answer}`
                        }
                    }
                }

                resultBox.append(resDiv)
            })
        },
        error: function (error){
            console.log(error)

        }
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})