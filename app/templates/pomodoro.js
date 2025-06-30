let timer;
let timeLeft = 25 * 60;

function startPomodoro() {
    clearInterval(timer); // resetar caso clique de novo
    timeLeft = 25 * 60;
    timer = setInterval(() => {
        if (timeLeft <= 0) {
            clearInterval(timer);
            alert("Tempo encerrado! Faça uma pausa.");
        } else {
            timeLeft--;
            document.getElementById("timer").innerText = formatTime(timeLeft);
        }
    }, 1000);
}

function formatTime(seconds) {
    const min = Math.floor(seconds / 60);
    const sec = seconds % 60;
    return `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
}
