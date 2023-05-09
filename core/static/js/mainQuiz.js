
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')



const url = window.location.href
modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const nome = modalBtn.getAttribute('data-nome')
    const numQuestoes = modalBtn.getAttribute('data-questions')
    const dificuldade = modalBtn.getAttribute('data-dificuldade')
    const ptsParaPassar = modalBtn.getAttribute('data-pass')
    const tempo = modalBtn.getAttribute('data-tempo')


    modalBody.innerHTML = `
        <div class= "h5 mb-3"> Você tem certeza que quer começar? "<b>${nome}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>Dificuldade: <b>${dificuldade}</b></li>
                <li>Número de questões: <b>${numQuestoes}</b></li>
                <li>Pontos necessários para passar: <b>${ptsParaPassar}%</b></li>
                <li>Tempo: <b>${tempo} minutos</b></li>
            </ul>
        </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}) )