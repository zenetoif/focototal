let timerDisplay = document.getElementById('timer');
let startPauseBtn = document.getElementById('startPauseBtn');
let resetBtn = document.getElementById('resetBtn');
let skipBtn = document.getElementById('skipBtn');

let pomodoroDuration = 25 * 60; // 25 minutos em segundos
let shortBreakDuration = 5 * 60; // 5 minutos em segundos
let longBreakDuration = 15 * 60; // 15 minutos em segundos

let timer; 
let timeLeft = pomodoroDuration;
let isRunning = false;
let onBreak = false;
let cycles = 0;

function updateTimerDisplay() {
    let minutes = Math.floor(timeLeft / 60);
    let seconds = timeLeft % 60;
    timerDisplay.textContent = `${minutes.toString().padStart(2,'0')}:${seconds.toString().padStart(2,'0')}`;
}

function startTimer() {
    if (isRunning) return;
    isRunning = true;
    startPauseBtn.textContent = 'Pausar';
    timer = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateTimerDisplay();
        } else {
            clearInterval(timer);
            isRunning = false;
            if (!onBreak) {
                cycles++;
                if (cycles % 4 === 0) {
                    timeLeft = longBreakDuration;
                    alert('Hora do intervalo longo! Relaxa por 15 minutos.');
                } else {
                    timeLeft = shortBreakDuration;
                    alert('Hora do intervalo curto! Pausa de 5 minutos.');
                }
                onBreak = true;
            } else {
                timeLeft = pomodoroDuration;
                onBreak = false;
                alert('Intervalo finalizado! Hora de focar por 25 minutos.');
            }
            updateTimerDisplay();
            startPauseBtn.textContent = 'Iniciar';
        }
    }, 1000);
}

function pauseTimer() {
    if (!isRunning) return;
    clearInterval(timer);
    isRunning = false;
    startPauseBtn.textContent = 'Continuar';
}

startPauseBtn.addEventListener('click', () => {
    if (!isRunning) {
        startTimer();
    } else {
        pauseTimer();
    }
});

resetBtn.addEventListener('click', () => {
    clearInterval(timer);
    isRunning = false;
    timeLeft = pomodoroDuration;
    onBreak = false;
    cycles = 0;
    updateTimerDisplay();
    startPauseBtn.textContent = 'Iniciar';
});

skipBtn.addEventListener('click', () => {
    clearInterval(timer);
    isRunning = false;
    if (onBreak) {
        timeLeft = pomodoroDuration;
        onBreak = false;
        alert('Intervalo pulado! Hora de focar.');
    } else {
        timeLeft = shortBreakDuration;
        onBreak = true;
        alert('Pomodoro pulado! Hora do intervalo curto.');
    }
    updateTimerDisplay();
    startPauseBtn.textContent = 'Iniciar';
});

updateTimerDisplay();
